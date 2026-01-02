# Car Evaluation Dataset - LLM Description Generation Prompt

## Dataset Information
- **Name**: Car Evaluation
- **Samples**: 1,728
- **Features**: 6 (all categorical)
- **Classes**: 4 (unacceptable, acceptable, good, very good)
- **Unique Values**: 21
- **Domain**: Automotive Engineering / Vehicle Evaluation

## Prompt

```
You are an expert in automotive engineering and vehicle evaluation. Generate comprehensive descriptions for categorical feature values used in car acceptability assessment.

For EACH feature-value pair below, generate a description following this EXACT format:

[CORE] 2-3 sentences: Definition and explanation of what this value represents in vehicle evaluation.
[INDICATOR] 2-3 sentences: What characteristics this value indicates about the vehicle.
[PATTERN] 2-3 sentences: Typical patterns or market contexts where this value occurs.
[DISTINCTION] 2-3 sentences: How this value differs from other possible values.

IMPORTANT:
- Use CONCRETE, STRAIGHTFORWARD descriptions
- NO abbreviations or acronyms (write "Manufacturer's Suggested Retail Price" not "MSRP")
- NO obscure industry jargon
- Use specific examples and price ranges where helpful

Here are ALL the feature-value pairs that need descriptions:

FEATURE: buying (buying price)
- Value vhigh: very high buying price
- Value high: high buying price
- Value med: medium buying price
- Value low: low buying price

FEATURE: maint (maintenance cost)
- Value vhigh: very high maintenance cost
- Value high: high maintenance cost
- Value med: medium maintenance cost
- Value low: low maintenance cost

FEATURE: doors (number of doors)
- Value 2: 2 doors
- Value 3: 3 doors
- Value 4: 4 doors
- Value 5more: 5 or more doors

FEATURE: persons (passenger capacity)
- Value 2: 2 persons capacity
- Value 4: 4 persons capacity
- Value more: more than 4 persons capacity

FEATURE: lug_boot (luggage boot size)
- Value small: small luggage boot
- Value med: medium luggage boot
- Value big: big luggage boot

FEATURE: safety (estimated safety)
- Value low: low safety rating
- Value med: medium safety rating
- Value high: high safety rating

OUTPUT FORMAT: Return a JSON object:

{
  "buying_vhigh": "[CORE] ... [INDICATOR] ... [PATTERN] ... [DISTINCTION] ...",
  ...
}

Generate descriptions for ALL 21 feature-value pairs listed above.
```
