# Create a Company Newsletter

## Source
https://claude.com/resources/use-case/create-a-company-newsletter

## Template Prompt

Create a {FREQUENCY|weekly,monthly,quarterly} digest for {DATE_RANGE} for my company. Pull information from relevant channels in my {COMMUNICATION_PLATFORM|Slack,Teams,Discord,email}, such as {CHANNEL_LIST}, and any other channels where major decisions happened.

**Content Requirements:**
- Include {VISUALIZATION_TYPES|data visualizations,charts,graphs,infographics} where useful
- Highlight {CONTENT_PRIORITIES|company announcements,product updates,team achievements,project milestones}
- Use a {DENSITY|dense but readable,spacious and airy,information-packed} layout

**Design Specifications:**
- Go for a {AESTHETIC|British newspaper,Modern tech blog,Corporate professional,Startup casual} aesthetic
- {DESIGN_CONSTRAINTS|No gradients, shadows, rounded corners, or bright colors,Use modern card-based layouts,Incorporate brand colors throughout}
- {TYPOGRAPHY_STYLE|Print-like typography with tight leading,Modern sans-serif with generous spacing,Classic serif with traditional spacing}
- Pack information efficiently using sophisticated typography and spacing

**Publication Elements:**
- Include {ELEMENTS|standfirsts,pull quotes with left borders,desk attributions,bylines,section headers}
- Add sourced charts using {CHART_LIBRARY|Chart.js,D3.js,embedded images}
- Format as {OUTPUT_FORMAT|HTML,PDF,Email-ready HTML}

## Use Case Description

This template helps synthesize company communication channels into publication-style digests. The system filters for important discussions, organizes information by topic, and presents findings in a carefully designed format. Users can request interactive outputs with visualizations, data charts, and refined layouts.

## Variables Explanation

- **FREQUENCY**: How often the newsletter is published
- **DATE_RANGE**: Time period to cover (e.g., "Oct 14-20")
- **COMMUNICATION_PLATFORM**: Where company communications happen
- **CHANNEL_LIST**: Specific channels to monitor (e.g., "#company-announcements, #product-updates")
- **VISUALIZATION_TYPES**: Types of data visualization to include
- **CONTENT_PRIORITIES**: What types of content to emphasize
- **DENSITY**: Information density preference
- **AESTHETIC**: Overall design style reference
- **DESIGN_CONSTRAINTS**: Specific design rules to follow or avoid
- **TYPOGRAPHY_STYLE**: Typography approach
- **ELEMENTS**: Editorial/publication elements to include
- **CHART_LIBRARY**: Tool for creating data visualizations
- **OUTPUT_FORMAT**: Final delivery format
