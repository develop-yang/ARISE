# Soybean Dataset - LLM Description Generation Prompt

## Dataset Information
- **Name**: Soybean (Small)
- **Samples**: 307
- **Features**: 35 (all categorical)
- **Classes**: 19
- **Unique Values**: 133
- **Domain**: Agricultural Plant Pathology / Soybean Disease Diagnosis

## Prompt

```
You are an expert in agricultural plant pathology and soybean disease diagnosis. Generate comprehensive descriptions for categorical feature values used in soybean disease classification.

For EACH feature-value pair below, generate a description following this EXACT format:

[CORE] 2-3 sentences: Definition and explanation of what this value represents in plant pathology.
[INDICATOR] 2-3 sentences: What disease characteristics this value indicates.
[PATTERN] 2-3 sentences: Typical patterns or conditions where this value occurs.
[DISTINCTION] 2-3 sentences: How this value differs from other possible values.

IMPORTANT:
- Use CONCRETE, STRAIGHTFORWARD descriptions
- NO abbreviations or acronyms
- NO obscure jargon - a farmer should be able to understand
- Give specific examples where helpful

Here are ALL the feature-value pairs that need descriptions:

FEATURE: date (planting date)
- Value 0: April
- Value 1: May
- Value 2: June
- Value 3: July
- Value 4: August
- Value 5: September
- Value 6: October

FEATURE: plant-stand (density of plants)
- Value 0: normal plant stand
- Value 1: low plant stand

FEATURE: precip (precipitation level)
- Value 0: less than normal precipitation
- Value 1: normal precipitation
- Value 2: greater than normal precipitation

FEATURE: temp (temperature)
- Value 0: less than normal temperature
- Value 1: normal temperature
- Value 2: greater than normal temperature

FEATURE: hail (hail damage)
- Value 0: no hail damage
- Value 1: hail damage present

FEATURE: crop-hist (crop history)
- Value 0: different disease last year
- Value 1: same disease last year
- Value 2: disease-free rotation
- Value 3: continuous soybean cropping

FEATURE: area-damaged (extent of damage)
- Value 0: scattered damage
- Value 1: low areas affected
- Value 2: upper areas affected
- Value 3: whole field affected

FEATURE: severity (disease severity)
- Value 0: minor severity
- Value 1: potentially severe
- Value 2: severe

FEATURE: seed-tmt (seed treatment)
- Value 0: no seed treatment
- Value 1: fungicide seed treatment
- Value 2: other seed treatment

FEATURE: germination (germination rate)
- Value 0: 90-100% germination
- Value 1: 80-89% germination
- Value 2: less than 80% germination

FEATURE: plant-growth (plant growth status)
- Value 0: normal growth
- Value 1: abnormal growth

FEATURE: leaves (leaf condition)
- Value 0: normal leaves
- Value 1: abnormal leaves

FEATURE: leafspots-halo (leaf spot halo)
- Value 0: absent halo
- Value 1: yellow halo
- Value 2: no yellow halo

FEATURE: leafspots-marg (leaf spot margin)
- Value 0: well-defined margin
- Value 1: frog-eye margin
- Value 2: diffuse margin

FEATURE: leafspot-size (leaf spot size)
- Value 0: less than 1/8 inch
- Value 1: greater than 1/8 inch
- Value 2: diffuse spots

FEATURE: leaf-shread (leaf shredding)
- Value 0: absent shredding
- Value 1: present shredding

FEATURE: leaf-malf (leaf malformation)
- Value 0: absent malformation
- Value 1: present malformation

FEATURE: leaf-mild (leaf mildew)
- Value 0: absent mildew
- Value 1: upper surface mildew
- Value 2: lower surface mildew

FEATURE: stem (stem condition)
- Value 0: normal stem
- Value 1: abnormal stem

FEATURE: lodging (plant lodging)
- Value 0: no lodging
- Value 1: lodging present

FEATURE: stem-cankers (stem cankers)
- Value 0: absent cankers
- Value 1: below soil line
- Value 2: above soil line
- Value 3: above second node

FEATURE: canker-lesion (canker lesion color)
- Value 0: diffuse lesion
- Value 1: dark brown lesion
- Value 2: brown lesion
- Value 3: tan lesion

FEATURE: fruiting-bodies (fruiting bodies presence)
- Value 0: absent fruiting bodies
- Value 1: present fruiting bodies

FEATURE: external-decay (external decay)
- Value 0: absent decay
- Value 1: firm and dry decay
- Value 2: watery decay

FEATURE: mycelium (mycelium presence)
- Value 0: absent mycelium
- Value 1: present mycelium

FEATURE: int-discolor (internal discoloration)
- Value 0: no internal discoloration
- Value 1: brown internal discoloration
- Value 2: black internal discoloration

FEATURE: sclerotia (sclerotia presence)
- Value 0: absent sclerotia
- Value 1: present sclerotia

FEATURE: fruit-pods (fruit pod condition)
- Value 0: normal pods
- Value 1: diseased pods
- Value 2: few present
- Value 3: diffuse damage

FEATURE: fruit-spots (fruit spots)
- Value 0: absent spots
- Value 1: colored spots
- Value 2: brown spots with black specks
- Value 3: distorted spots
- Value 4: diffuse spots

FEATURE: seed (seed condition)
- Value 0: normal seed
- Value 1: abnormal seed

FEATURE: mold-growth (mold growth)
- Value 0: absent mold
- Value 1: present mold

FEATURE: seed-discolor (seed discoloration)
- Value 0: absent discoloration
- Value 1: present discoloration

FEATURE: seed-size (seed size)
- Value 0: normal size
- Value 1: less than normal size

FEATURE: shriveling (seed shriveling)
- Value 0: absent shriveling
- Value 1: present shriveling

FEATURE: roots (root condition)
- Value 0: normal roots
- Value 1: rotted roots
- Value 2: galls on roots

OUTPUT FORMAT: Return a JSON object where each key is "feature_value" (e.g., "date_0", "precip_1"):

{
  "date_0": "[CORE] ... [INDICATOR] ... [PATTERN] ... [DISTINCTION] ...",
  ...
}

Generate descriptions for ALL feature-value pairs listed above.
```
