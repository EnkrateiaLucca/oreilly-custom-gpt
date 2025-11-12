# ChatGPT & Claude

A comprehensive training course repository covering ChatGPT, Custom GPTs, Claude along with their feature offerings and capabilities. Containing practical examples, templates, and hands-on demonstrations for building specialized AI tools and workflows.

## Overview

This repository contains all materials for the O'Reilly Live Training course "Custom GPTs & Claude Artifacts". The course teaches participants how to leverage two powerful AI platforms to automate tasks, build specialized tools, and create interactive applications without traditional programming.

## What You'll Learn

- **Custom GPT Basics**: Understanding and building specialized ChatGPT configurations
- **Claude & Artifacts**: Creating interactive, shareable AI-powered applications
- **Practical Applications**: Real-world use cases across multiple domains
- **Best Practices**: Prompt engineering techniques and workflow optimization
- **Integration Patterns**: Using MCPs (Model Context Protocol) with Claude Desktop

## Repository Structure

```
.
├── presentation/           # Training presentation slides (Remark.js HTML)
│   ├── presentation_updated.html    # Main course slides
│   ├── presentation.html
│   └── claude-presentation-slides.html
├── prompts/
│   ├── prompt-templates/  # 14 reusable prompt templates
│   ├── custom-gpt-templates/  # Custom GPT instruction sets
│   └── claude-artifacts/  # Claude Artifact examples
├── assets/                # Images and visual resources for presentations
└── usecases/             # Real-world implementation examples
```

## Course Content

### 1. Introduction & Learning Objectives
- Course structure and goals
- AI tools landscape overview
- Setting up your environment

### 2. Custom GPT Basics
- **What & Why**: Understanding Custom GPTs as specialized AI tools
- **Use Cases**:
  - Translators of Complexity (simplifying domain knowledge)
  - Tools (automating repetitive tasks)
  - Agents (autonomous task execution)
  - Collaborators (working alongside you)
- **When to Use**: Decision framework for building vs. using existing GPTs
- **Interface Walkthrough**: Complete guide to the Custom GPT builder

### 3. Claude & Artifacts
- **Core Capabilities**:
  - Text and code generation
  - Document interaction and analysis
  - Visual content creation
- **Artifacts Features**:
  - Dedicated windows for substantial content
  - Interactive, editable outputs
  - Version history and collaboration
  - Export and sharing capabilities
- **Content Types**:
  - Documents (Markdown, Plain Text)
  - Code snippets (multiple languages)
  - Websites (single-page HTML apps)
  - SVG images and diagrams
  - Interactive React components

### 4. Claude Desktop + MCPs
- Model Context Protocol integration
- Building personal assistants with external tool access
- Advanced workflow automation

## Prompt Templates (14 Templates)

The `prompts/prompt-templates/` directory contains professionally crafted, reusable templates for common tasks:

### Creative & Design
1. **create-brand-assets.md** - Generate logos, color schemes, and brand guidelines
2. **create-custom-webpage.md** - Build single-page websites with interactive elements
3. **turn-inspiration-to-design-plans.md** - Convert ideas into structured design specifications

### Content Creation
4. **create-company-newsletter.md** - Professional internal/external communications
5. **create-digital-recipe-cards.md** - Formatted recipe cards with nutritional info
6. **create-custom-course-materials.md** - Educational content and handouts

### Business & Productivity
7. **create-sales-reports.md** - Executive-ready sales analysis and visualizations
8. **create-interactive-pdf-forms.md** - Fillable forms for data collection
9. **create-a-process-flowchart.md** - Visual process documentation

### Research & Analysis
10. **research-data-analysis.md** - Data exploration and visualization
11. **plan-literature-review.md** - Academic research organization
12. **turn-text-threads-to-researched-notes.md** - Convert conversations to structured notes
13. **turn-research-into-presentations.md** - Academic findings to slide decks

### Travel & Planning
14. **compare-travel-destinations.md** - Destination comparison matrices
15. **create-daily-travel-itinerary.md** - Detailed day-by-day trip planning

### Template Structure Guide
See `prompts/prompt-templates/prompt_template_structure_walkthrough.md` for detailed instructions on:
- Variable syntax: `{VARIABLE_NAME}`
- Multi-option variables: `{FORMAT|PDF,HTML,DOCX}`
- Customization and adaptation techniques

## Custom GPT Examples

### Italian Tutor (`prompts/custom-gpt-templates/italian-tutor.md`)
A specialized language tutor with 20 years of experience simulation:
- **Features**:
  - Translation with contextual explanations
  - Conversation scenarios based on uploaded materials
  - Interactive feedback on user responses
- **Use Case**: Language learning with structured practice

