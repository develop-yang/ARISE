# Solar Flare Dataset - LLM Description Generation Prompt

## Dataset Information
- **Name**: Solar Flare
- **Samples**: 1,066
- **Features**: 10 (all categorical)
- **Classes**: 6
- **Unique Values**: 31
- **Domain**: Solar Physics / Space Weather Prediction

## Prompt

```
You are an expert in solar physics and space weather prediction. Generate comprehensive descriptions for categorical feature values used in solar flare forecasting.

For EACH feature-value pair below, generate a description following this EXACT format:

[CORE] 2-3 sentences: Definition and explanation of what this value represents in solar physics.
[INDICATOR] 2-3 sentences: What solar activity characteristics this value indicates.
[PATTERN] 2-3 sentences: Typical patterns or conditions where this value occurs.
[DISTINCTION] 2-3 sentences: How this value differs from other possible values.

IMPORTANT:
- Use CONCRETE, STRAIGHTFORWARD descriptions
- NO abbreviations or acronyms
- NO obscure jargon
- Describe observable characteristics clearly

Here are ALL the feature-value pairs that need descriptions:

FEATURE: zurich-class (modified Zurich classification of sunspot group)
- Value A: small single unipolar sunspot
- Value B: bipolar sunspot group with no penumbra
- Value C: bipolar group with penumbra on one end
- Value D: bipolar group with penumbra on both ends (length < 10 degrees)
- Value E: bipolar group with penumbra on both ends (length 10-15 degrees)
- Value F: bipolar group with penumbra on both ends (length > 15 degrees)
- Value H: unipolar sunspot with penumbra

FEATURE: spot-size (size of largest spot in the sunspot group)
- Value X: undefined or minimal area
- Value R: small area
- Value S: moderate area
- Value A: large area
- Value H: huge area
- Value K: extreme area

FEATURE: spot-distribution (distribution pattern of spots within the group)
- Value X: undefined distribution pattern
- Value O: open distribution - spots spread apart
- Value I: intermediate distribution
- Value C: compact distribution - spots closely packed

FEATURE: activity (current activity level of the active region)
- Value 1: reduced activity level
- Value 2: unchanged activity level

FEATURE: evolution (evolutionary phase of the sunspot group)
- Value 1: decay phase - group is shrinking/fading
- Value 2: no growth - stable
- Value 3: growth phase - group is actively developing

FEATURE: prev-24h-activity (flare activity in the previous 24 hours)
- Value 1: minimal activity
- Value 2: moderate activity - one M1-class flare occurred
- Value 3: high activity - more than one M1-class flare

FEATURE: historically-complex (whether the region has been historically complex)
- Value 1: region has been historically complex
- Value 2: region has not been historically complex

FEATURE: became-complex (whether the region became magnetically complex)
- Value 1: region did not become complex
- Value 2: region became complex during observation

FEATURE: area (overall area classification of the sunspot group)
- Value 1: small total area
- Value 2: large total area

FEATURE: area-largest-spot (area classification of the largest individual spot)
- Value 1: small largest spot
- Value 2: large largest spot

OUTPUT FORMAT: Return a JSON object with EXACTLY these feature names in the keys:

{
  "zurich-class_A": "[CORE] ... [INDICATOR] ... [PATTERN] ... [DISTINCTION] ...",
  "spot-size_X": "[CORE] ... [INDICATOR] ... [PATTERN] ... [DISTINCTION] ...",
  ...
}

IMPORTANT: Use EXACTLY these feature names:
- zurich-class
- spot-size  
- spot-distribution
- activity
- evolution
- prev-24h-activity
- historically-complex
- became-complex
- area
- area-largest-spot

Generate descriptions for ALL 33 feature-value pairs listed above.
```
