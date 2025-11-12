# Create Interactive PDF Forms

## Source
https://claude.com/resources/use-case/create-interactive-pdf-forms

## Template Prompt

Create a professional {FORM_TYPE|event registration,feedback survey,application,order,intake} form for {EVENT_OR_PURPOSE}. The form should include:

**Form Sections:**
- {SECTION_1|Attendee information,Contact details,Personal information} with fields for {FIELDS_1|name, email, phone}
- {SECTION_2|Registration details,Preferences,Requirements} with {FIELD_TYPE_2|dropdown menus,checkboxes,radio buttons} for {OPTIONS_2}
- {SECTION_3|Session interests,Additional options,Special requests} with checkboxes for {OPTIONS_3}
- {SECTION_4|Communication preferences,Consent,Terms}

**Branding Requirements:**
- Use {BRAND_COLORS|company colors,specific hex codes}
- Include {LOGO_POSITION|header,footer,top-right} logo placement
- {STYLE|Modern and clean,Professional and formal,Minimalist,Colorful} design aesthetic

**Technical Requirements:**
- Interactive form fields that work in any PDF reader
- {ADDITIONAL_FEATURES|Calculation fields,Validation rules,Conditional visibility}

Please ensure the form is {DISTRIBUTION_METHOD|email-ready,print-friendly,web-compatible} and includes clear instructions for completion.

## Use Case Description

This template helps create interactive PDFs with functional form fields that recipients can fill out digitally in any PDF reader. The workflow involves describing the form requirements, providing brand context, and generating a professional form ready for distribution.

## Variables Explanation

- **FORM_TYPE**: Type of form being created
- **EVENT_OR_PURPOSE**: Specific event or purpose (e.g., "Innovation Summit 2025")
- **SECTION_1-4**: Different sections of the form
- **FIELDS_1**: Specific fields needed in first section
- **FIELD_TYPE_2**: Type of input fields (dropdown, checkbox, etc.)
- **OPTIONS_2-3**: Specific options or choices to include
- **BRAND_COLORS**: Color scheme to use
- **LOGO_POSITION**: Where to place branding elements
- **STYLE**: Overall design style
- **ADDITIONAL_FEATURES**: Advanced form features needed
- **DISTRIBUTION_METHOD**: How the form will be shared
