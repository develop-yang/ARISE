# Mushroom Dataset - LLM Description Generation Prompt

## Dataset Information
- **Name**: Mushroom (Agaricus-Lepiota)
- **Samples**: 8,124
- **Features**: 22 (all categorical)
- **Classes**: 2 (edible/poisonous)
- **Unique Values**: 126
- **Domain**: Mycology / Mushroom Classification

## Prompt

```
You are an expert mycologist specializing in mushroom identification and classification. Generate comprehensive descriptions for categorical feature values used in mushroom edibility classification.

For EACH feature-value pair below, generate a description following this EXACT format:

[CORE] 2-3 sentences: Definition and explanation of what this morphological feature value represents in mycology.
[INDICATOR] 2-3 sentences: What this characteristic indicates about mushroom identification and potential edibility.
[PATTERN] 2-3 sentences: Typical patterns or species where this value commonly occurs.
[DISTINCTION] 2-3 sentences: How this value differs from other possible values for the same feature.

IMPORTANT:
- Use CONCRETE, STRAIGHTFORWARD descriptions
- NO abbreviations or acronyms
- NO obscure jargon - descriptions should be understandable to amateur foragers
- Give specific mushroom examples where helpful

Here are ALL the feature-value pairs that need descriptions:

FEATURE: cap-shape (shape of the mushroom cap)
- Value b: bell-shaped cap
- Value c: conical cap
- Value x: convex cap
- Value f: flat cap
- Value k: knobbed cap (with a central bump)
- Value s: sunken cap (depressed in center)

FEATURE: cap-surface (texture of the cap surface)
- Value f: fibrous surface
- Value g: grooved surface
- Value y: scaly surface
- Value s: smooth surface

FEATURE: cap-color (color of the cap)
- Value n: brown cap
- Value b: buff cap (pale yellowish-brown)
- Value c: cinnamon cap
- Value g: gray cap
- Value r: green cap
- Value p: pink cap
- Value u: purple cap
- Value e: red cap
- Value w: white cap
- Value y: yellow cap

FEATURE: bruises (whether the mushroom bruises when damaged)
- Value t: bruises present (changes color when damaged)
- Value f: no bruising

FEATURE: odor (smell of the mushroom)
- Value a: almond odor
- Value l: anise odor (licorice-like)
- Value c: creosote odor (chemical/tar-like)
- Value y: fishy odor
- Value f: foul odor
- Value m: musty odor
- Value n: no odor (odorless)
- Value p: pungent odor (sharp/acrid)
- Value s: spicy odor

FEATURE: gill-attachment (how gills attach to the stalk)
- Value a: attached gills
- Value d: descending gills (running down the stalk)
- Value f: free gills (not touching the stalk)
- Value n: notched gills

FEATURE: gill-spacing (distance between gills)
- Value c: close gill spacing
- Value w: crowded gill spacing
- Value d: distant gill spacing

FEATURE: gill-size (width of the gills)
- Value b: broad gills
- Value n: narrow gills

FEATURE: gill-color (color of the gills)
- Value k: black gills
- Value n: brown gills
- Value b: buff gills
- Value h: chocolate gills
- Value g: gray gills
- Value r: green gills
- Value o: orange gills
- Value p: pink gills
- Value u: purple gills
- Value e: red gills
- Value w: white gills
- Value y: yellow gills

FEATURE: stalk-shape (shape of the stalk)
- Value e: enlarging stalk (wider at base)
- Value t: tapering stalk (narrower at base)

FEATURE: stalk-root (type of stalk base/root)
- Value b: bulbous root
- Value c: club-shaped root
- Value u: cup-shaped root
- Value e: equal root (no enlargement)
- Value z: rhizomorphs present (root-like strands)
- Value r: rooted (taproot-like)
- Value ?: missing or unknown root type

FEATURE: stalk-surface-above-ring (texture of stalk above the ring)
- Value f: fibrous surface above ring
- Value y: scaly surface above ring
- Value k: silky surface above ring
- Value s: smooth surface above ring

FEATURE: stalk-surface-below-ring (texture of stalk below the ring)
- Value f: fibrous surface below ring
- Value y: scaly surface below ring
- Value k: silky surface below ring
- Value s: smooth surface below ring

FEATURE: stalk-color-above-ring (color of stalk above the ring)
- Value n: brown stalk above ring
- Value b: buff stalk above ring
- Value c: cinnamon stalk above ring
- Value g: gray stalk above ring
- Value o: orange stalk above ring
- Value p: pink stalk above ring
- Value e: red stalk above ring
- Value w: white stalk above ring
- Value y: yellow stalk above ring

FEATURE: stalk-color-below-ring (color of stalk below the ring)
- Value n: brown stalk below ring
- Value b: buff stalk below ring
- Value c: cinnamon stalk below ring
- Value g: gray stalk below ring
- Value o: orange stalk below ring
- Value p: pink stalk below ring
- Value e: red stalk below ring
- Value w: white stalk below ring
- Value y: yellow stalk below ring

FEATURE: veil-type (type of veil covering the gills)
- Value p: partial veil
- Value u: universal veil

FEATURE: veil-color (color of the veil)
- Value n: brown veil
- Value o: orange veil
- Value w: white veil
- Value y: yellow veil

FEATURE: ring-number (number of rings on the stalk)
- Value n: no ring
- Value o: one ring
- Value t: two rings

FEATURE: ring-type (type/appearance of the ring)
- Value c: cobwebby ring
- Value e: evanescent ring (disappearing/fragile)
- Value f: flaring ring (spreading outward)
- Value l: large ring
- Value n: no ring present
- Value p: pendant ring (hanging down)
- Value s: sheathing ring (like a sleeve)
- Value z: zone-like ring (marked zone rather than distinct ring)

FEATURE: spore-print-color (color of spore print)
- Value k: black spore print
- Value n: brown spore print
- Value b: buff spore print
- Value h: chocolate spore print
- Value r: green spore print
- Value o: orange spore print
- Value u: purple spore print
- Value w: white spore print
- Value y: yellow spore print

FEATURE: population (how mushrooms grow in groups)
- Value a: abundant population
- Value c: clustered population
- Value n: numerous population
- Value s: scattered population
- Value v: several (small group)
- Value y: solitary (growing alone)

FEATURE: habitat (where the mushroom grows)
- Value g: grasses habitat
- Value l: leaves habitat (leaf litter)
- Value m: meadows habitat
- Value p: paths habitat
- Value u: urban habitat
- Value w: waste areas habitat
- Value d: woods habitat (forest)

OUTPUT FORMAT: Return a JSON object where each key is "feature_value" (e.g., "cap-shape_b", "odor_a") and the value is the complete description string.

{
  "cap-shape_b": "[CORE] ... [INDICATOR] ... [PATTERN] ... [DISTINCTION] ...",
  "cap-shape_c": "[CORE] ... [INDICATOR] ... [PATTERN] ... [DISTINCTION] ...",
  ...
}

Generate descriptions for ALL 126 feature-value pairs listed above.
```
