# Prompt Template Structure Walkthrough

## Overview

This guide explains how to use the templatized prompts in this directory. Each template is designed to be reusable across different contexts by replacing variables with your specific details.

## Template Variable Syntax

### Basic Variables: `{VARIABLE_NAME}`

Simple placeholders that you replace with your specific value.

**Example:**
```
Template: I need help with {SUBJECT}
Usage: I need help with Python programming
```

### Multi-Option Variables: `{VARIABLE|option1,option2,option3}`

Variables that suggest common options to choose from. Pick one option or provide your own alternative.

**Example:**
```
Template: Create a {FORMAT|PDF,HTML,DOCX} document
Usage: Create a PDF document
OR
Usage: Create a LaTeX document (your own option)
```

### Descriptive Variables: `{VARIABLE|description}`

Variables followed by a single descriptive option serve as examples of what to provide.

**Example:**
```
Template: in {TIME_PERIOD|early June,late September,winter}
Usage: in mid-November
```

## How to Use These Templates

### Step 1: Choose Your Template

Browse the template files to find one that matches your use case. Each file includes:
- **Source**: Original URL for reference
- **Template Prompt**: The templatized version
- **Use Case Description**: What the prompt accomplishes
- **Variables Explanation**: Detailed explanation of each variable

### Step 2: Identify Variables

Scan through the template and note all variables in `{CURLY_BRACES}`.

**Example from create-sales-reports.md:**
```
I need a {QUARTER} sales report for our exec team meeting next week.
```

Variables to replace: `{QUARTER}`

### Step 3: Replace Variables

Go through each variable and substitute with your specific information.

**Before:**
```
I need a {QUARTER} sales report for {DATA_SOURCE|HubSpot,Salesforce,Drive}.
```

**After:**
```
I need a Q4 sales report for HubSpot.
```

### Step 4: Customize Further

Templates are starting points. Feel free to:
- Add more details
- Remove sections that don't apply
- Modify language to match your style
- Combine elements from multiple templates

## Understanding Multi-Option Variables

Multi-option variables use the pipe `|` character to separate choices.

### Format: `{VARIABLE|option1,option2,option3,option4}`

**Purpose:**
- Provide common use cases
- Spark ideas for what to specify
- Show the range of possibilities

**You are NOT limited to these options** - they're suggestions based on common patterns.

### Example:

**Template:**
```
Create visualizations using {CHART_TYPE|bar chart,line graph,scatter plot,heatmap}
```

**Valid usages:**
```
Create visualizations using bar chart (from options)
Create visualizations using pie chart (your own choice)
Create visualizations using Sankey diagram (specialized choice)
```

## Template Structure Components

Each template file contains:

### 1. Title
The name of the use case (e.g., "Create Digital Recipe Cards")

### 2. Source
The original URL where the use case was published

### 3. Template Prompt
The main templatized prompt with all variables clearly marked

### 4. Use Case Description
A brief explanation of:
- What problem the prompt solves
- What output it generates
- Who might use it

### 5. Variables Explanation
Detailed breakdown of each variable including:
- What it represents
- What kind of information to provide
- Examples where helpful

## Real-World Example

Let's walk through using the **create-daily-travel-itinerary.md** template:

### Original Template Snippet:
```
Create a {DURATION}-day trip itinerary for my visit to {DESTINATION} in {TIME_PERIOD}.

Travel Style Preferences:
- {DINING_PREFERENCE|Authentic neighborhood restaurants,Michelin-starred dining,Street food}
- {INTERESTS|Architecture,Art museums,Historical sites,Food culture}
```

### Step 1: Identify Your Values
- DURATION: 7
- DESTINATION: Tokyo
- TIME_PERIOD: April during cherry blossom season
- DINING_PREFERENCE: Mix of izakayas and ramen shops
- INTERESTS: Japanese gardens, temples, and anime culture

### Step 2: Fill in the Template
```
Create a 7-day trip itinerary for my visit to Tokyo in April during cherry blossom season.

Travel Style Preferences:
- Mix of izakayas and ramen shops with some traditional kaiseki experiences
- Japanese gardens, temples, and anime culture hotspots
```

### Step 3: Enhance with Details
```
Create a 7-day trip itinerary for my visit to Tokyo in April during cherry blossom season.

Travel Style Preferences:
- Mix of izakayas and ramen shops with 1-2 traditional kaiseki experiences
- Japanese gardens (especially those famous for cherry blossoms), historical temples, anime culture (Akihabara, Studio Ghibli Museum), and one day trip outside Tokyo

Activity Level:
- Walk 5-6 miles daily with some subway usage
- Visit only top-rated temples and gardens
- Balance between popular spots and less touristy neighborhoods
```

## Advanced Tips

### Combining Multiple Variables

Some templates have complex nested structures. Handle them systematically:

