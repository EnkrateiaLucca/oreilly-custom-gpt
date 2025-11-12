# Create Custom Course Materials

## Source
https://claude.com/resources/use-case/create-custom-course-materials

## Template Prompt

I'm a {SUBJECT|math,physics,chemistry,computer science,biology} professor converting my handwritten {TOPIC} notes into professional course materials. I have:
- Handwritten notes with {CONTENT_TYPE|equations,diagrams,formulas,code examples}
- A typed outline of topics

Craft a professional-looking {FORMAT|LaTeX,Markdown,HTML} document, resembling a published textbook page with {DESIGN_ELEMENTS|colored boxes,highlighted definitions,examples sections,practice problems} and precise {CONTENT_TYPE}, then convert it to {OUTPUT_FORMAT|PDF,HTML,DOCX}.

Please ensure:
- Professional typography and layout
- Clear section hierarchy
- {STYLE_PREFERENCE|Academic,Modern,Classic,Minimalist} design aesthetic
- Proper formatting of all {CONTENT_TYPE}

## Use Case Description

This template helps educators transform informal handwritten academic content into publication-ready educational materials. The system processes visual notes and technical notation, converts them into proper formatted syntax, and generates professionally formatted documents—allowing educators to focus on pedagogy rather than technical formatting.

## Variables Explanation

- **SUBJECT**: Academic discipline being taught
- **TOPIC**: Specific topic of the notes (e.g., "integration", "quantum mechanics", "algorithms")
- **CONTENT_TYPE**: Type of technical content in the notes
- **FORMAT**: Document format to create
- **DESIGN_ELEMENTS**: Visual elements to include for clarity
- **OUTPUT_FORMAT**: Final file format needed
- **STYLE_PREFERENCE**: Overall design aesthetic
