# Create a Process Flowchart

## Source
https://claude.com/resources/use-case/create-a-process-flowchart

## Template Prompt

I'm uploading our {DOCUMENT_TYPE|enterprise software implementation playbook,operational procedures,customer journey documentation,project workflow guide}—{PAGE_COUNT} pages of {PROCESS_DESCRIPTION|customer onboarding procedures,internal workflows,decision-making processes} that {PROBLEM|nobody can navigate in real-time,are difficult to understand,need visualization}.

We have {PATH_COUNT|a few different,several,multiple} paths based on {DECISION_FACTORS|data quality, integration capability, resources, and deployment readiness,customer segment, project complexity, risk level,urgency, budget, and technical requirements}.

Can you help me visualize this so we can:
- See the whole system in one view
- Understand how {FLOW_METRIC|customer volume,project volume,request volume,transactions} distributes across the different paths
- {ADDITIONAL_GOAL|Identify bottlenecks,Optimize decision points,Train new team members,Document best practices}

**Visualization Requirements:**

Create a {DIAGRAM_TYPE|Sankey flow diagram,Process flowchart,Decision tree,Swimlane diagram,BPMN diagram} with:
- {VISUAL_STYLE|Organic curved paths,Straight connectors,Angular connections,Minimalist lines}
- {COLOR_SCHEME|Color-coded by department,Gradient by complexity,Status-based colors,Monochrome with highlights}
- {SIZING|Proportional widths showing volume distribution,Equal-sized elements,Hierarchical sizing}

**Interactive Elements:**
- {INTERACTION_TYPE|Clickable cards,Hover tooltips,Expandable sections,Linked documentation} revealing {DETAIL_LEVEL|detailed documentation behind each phase,step-by-step instructions,requirements and criteria,examples and edge cases}
- {NAVIGATION|Phase-to-phase navigation,Jump to section links,Search functionality,Filter by path type}

**Content to Display:**

For each {PROCESS_STAGE|phase,step,decision point,milestone}:
- {STAGE_INFO|Stage name and description,Duration estimates,Required inputs/outputs,Responsible parties}
- {DECISION_CRITERIA|Decision logic and criteria,Branching conditions,Success metrics,Exit criteria}
- {METADATA|Volume statistics,Completion rates,Average time,Common issues}

**Technical Specifications:**
- Format: {OUTPUT_FORMAT|Interactive HTML,SVG diagram,Mermaid diagram,Editable Figma file}
- Layout: {LAYOUT_DIRECTION|Left-to-right flow,Top-to-bottom,Circular,Matrix}
- Accessibility: {ACCESSIBILITY_FEATURES|Screen reader compatible,High contrast mode,Keyboard navigation,Text alternatives}

## Use Case Description

This template helps transform lengthy procedural documentation into interactive visual flowcharts. The system analyzes process documents to identify structure, decision points, and logic flows, then generates diagrams showing how volume or work distributes across different pathways. The resulting visualizations can include interactive elements revealing detailed documentation behind each phase, making complex procedures accessible for team understanding and real-time reference.

## Variables Explanation

- **DOCUMENT_TYPE**: Type of process documentation being visualized
- **PAGE_COUNT**: Length of the documentation (e.g., "42", "150", "200+")
- **PROCESS_DESCRIPTION**: What the process covers
- **PROBLEM**: Why visualization is needed
- **PATH_COUNT**: How many different paths exist in the process
- **DECISION_FACTORS**: Criteria that determine which path is followed
- **FLOW_METRIC**: What metric flows through the process
- **ADDITIONAL_GOAL**: Secondary objectives for the visualization
- **DIAGRAM_TYPE**: Type of flowchart or diagram to create
- **VISUAL_STYLE**: Aesthetic style of connectors and paths
- **COLOR_SCHEME**: How to use color in the diagram
- **SIZING**: How to size elements in the diagram
- **INTERACTION_TYPE**: Interactive features to include
- **DETAIL_LEVEL**: Information revealed through interactions
- **NAVIGATION**: Navigation features for the diagram
- **PROCESS_STAGE**: Term used for steps in the process
- **STAGE_INFO**: Basic information to display for each stage
- **DECISION_CRITERIA**: Logic and decision information
- **METADATA**: Quantitative data to include
- **OUTPUT_FORMAT**: File format for the final diagram
- **LAYOUT_DIRECTION**: Flow direction of the diagram
- **ACCESSIBILITY_FEATURES**: Accessibility requirements
