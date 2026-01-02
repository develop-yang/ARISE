# Lymphography Dataset - LLM Description Generation Prompt

## Dataset Information
- **Name**: Lymphography
- **Samples**: 148
- **Features**: 18 (all categorical)
- **Classes**: 4
- **Unique Values**: 59
- **Domain**: Medical Imaging / Lymphatic System Pathology

## Prompt

```
You are an expert in medical imaging and lymphatic system pathology. Generate comprehensive descriptions for categorical feature values used in lymphography diagnosis.

For EACH feature-value pair below, generate a description following this EXACT format:

[CORE] 2-3 sentences: Definition and explanation of what this value represents in lymphography.
[INDICATOR] 2-3 sentences: What diagnostic characteristics this value indicates.
[PATTERN] 2-3 sentences: Typical patterns or conditions where this value occurs.
[DISTINCTION] 2-3 sentences: How this value differs from other possible values.

IMPORTANT:
- Use CONCRETE, STRAIGHTFORWARD descriptions
- NO abbreviations or acronyms
- NO obscure jargon - descriptions must be clear
- Describe what is actually observed in the imaging

Here are ALL the feature-value pairs that need descriptions:

FEATURE: lymphatics (lymphatic vessel appearance)
- Value 1: normal lymphatics
- Value 2: arched lymphatics
- Value 3: deformed lymphatics
- Value 4: displaced lymphatics

FEATURE: block-of-affere (blockage of afferent lymphatics)
- Value 1: no blockage
- Value 2: blockage present

FEATURE: bl-of-lymph-c (blockage of lymph node cortex)
- Value 1: no blockage
- Value 2: blockage present

FEATURE: bl-of-lymph-s (blockage of lymph node sinus)
- Value 1: no blockage
- Value 2: blockage present

FEATURE: by-pass (lymphatic bypass)
- Value 1: no bypass
- Value 2: bypass present

FEATURE: extravasates (lymphatic extravasation)
- Value 1: no extravasation
- Value 2: extravasation present

FEATURE: regeneration-of (regeneration of lymphatics)
- Value 1: no regeneration
- Value 2: regeneration present

FEATURE: early-uptake-in (early uptake in lymph nodes)
- Value 1: no early uptake
- Value 2: early uptake present

FEATURE: lym-nodes-dimin (diminished lymph nodes)
- Value 1: no diminution
- Value 2: diminution present
- Value 3: severely diminished

FEATURE: lym-nodes-enlar (enlarged lymph nodes)
- Value 1: no enlargement
- Value 2: enlargement present
- Value 3: severely enlarged
- Value 4: extremely enlarged

FEATURE: changes-in-lym (changes in lymph node appearance)
- Value 1: bean-shaped (normal)
- Value 2: oval-shaped
- Value 3: round-shaped

FEATURE: defect-in-node (defect in lymph node filling)
- Value 1: no defect
- Value 2: lacunar defect
- Value 3: lacunar marginal defect
- Value 4: lacunar central defect

FEATURE: changes-in-node (changes in lymph node structure)
- Value 1: no changes
- Value 2: lacunar changes
- Value 3: lacunar marginal changes
- Value 4: lacunar central changes

FEATURE: changes-in-stru (changes in overall structure)
- Value 1: no structural changes
- Value 2: grainy structure
- Value 3: drop-like structure
- Value 4: coarse structure
- Value 5: diluted structure
- Value 6: reticular structure
- Value 7: stripped structure
- Value 8: faint structure

FEATURE: special-forms (special morphological forms)
- Value 1: no special forms
- Value 2: chalices form
- Value 3: vesicles form

FEATURE: dislocation-of (dislocation of lymph nodes)
- Value 1: no dislocation
- Value 2: dislocation present

FEATURE: exclusion-of-no (exclusion of lymph nodes from contrast)
- Value 1: no exclusion
- Value 2: exclusion present

FEATURE: no-of-nodes-in (number of nodes involved)
- Value 1: 0-9 nodes
- Value 2: 10-19 nodes
- Value 3: 20-29 nodes
- Value 4: 30-39 nodes
- Value 5: 40-49 nodes
- Value 6: 50-59 nodes
- Value 7: 60-69 nodes
- Value 8: 70 or more nodes

OUTPUT FORMAT: Return a JSON object:

{
  "lymphatics_1": "[CORE] ... [INDICATOR] ... [PATTERN] ... [DISTINCTION] ...",
  ...
}

Generate descriptions for ALL 58 feature-value pairs listed above.
```
