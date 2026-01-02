# Dermatology Dataset - LLM Description Generation Prompt

## Dataset Information
- **Name**: Dermatology
- **Samples**: 366
- **Features**: 34 (33 clinical/histopathological features + 1 age)
- **Classes**: 6 (erythemato-squamous skin diseases)
  1. psoriasis
  2. seborrheic dermatitis
  3. lichen planus
  4. pityriasis rosea
  5. chronic dermatitis
  6. pityriasis rubra pilaris
- **Feature Values**: 0-3 (representing symptom severity: 0=absent, 1=mild, 2=moderate, 3=severe)
- **Unique Values**: 133
- **Domain**: Dermatology / Clinical Diagnosis

## Prompt

```
You are an expert dermatologist specializing in differential diagnosis of erythemato-squamous skin diseases. Generate comprehensive descriptions for categorical feature values used in dermatological disease classification.

For EACH feature-value pair below, generate a description following this EXACT format:

[CORE] 2-3 sentences: Definition and explanation of what this clinical/histopathological finding represents in dermatology.
[INDICATOR] 2-3 sentences: What this finding indicates about potential skin disease diagnosis.
[PATTERN] 2-3 sentences: Typical patterns or diseases where this value commonly occurs.
[DISTINCTION] 2-3 sentences: How this value differs from other severity levels for the same feature.

IMPORTANT:
- Use CONCRETE, STRAIGHTFORWARD descriptions
- NO abbreviations or acronyms
- NO obscure jargon - descriptions should be understandable to medical students
- Give specific disease examples where helpful

Here are ALL the feature-value pairs that need descriptions:

FEATURE: erythema (skin redness due to increased blood flow)
- Value 0: no erythema present
- Value 1: mild erythema
- Value 2: moderate erythema
- Value 3: severe erythema

FEATURE: scaling (flaky skin shedding)
- Value 0: no scaling present
- Value 1: mild scaling
- Value 2: moderate scaling
- Value 3: severe scaling

FEATURE: definite-borders (clarity of lesion boundaries)
- Value 0: borders not definite/unclear
- Value 1: slightly definite borders
- Value 2: moderately definite borders
- Value 3: very definite/sharp borders

FEATURE: itching (pruritus sensation)
- Value 0: no itching
- Value 1: mild itching
- Value 2: moderate itching
- Value 3: severe itching

FEATURE: koebner-phenomenon (new lesions appearing at sites of skin trauma)
- Value 0: koebner phenomenon absent
- Value 1: mild koebner phenomenon
- Value 2: moderate koebner phenomenon
- Value 3: marked koebner phenomenon

FEATURE: polygonal-papules (flat-topped angular skin elevations)
- Value 0: no polygonal papules
- Value 1: few polygonal papules
- Value 2: moderate polygonal papules
- Value 3: numerous polygonal papules

FEATURE: follicular-papules (papules centered on hair follicles)
- Value 0: no follicular papules
- Value 1: few follicular papules
- Value 2: moderate follicular papules
- Value 3: numerous follicular papules

FEATURE: oral-mucosal-involvement (lesions in mouth lining)
- Value 0: no oral mucosal involvement
- Value 1: mild oral involvement
- Value 2: moderate oral involvement
- Value 3: severe oral involvement

FEATURE: knee-elbow-involvement (lesions on knees and elbows)
- Value 0: no knee/elbow involvement
- Value 1: mild knee/elbow involvement
- Value 2: moderate knee/elbow involvement
- Value 3: severe knee/elbow involvement

FEATURE: scalp-involvement (lesions on the scalp)
- Value 0: no scalp involvement
- Value 1: mild scalp involvement
- Value 2: moderate scalp involvement
- Value 3: severe scalp involvement

FEATURE: family-history (genetic predisposition in relatives)
- Value 0: no family history of skin disease
- Value 1: possible family history

FEATURE: melanin-incontinence (pigment leakage into dermis - histological)
- Value 0: no melanin incontinence
- Value 1: mild melanin incontinence
- Value 2: moderate melanin incontinence
- Value 3: marked melanin incontinence

FEATURE: eosinophils-infiltrate (eosinophil cells in skin tissue - histological)
- Value 0: no eosinophils in infiltrate
- Value 1: few eosinophils
- Value 2: moderate to many eosinophils

FEATURE: PNL-infiltrate (polymorphonuclear leukocytes in tissue - histological)
- Value 0: no polymorphonuclear leukocyte infiltrate
- Value 1: mild infiltrate
- Value 2: moderate infiltrate
- Value 3: heavy infiltrate

FEATURE: fibrosis-papillary-dermis (scarring in upper dermis layer - histological)
- Value 0: no fibrosis of papillary dermis
- Value 1: mild fibrosis
- Value 2: moderate fibrosis
- Value 3: marked fibrosis

FEATURE: exocytosis (inflammatory cells migrating into epidermis - histological)
- Value 0: no exocytosis
- Value 1: mild exocytosis
- Value 2: moderate exocytosis
- Value 3: marked exocytosis

FEATURE: acanthosis (thickening of the prickle cell layer - histological)
- Value 0: no acanthosis
- Value 1: mild acanthosis
- Value 2: moderate acanthosis
- Value 3: marked acanthosis

FEATURE: hyperkeratosis (thickening of the outer skin layer - histological)
- Value 0: no hyperkeratosis
- Value 1: mild hyperkeratosis
- Value 2: moderate hyperkeratosis
- Value 3: marked hyperkeratosis

FEATURE: parakeratosis (retention of nuclei in stratum corneum - histological)
- Value 0: no parakeratosis
- Value 1: mild parakeratosis
- Value 2: moderate parakeratosis
- Value 3: marked parakeratosis

FEATURE: clubbing-rete-ridges (club-shaped downward projections of epidermis - histological)
- Value 0: no clubbing of rete ridges
- Value 1: mild clubbing
- Value 2: moderate clubbing
- Value 3: marked clubbing

FEATURE: elongation-rete-ridges (lengthened epidermal projections - histological)
- Value 0: no elongation of rete ridges
- Value 1: mild elongation
- Value 2: moderate elongation
- Value 3: marked elongation

FEATURE: thinning-suprapapillary-epidermis (thinned epidermis above dermal papillae - histological)
- Value 0: no thinning of suprapapillary epidermis
- Value 1: mild thinning
- Value 2: moderate thinning
- Value 3: marked thinning

FEATURE: spongiform-pustule (sponge-like pus collection in epidermis - histological)
- Value 0: no spongiform pustule
- Value 1: small spongiform pustule
- Value 2: moderate spongiform pustule
- Value 3: large spongiform pustule

FEATURE: munro-microabcess (small neutrophil collections in stratum corneum - histological)
- Value 0: no munro microabcess
- Value 1: few microabcesses
- Value 2: moderate microabcesses
- Value 3: many microabcesses

FEATURE: focal-hypergranulosis (localized thickening of granular layer - histological)
- Value 0: no focal hypergranulosis
- Value 1: mild focal hypergranulosis
- Value 2: moderate focal hypergranulosis
- Value 3: marked focal hypergranulosis

FEATURE: disappearance-granular-layer (loss of the granular cell layer - histological)
- Value 0: granular layer present/normal
- Value 1: slight disappearance
- Value 2: moderate disappearance
- Value 3: complete disappearance

FEATURE: vacuolisation-basal-layer (fluid-filled spaces in basal cells - histological)
- Value 0: no vacuolisation of basal layer
- Value 1: mild vacuolisation
- Value 2: moderate vacuolisation
- Value 3: marked vacuolisation

FEATURE: spongiosis (intercellular edema in epidermis - histological)
- Value 0: no spongiosis
- Value 1: mild spongiosis
- Value 2: moderate spongiosis
- Value 3: marked spongiosis

FEATURE: saw-tooth-rete-ridges (irregular jagged epidermal projections - histological)
- Value 0: no saw-tooth appearance of rete ridges
- Value 1: mild saw-tooth pattern
- Value 2: moderate saw-tooth pattern
- Value 3: marked saw-tooth pattern

FEATURE: follicular-horn-plug (keratin plugs in hair follicle openings - histological)
- Value 0: no follicular horn plug
- Value 1: few horn plugs
- Value 2: moderate horn plugs
- Value 3: many horn plugs

FEATURE: perifollicular-parakeratosis (abnormal keratin around hair follicles - histological)
- Value 0: no perifollicular parakeratosis
- Value 1: mild perifollicular parakeratosis
- Value 2: moderate perifollicular parakeratosis
- Value 3: marked perifollicular parakeratosis

FEATURE: inflammatory-monoluclear-infiltrate (single-nucleus immune cells in tissue - histological)
- Value 0: no inflammatory mononuclear infiltrate
- Value 1: mild infiltrate
- Value 2: moderate infiltrate
- Value 3: heavy infiltrate

FEATURE: band-like-infiltrate (horizontal band of inflammatory cells - histological)
- Value 0: no band-like infiltrate
- Value 1: mild band-like infiltrate
- Value 2: moderate band-like infiltrate
- Value 3: marked band-like infiltrate

FEATURE: age (patient age group)
- Value 0-20: young patient (child to young adult, 0-20 years)
- Value 21-40: young adult patient (21-40 years)
- Value 41-60: middle-aged patient (41-60 years)
- Value 61+: elderly patient (over 60 years)

OUTPUT FORMAT: Return a JSON object where each key is "feature_value" (e.g., "erythema_0", "scaling_1") and the value is the complete description string.

{
  "erythema_0": "[CORE] ... [INDICATOR] ... [PATTERN] ... [DISTINCTION] ...",
  "erythema_1": "[CORE] ... [INDICATOR] ... [PATTERN] ... [DISTINCTION] ...",
  ...
}

Generate descriptions for ALL 133 feature-value pairs listed above.
```
