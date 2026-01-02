# Breast Cancer Dataset - LLM Description Generation Prompt

## Dataset Information
- **Name**: Breast Cancer (Wisconsin)
- **Samples**: 286
- **Features**: 9 (all categorical)
- **Classes**: 2 (recurrence / no-recurrence)
- **Unique Values**: 51
- **Domain**: Oncology / Breast Cancer Prognosis

## Prompt

```
You are an expert in oncology and breast cancer prognosis. Generate comprehensive descriptions for categorical feature values used in breast cancer recurrence prediction.

For EACH feature-value pair below, generate a description following this EXACT format:

[CORE] 2-3 sentences: Definition and explanation of what this value represents in oncology.
[INDICATOR] 2-3 sentences: What prognostic characteristics this value indicates.
[PATTERN] 2-3 sentences: Typical patterns or conditions where this value occurs.
[DISTINCTION] 2-3 sentences: How this value differs from other possible values.

IMPORTANT:
- Use CONCRETE, STRAIGHTFORWARD descriptions
- NO abbreviations or acronyms (write "estrogen receptor" not "ER")
- NO obscure jargon
- Use specific numbers and ranges where applicable

Here are ALL the feature-value pairs that need descriptions:

FEATURE: age (patient age group)
- Value 10-19: age 10-19 years
- Value 20-29: age 20-29 years
- Value 30-39: age 30-39 years
- Value 40-49: age 40-49 years
- Value 50-59: age 50-59 years
- Value 60-69: age 60-69 years
- Value 70-79: age 70-79 years
- Value 80-89: age 80-89 years
- Value 90-99: age 90-99 years

FEATURE: menopause (menopause status)
- Value lt40: premature menopause (before age 40)
- Value ge40: menopause at age 40 or later
- Value premeno: premenopausal

FEATURE: tumor-size (tumor size in mm)
- Value 0-4: tumor size 0-4mm
- Value 5-9: tumor size 5-9mm
- Value 10-14: tumor size 10-14mm
- Value 15-19: tumor size 15-19mm
- Value 20-24: tumor size 20-24mm
- Value 25-29: tumor size 25-29mm
- Value 30-34: tumor size 30-34mm
- Value 35-39: tumor size 35-39mm
- Value 40-44: tumor size 40-44mm
- Value 45-49: tumor size 45-49mm
- Value 50-54: tumor size 50-54mm

FEATURE: inv-nodes (number of axillary lymph nodes with metastasis)
- Value 0-2: 0-2 involved nodes
- Value 3-5: 3-5 involved nodes
- Value 6-8: 6-8 involved nodes
- Value 9-11: 9-11 involved nodes
- Value 12-14: 12-14 involved nodes
- Value 15-17: 15-17 involved nodes
- Value 24-26: 24-26 involved nodes

FEATURE: node-caps (penetration of tumor through lymph node capsule)
- Value yes: node capsule penetration present
- Value no: no node capsule penetration

FEATURE: deg-malig (degree of malignancy / histological grade)
- Value 1: grade 1 (low malignancy)
- Value 2: grade 2 (intermediate malignancy)
- Value 3: grade 3 (high malignancy)

FEATURE: breast (affected breast)
- Value left: left breast
- Value right: right breast

FEATURE: breast-quad (breast quadrant location)
- Value left_up: left upper quadrant
- Value left_low: left lower quadrant
- Value right_up: right upper quadrant
- Value right_low: right lower quadrant
- Value central: central region

FEATURE: irradiat (radiation therapy received)
- Value yes: received radiation therapy
- Value no: no radiation therapy

OUTPUT FORMAT: Return a JSON object:

{
  "age_30-39": "[CORE] ... [INDICATOR] ... [PATTERN] ... [DISTINCTION] ...",
  ...
}

Generate descriptions for ALL feature-value pairs listed above.
```