### Data Extractor (`prompts/custom-gpt-templates/data_extractor.md`)
Medical research paper data extraction engine:
- **Features**:
  - Structured data extraction from PDFs
  - Column structure confirmation
  - Table output ready for export
- **Use Case**: Systematic literature reviews and meta-analysis

## Claude Artifacts Examples

### Data Visualizer (`prompts/claude-artifacts/data_visualizer.md`)
Interactive data visualization tool for creating charts and graphs from structured data.

## Use Cases & Demos

The course includes hands-on demonstrations:
1. **Building Specialized GPT Tutors** - Custom language learning assistants
2. **PDF Data Extraction** - Automated information extraction from documents
3. **Claude Desktop with MCPs** - Deep dive into Model Context Protocol
4. **Personal Assistant Building** - Claude Desktop + MCPs integration
5. **Platform Comparison** - ChatGPT/Custom GPTs vs Claude/Artifacts

### Sample Data
- `usecases/sample_sales_data.csv` - Example dataset for data analysis demos
- `usecases/pdf-csv-usecase/` - PDF extraction workflow examples

## Getting Started

### Prerequisites
- ChatGPT Plus account (for Custom GPTs)
- Claude Pro account (for Artifacts)
- Claude Desktop (optional, for MCP integration)

### Using the Prompt Templates

1. **Choose a template** from `prompts/prompt-templates/`
2. **Identify variables** in `{CURLY_BRACES}`
3. **Replace with your values**:
   ```
   Template: Create a {DURATION}-day trip to {DESTINATION}
   Usage: Create a 7-day trip to Tokyo
   ```
4. **Customize further** - templates are starting points, adapt as needed

### Building a Custom GPT

1. Navigate to ChatGPT → Create a GPT
2. Choose a template from `prompts/custom-gpt-templates/`
3. Paste the instructions into the "Instructions" field
4. Configure capabilities (web browsing, code interpreter, file uploads)
5. Test and iterate
6. Save and share

### Creating Claude Artifacts

1. Open Claude.ai
2. Use prompts from `prompts/claude-artifacts/`
3. Request content that results in an Artifact (>15 lines, self-contained)
4. Edit in the dedicated Artifact window
5. Export, share, or save to Projects

## Key Concepts

### When to Use Custom GPTs
✓ **Use when**:
- Writing too many edits to system messages
- Complex tasks need multiple specialized prompts
- You need consistent behavior across sessions

⚡ **Build vs. Use Existing**:
- Search GPT store first
- Build custom for specific domain knowledge
- Start with concrete requirements

### Artifacts vs. Regular Chat

| Regular Chat | Artifacts |
|--------------|-----------|
| Inline text | Dedicated window |
| Primarily text | Multiple formats |
| Static | Fully editable |
| Shorter content | Complex, substantial content |
| Limited visualization | Rich visualization options |

### Custom GPTs as...
- **Translators of Complexity** - Simplify domain knowledge
- **Tools** - Automate repetitive tasks
- **Agents** - Act autonomously
- **Collaborators** - Work as partners

## Presentation

View the full training presentation by opening `presentation/presentation_updated.html` in a web browser. The presentation uses Remark.js and includes:
- Visual walkthroughs
- Code examples
- Live demonstration guides
- Interactive slides

## Best Practices

### Prompt Engineering
- Start with templates, then customize
- Be specific about desired output format
- Iterate based on results
- Combine elements from multiple templates

### Custom GPT Development
- Define clear role and process
- Set explicit output constraints
- Include example inputs/outputs
- Test with edge cases

### Artifacts Usage
- Request significant, self-contained content (>15 lines)
- Use for content that needs iteration
- Leverage version history
- Save to Projects for organization

## Resources

### Official Documentation
- [ChatGPT Custom GPTs Guide](https://help.openai.com/en/articles/8554397-creating-a-gpt)
- [Claude.ai Artifacts Documentation](https://support.anthropic.com/en/articles/9487310-what-are-artifacts-and-how-do-i-use-them)
- [Model Context Protocol (MCP)](https://modelcontextprotocol.io)

### Course Materials
- **Presentation**: `presentation/presentation_updated.html`
- **Templates**: Browse `prompts/` directory
- **Assets**: Visual resources in `assets/`

## Contributing

This repository serves as course materials. For suggestions or improvements:
1. Document your use case
2. Test your modifications
3. Ensure templates follow the established format
4. Include examples in your documentation

## License

Course materials provided for educational purposes as part of O'Reilly Live Training.

## Contact & Support

For questions about the course content or materials, refer to the O'Reilly Live Training platform or your course instructor.

---

**Last Updated**: November 2024
**Course**: Custom GPTs & Claude Artifacts
**Platform**: O'Reilly Live Training
