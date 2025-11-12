# Create Digital Recipe Cards

## Source
https://claude.com/resources/use-case/create-digital-recipe-cards

## Template Prompt

Read this {RECIPE_SOURCE|handwritten family recipe,cookbook recipe,recipe card,digital recipe} and turn it into something I can share with {AUDIENCE|family,friends,online community,cookbook}.

Please:
1. **Process the Content**: {TASKS|Decode the handwriting,Clean up unclear formatting,Standardize the text}
2. **Standardize Measurements**: Convert {MEASUREMENT_STYLE|vague measurements,imperial units,metric units,non-standard measures} into {TARGET_MEASUREMENT_STYLE|precise amounts,metric,imperial,both systems}
3. **Clarify Instructions**: Write clear {INSTRUCTION_STYLE|step-by-step,traditional narrative,detailed explanatory} instructions

**Design Requirements:**
- Create an {OUTPUT_FORMAT|interactive HTML,printable PDF,digital card,social media graphic} format
- Include {FEATURES|serving size adjuster,ingredient scaling,cooking timer,nutrition info}
- Display {ORIGINAL_HANDLING|the original recipe in a museum-quality frame,side-by-side comparison,original as reference}
- Add {CONTEXT|cultural context about the dish,family history,origin story,cooking tips}

**Visual Style:**
- Design aesthetic: {AESTHETIC|Vintage family recipe,Modern clean,Rustic handwritten,Professional cookbook}
- Color scheme: {COLORS|Warm and nostalgic,Bright and modern,Neutral and classic,Custom brand colors}
- Typography: {TYPOGRAPHY|Handwritten-style fonts,Classic serif,Modern sans-serif,Mixed traditional}

## Use Case Description

This template helps transform handwritten or informal recipes into shareable digital formats. The AI decodes difficult handwriting, standardizes measurements, and creates clear cooking instructions. It can generate interactive formats with serving adjusters, cultural context, and preserve the original recipe for sentimental value.

## Variables Explanation

- **RECIPE_SOURCE**: Where the recipe comes from
- **AUDIENCE**: Who will receive the recipe
- **TASKS**: What needs to be done to the original
- **MEASUREMENT_STYLE**: Current measurement format
- **TARGET_MEASUREMENT_STYLE**: Desired measurement format
- **INSTRUCTION_STYLE**: How to write the steps
- **OUTPUT_FORMAT**: Final format of the recipe
- **FEATURES**: Interactive or functional features to add
- **ORIGINAL_HANDLING**: How to present the original recipe
- **CONTEXT**: Additional information to include
- **AESTHETIC**: Overall design style
- **COLORS**: Color palette
- **TYPOGRAPHY**: Font style choices