```
Break it down by {SEGMENT_TYPE|segment,region,product line}: {SEGMENT_OPTIONS}.
For each one, show {METRICS|revenue,conversion rate,customer count}.
```

**Approach:**
1. Choose SEGMENT_TYPE: "region"
2. List SEGMENT_OPTIONS: "North America, Europe, Asia-Pacific"
3. Choose METRICS: "revenue, growth rate, market share"

**Result:**
```
Break it down by region: North America, Europe, Asia-Pacific.
For each one, show revenue, growth rate, and market share.
```

### Adapting Templates for Different Tools

The same template can work across different AI tools (ChatGPT, Claude, etc.), but you might need to adjust:

**For file uploads:**
- Claude: "I've uploaded..." or attach files directly
- ChatGPT: "I've attached..." or use file upload feature

**For data access:**
- Some templates reference integrations (Slack, HubSpot)
- If unavailable, adapt to: "Using the data below..." and paste content

### Creating Your Own Templates

After using these templates, you might want to create your own:

1. **Start with a successful prompt** you've used
2. **Identify repeated elements** that change between uses
3. **Replace specific details** with `{DESCRIPTIVE_VARIABLES}`
4. **Add multi-option hints** for common variations
5. **Document what each variable means**

## Common Pitfalls to Avoid

### 1. Being Too Literal
**Don't:** Only use the exact options listed in multi-option variables
**Do:** Use them as inspiration and provide what you actually need

### 2. Incomplete Replacement
**Don't:**
```
Create a {DURATION}-day itinerary for Tokyo
```
**Do:**
```
Create a 5-day itinerary for Tokyo
```

### 3. Losing Context
Some variables depend on others. Maintain logical consistency:
```
I'm a {SUBJECT} professor converting {TOPIC} notes...
```
Make sure TOPIC relates to SUBJECT (e.g., "math professor converting calculus notes" not "math professor converting chemistry notes")

### 4. Ignoring the Description Section
The "Use Case Description" and "Variables Explanation" provide crucial context. Read them before using the template.

## Template Adaptation Examples

### Example 1: Simplifying a Template

**Original (from create-custom-course-materials.md):**
```
I'm a {SUBJECT} professor converting my handwritten {TOPIC} notes into professional course materials.
Craft a professional-looking {FORMAT} document with {DESIGN_ELEMENTS}.
```

**Simplified for different use:**
```
I'm converting my handwritten recipe collection into a professional cookbook.
Craft a professional-looking PDF document with photos and decorative borders.
```

### Example 2: Expanding a Template

**Original (from genomic-data-analysis.md):**
```
Can you help me go through the differentially expressed genes and create a {VISUALIZATION_TYPE}?
```

**Expanded version:**
```
Can you help me go through the differentially expressed genes and create a heatmap?
Additionally, perform GO term enrichment analysis, create a volcano plot highlighting
genes with p-value < 0.05, and generate a summary table of the top 20 upregulated
and downregulated genes with their functions.
```

## Integration with AI Assistants

### Best Practices for Using Templates

1. **Start with the basics**: Fill in required variables first
2. **Add context gradually**: Start simple, then add details based on initial responses
3. **Iterate**: Templates are conversation starters, not complete specifications
4. **Reference files**: When templates mention uploading files, prepare them in advance

### Example Conversation Flow

**First prompt (using template):**
```
Create a 3-day trip itinerary for my visit to Paris in September.
I prefer authentic bistros where locals eat and am interested in Impressionist art
and architecture from the Belle Époque period.
```

**Follow-up refinement:**
```
Can you adjust day 2 to include more time at Musée d'Orsay and add a dinner
reservation recommendation in the Marais district?
```

**Final polish:**
```
Format this as a mobile-friendly HTML page with a map showing the daily routes.
```

## Conclusion

These templates are designed to:
- **Save time** by providing proven prompt structures
- **Inspire ideas** through multi-option variables
- **Ensure completeness** by highlighting key information to include
- **Enable consistency** across similar tasks

Remember: Templates are starting points, not rigid formulas. Adapt them to your specific needs, combine elements from multiple templates, and don't hesitate to add your own requirements.

## Quick Reference

| Syntax | Meaning | Example |
|--------|---------|---------|
| `{VARIABLE}` | Simple placeholder | `{TOPIC}` → "machine learning" |
| `{VAR\|opt1,opt2}` | Multi-option variable | `{FORMAT\|PDF,HTML}` → "PDF" or "LaTeX" |
| Required variables | Always replace these | All CAPS variables in templates |
| Optional sections | Can be removed if not needed | Sections marked as optional in description |

## Getting Help

If you're unsure how to use a template:
1. Read the "Use Case Description" section
2. Check the "Variables Explanation" section
3. Look at the original source URL for real examples
4. Start with a simplified version and iterate
5. Experiment - AI assistants are forgiving of imperfect prompts!
