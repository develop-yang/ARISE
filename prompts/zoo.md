# Zoo Dataset - LLM Description Generation Prompt

## Dataset Information
- **Name**: Zoo
- **Samples**: 101
- **Features**: 16 (all categorical)
- **Classes**: 7
- **Unique Values**: 36
- **Domain**: Zoology / Animal Classification

## Prompt

```
You are an expert in zoology and animal classification. Generate a comprehensive description for a categorical feature value.

For EACH feature-value pair below, generate a description following this EXACT format:

[CORE] 2-3 sentences: Definition and explanation of what this value represents in zoology.
[INDICATOR] 2-3 sentences: What characteristics or behaviors this value indicates.
[PATTERN] 2-3 sentences: Typical patterns or contexts where this value occurs.
[DISTINCTION] 2-3 sentences: How this value differs from other possible values.

IMPORTANT:
- Use CONCRETE, STRAIGHTFORWARD descriptions
- NO abbreviations or acronyms
- NO obscure jargon - descriptions must be clear and understandable
- Give specific examples (animal names) where helpful

Here are ALL the feature-value pairs that need descriptions:

FEATURE: hair
- Value 0: does not have hair
- Value 1: has hair

FEATURE: feathers
- Value 0: does not have feathers
- Value 1: has feathers

FEATURE: eggs
- Value 0: does not lay eggs
- Value 1: lays eggs

FEATURE: milk
- Value 0: does not produce milk
- Value 1: produces milk

FEATURE: airborne
- Value 0: not airborne (cannot fly)
- Value 1: airborne (can fly)

FEATURE: aquatic
- Value 0: not aquatic
- Value 1: aquatic (lives in water)

FEATURE: predator
- Value 0: not a predator
- Value 1: is a predator

FEATURE: toothed
- Value 0: does not have teeth
- Value 1: has teeth

FEATURE: backbone
- Value 0: does not have backbone (invertebrate)
- Value 1: has backbone (vertebrate)

FEATURE: breathes
- Value 0: does not breathe air
- Value 1: breathes air

FEATURE: venomous
- Value 0: not venomous
- Value 1: venomous

FEATURE: fins
- Value 0: does not have fins
- Value 1: has fins

FEATURE: legs
- Value 0: has 0 legs
- Value 2: has 2 legs
- Value 4: has 4 legs
- Value 5: has 5 legs
- Value 6: has 6 legs
- Value 8: has 8 legs

FEATURE: tail
- Value 0: does not have tail
- Value 1: has tail

FEATURE: domestic
- Value 0: not domestic (wild animal)
- Value 1: domestic animal

FEATURE: catsize
- Value 0: not cat-sized (smaller or larger)
- Value 1: cat-sized

OUTPUT FORMAT: Return a JSON object where each key is "feature_value" (e.g., "hair_0", "hair_1") and the value is the complete description string.

{
  "hair_0": "[CORE] ... [INDICATOR] ... [PATTERN] ... [DISTINCTION] ...",
  "hair_1": "[CORE] ... [INDICATOR] ... [PATTERN] ... [DISTINCTION] ...",
  ...
}

Generate descriptions for ALL 36 feature-value pairs listed above.
```
