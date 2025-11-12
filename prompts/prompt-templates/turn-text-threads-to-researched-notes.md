# Turn Text Threads to Researched Notes

## Source
https://claude.com/resources/use-case/turn-text-threads-to-researched-notes

## Template Prompt

Read my {MESSAGE_SOURCE|Messages,Slack thread,Email chain,WhatsApp conversation} to see the full context about {TOPIC|the potluck dessert request,the project requirements,the meeting discussion,the research question}, then help me figure out {GOAL|what to make,what to do,how to proceed,what to research}.

**Context and Requirements:**
From the conversation, identify:
- {KEY_INFO|Who requested what,Requirements and constraints,Preferences mentioned,Timeline and deadlines}
- {SPECIFIC_CRITERIA|Impressive but not complicated,Budget-friendly,Time-sensitive,Skill level appropriate}
- {PRACTICAL_CONSTRAINTS|Must travel well,Can be prepared ahead,Dietary restrictions,Available resources}

**Research Phase:**
Search online for {SEARCH_TARGET|recipes,solutions,approaches,products,resources} that match:
- {REQUIREMENT_1|Impressive presentation,High quality,Professional level}
- {REQUIREMENT_2|Manageable complexity,Time-efficient,Beginner-friendly}
- {REQUIREMENT_3|Practical constraints met,Budget-conscious,Readily available materials}
- {ADDITIONAL_FILTERS|Highly rated,Recently published,Expert-recommended,Community-tested}

**Output Requirements:**
Create {OUTPUT_TYPE|organized recipe notes,action plan,research summary,recommendation document} and save to {SAVE_LOCATION|Notes app,Google Docs,Notion,email draft} with:

**Main Content:**
- {CONTENT_SECTION_1|Recipe with clear instructions,Step-by-step action plan,Summary of findings}
- {CONTENT_SECTION_2|Ingredient list,Materials needed,Resources required}
- {CONTENT_SECTION_3|Tips and variations,Best practices,Alternatives}
- {TIMING_INFO|Prep time and timeline,Project schedule,Important dates}

**Organized Lists:**
Create {LIST_TYPE|categorized shopping list,task breakdown,resource inventory} organized by {ORGANIZATION_METHOD|store sections,priority,category,phase}:
- {CATEGORY_1|Produce,Phase 1,High priority}
- {CATEGORY_2|Dairy,Phase 2,Medium priority}
- {CATEGORY_3|Pantry,Phase 3,Optional items}
- {CATEGORY_4|Specialty items,Equipment,Nice-to-haves}

**Additional Features:**
- {FEATURE_1|Quantity adjustments,Scalability notes,Alternative options}
- {FEATURE_2|Cost estimates,Time estimates,Difficulty ratings}
- {FEATURE_3|Links to references,Source attribution,Visual references}

**Follow-up Actions:**
- {ACTION_1|Reply to the message thread,Send update email,Post response}
- {ACTION_2|Set reminders,Create calendar events,Schedule tasks}
- {ACTION_3|Share the notes,Coordinate with others,Request feedback}

## Use Case Description

This template demonstrates multi-tool integration workflows where Claude reads context from messages or conversations, researches solutions using web search, and outputs structured notes to a destination app. The system extracts requirements from casual conversations, finds options matching specific criteria, and creates organized documentation to streamline execution. It can also handle follow-up actions like replying to messages or adjusting plans when circumstances change.

## Variables Explanation

- **MESSAGE_SOURCE**: Where the conversation is happening
- **TOPIC**: What the conversation is about
- **GOAL**: What needs to be accomplished
- **KEY_INFO**: Important information to extract from the conversation
- **SPECIFIC_CRITERIA**: Qualitative requirements mentioned
- **PRACTICAL_CONSTRAINTS**: Practical limitations to consider
- **SEARCH_TARGET**: What to research online
- **REQUIREMENT_1-3**: Specific criteria for the research
- **ADDITIONAL_FILTERS**: Quality filters for research results
- **OUTPUT_TYPE**: Type of document to create
- **SAVE_LOCATION**: Where to save the final output
- **CONTENT_SECTION_1-3**: Main sections of the output document
- **TIMING_INFO**: Time-related information to include
- **LIST_TYPE**: Type of organized list needed
- **ORGANIZATION_METHOD**: How to organize the list
- **CATEGORY_1-4**: Categories for organization
- **FEATURE_1-3**: Additional helpful features to include
- **ACTION_1-3**: Follow-up actions to take
