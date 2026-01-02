import os
import json
import numpy as np
import torch
from sklearn.cluster import KMeans
from sklearn.preprocessing import OneHotEncoder, StandardScaler, LabelEncoder
from sklearn.metrics import silhouette_score, adjusted_rand_score, normalized_mutual_info_score
from sentence_transformers import SentenceTransformer
from scipy.optimize import linear_sum_assignment
from typing import List, Dict, Tuple, Optional
import warnings

warnings.filterwarnings('ignore')


class AttentionPoolingEncoder:
    
    def __init__(self, model_name: str = "all-mpnet-base-v2"):
        self.model = SentenceTransformer(model_name, device='cpu')
        self.tokenizer = self.model.tokenizer
        self.embedding_dim = self.model.get_sentence_embedding_dimension()
    
    def encode(self, texts: List[str], batch_size: int = 32) -> np.ndarray:
        all_embeddings = []
        for i in range(0, len(texts), batch_size):
            batch_texts = texts[i:i + batch_size]
            batch_embeddings = self._encode_batch_with_attention(batch_texts)
            all_embeddings.append(batch_embeddings)
        return np.vstack(all_embeddings)
    
    def _encode_batch_with_attention(self, texts: List[str]) -> np.ndarray:
        encoded = self.tokenizer(texts, padding=True, truncation=True, max_length=512, return_tensors='pt')
        
        with torch.no_grad():
            model_output = self.model[0].auto_model(**encoded)
            token_embeddings = model_output.last_hidden_state
            attention_mask = encoded['attention_mask']
            
            mean_activation = token_embeddings.mean(dim=-1)
            masked_activation = mean_activation * attention_mask.float() + (1 - attention_mask.float()) * -1e9
            attention_weights = torch.nn.functional.softmax(masked_activation, dim=-1)
            pooled = torch.bmm(attention_weights.unsqueeze(1), token_embeddings).squeeze(1)
        
        return pooled.numpy()


class ARISE:
    
    def __init__(self, embedding_model: str = "all-mpnet-base-v2", 
                 alpha_range: Optional[List[float]] = None):
        self.embedding_model = embedding_model
        self.alpha_range = alpha_range or [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
        self._encoder = None
    
    @property
    def encoder(self) -> AttentionPoolingEncoder:
        if self._encoder is None:
            self._encoder = AttentionPoolingEncoder(self.embedding_model)
        return self._encoder
    
    def fit_predict(self, features: np.ndarray, feature_names: List[str],
                    descriptions: Dict[str, str], n_clusters: int,
                    n_runs: int = 10, random_state: int = 42) -> Tuple[np.ndarray, float]:
        onehot_features = self._encode_onehot(features)
        semantic_embeddings = self._generate_semantic_embeddings(features, feature_names, descriptions)
        fused_features, best_alpha = self._adaptive_fusion(onehot_features, semantic_embeddings, n_clusters)
        
        kmeans = KMeans(n_clusters=n_clusters, random_state=random_state, n_init=10)
        cluster_labels = kmeans.fit_predict(fused_features)
        
        return cluster_labels, best_alpha
    
    def _encode_onehot(self, features: np.ndarray) -> np.ndarray:
        features_encoded = np.zeros_like(features, dtype=int)
        for col in range(features.shape[1]):
            le = LabelEncoder()
            features_encoded[:, col] = le.fit_transform(features[:, col].astype(str))
        encoder = OneHotEncoder(sparse_output=False, handle_unknown='ignore')
        return encoder.fit_transform(features_encoded)
    
    def _generate_semantic_embeddings(self, features: np.ndarray, feature_names: List[str],
                                       descriptions: Dict[str, str]) -> np.ndarray:
        all_keys = list(descriptions.keys())
        all_descriptions = [descriptions[k] for k in all_keys]
        all_embeddings = self.encoder.encode(all_descriptions)
        
        embedding_dim = all_embeddings.shape[1]
        value_embeddings = {k: all_embeddings[i] for i, k in enumerate(all_keys)}
        
        n_samples, n_features = features.shape
        sample_embeddings = np.zeros((n_samples, n_features * embedding_dim))
        
        for i in range(n_samples):
            for j, (fname, val) in enumerate(zip(feature_names, features[i])):
                key = f"{fname}_{val}"
                emb = value_embeddings.get(key, np.zeros(embedding_dim))
                sample_embeddings[i, j*embedding_dim:(j+1)*embedding_dim] = emb
        
        return sample_embeddings
    
    def _adaptive_fusion(self, onehot_features: np.ndarray, semantic_embeddings: np.ndarray,
                         n_clusters: int) -> Tuple[np.ndarray, float]:
        oh_norm = StandardScaler().fit_transform(onehot_features)
        sem_norm = StandardScaler().fit_transform(semantic_embeddings)
        
        best_alpha, best_score = 0.7, -1
        
        for alpha in self.alpha_range:
            fused = np.concatenate([(1 - alpha) * oh_norm, alpha * sem_norm], axis=1)
            if n_clusters > 1:
                labels_pred = KMeans(n_clusters=n_clusters, random_state=42, n_init=10).fit_predict(fused)
                if len(np.unique(labels_pred)) > 1:
                    score = silhouette_score(fused, labels_pred)
                    if score > best_score:
                        best_score, best_alpha = score, alpha
        
        best_features = np.concatenate([(1 - best_alpha) * oh_norm, best_alpha * sem_norm], axis=1)
        return best_features, best_alpha


def clustering_accuracy(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    y_true, y_pred = np.array(y_true), np.array(y_pred)
    n_clusters = max(len(np.unique(y_true)), len(np.unique(y_pred)))
    cost_matrix = np.zeros((n_clusters, n_clusters))
    for i in range(n_clusters):
        for j in range(n_clusters):
            cost_matrix[i, j] = -np.sum((y_true == i) & (y_pred == j))
    row_ind, col_ind = linear_sum_assignment(cost_matrix)
    return -cost_matrix[row_ind, col_ind].sum() / len(y_true)


def evaluate_clustering(features: np.ndarray, true_labels: np.ndarray, 
                        n_clusters: int, n_runs: int = 10) -> Dict[str, float]:
    ari_scores, nmi_scores, acc_scores = [], [], []
    for run in range(n_runs):
        pred_labels = KMeans(n_clusters=n_clusters, random_state=run, n_init=10).fit_predict(features)
        ari_scores.append(adjusted_rand_score(true_labels, pred_labels))
        nmi_scores.append(normalized_mutual_info_score(true_labels, pred_labels))
        acc_scores.append(clustering_accuracy(true_labels, pred_labels))
    return {
        'ARI_mean': np.mean(ari_scores), 'ARI_std': np.std(ari_scores),
        'NMI_mean': np.mean(nmi_scores), 'NMI_std': np.std(nmi_scores),
        'ACC_mean': np.mean(acc_scores), 'ACC_std': np.std(acc_scores)
    }


# ============================================================================
# Dataset Loader
# ============================================================================

ZOO_FEATURE_NAMES = [
    'hair', 'feathers', 'eggs', 'milk', 'airborne', 'aquatic', 'predator', 
    'toothed', 'backbone', 'breathes', 'venomous', 'fins', 'legs', 'tail', 
    'domestic', 'catsize'
]

def load_zoo_dataset(data_path: str = "./datasets/zoo/zoo.data"):
    data = np.genfromtxt(data_path, delimiter=',', dtype=str)
    features = data[:, 1:-1]
    labels = data[:, -1].astype(int) - 1
    return features, labels, ZOO_FEATURE_NAMES

def load_descriptions(json_path: str) -> Dict[str, str]:
    with open(json_path, 'r', encoding='utf-8') as f:
        return json.load(f)


if __name__ == "__main__":
    print("=" * 60)
    print("ARISE: Zoo Dataset Example")
    print("=" * 60)
    
    features, true_labels, feature_names = load_zoo_dataset("./datasets/zoo/zoo.data")
    descriptions = load_descriptions("./examples/gpt_Zoo.json")
    n_clusters = len(np.unique(true_labels))
    
    print(f"Samples: {len(features)}, Features: {len(feature_names)}, Clusters: {n_clusters}")
    
    arise = ARISE()
    cluster_labels, best_alpha = arise.fit_predict(
        features=features,
        feature_names=feature_names,
        descriptions=descriptions,
        n_clusters=n_clusters
    )
    
    print(f"\nResults:")
    print(f"  Best α: {best_alpha}")
    print(f"  ARI: {adjusted_rand_score(true_labels, cluster_labels):.4f}")
    print(f"  NMI: {normalized_mutual_info_score(true_labels, cluster_labels):.4f}")
    print(f"  ACC: {clustering_accuracy(true_labels, cluster_labels):.4f}")
