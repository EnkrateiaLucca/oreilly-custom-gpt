# Create a Daily Travel Itinerary

## Source
https://claude.com/resources/use-case/create-a-daily-travel-itinerary

## Template Prompt

Create a {DURATION}-day trip itinerary for my visit to {DESTINATION} in {TIME_PERIOD|early June,late September,winter,summer}.

**Travel Style Preferences:**
- {DINING_PREFERENCE|Authentic neighborhood restaurants where locals eat,Michelin-starred fine dining,Street food and casual spots,Mix of local and upscale}
- {INTERESTS|Architecture at actual monuments,Art museums,Historical sites,Food culture,Nature and outdoors}
- {ACTIVITY_LEVEL|Walk 8-10 miles daily,Leisurely pace with transit,Mix of walking and driving,Intensive exploration}
- Visit only {QUALITY_FILTER|truly exceptional museums,highly-rated attractions,off-the-beaten-path spots,major landmarks}

**Specific Interests:**
- {ARCHITECTURAL_STYLES|Manueline and Pombaline architecture,Gothic cathedrals,Modern design,Historic districts}
- {CULTURAL_EXPERIENCES|Genuine fado experiences,Local festivals,Traditional performances,Artisan workshops}
- {ACTIVITY_PREFERENCES|Skip generic collections,Avoid tourist traps,Focus on authentic experiences,Include popular highlights}

**Practical Requirements:**
- Incorporate realistic timing with {BREAK_PREFERENCES|built-in rest breaks,packed schedule,flexible timing,buffer time}
- Include {DISTANCE_INFO|walking distances,transit times,neighborhood-to-neighborhood logistics}
- Provide {ALTERNATIVES|backup options for closed venues,alternative restaurants,flexible scheduling,weather-dependent plans}
- Format as {OUTPUT_FORMAT|mobile-friendly document,PDF with maps,interactive HTML,day-by-day text}

**Research Requirements:**
- Use {RECENCY|current 2024-2025 recommendations,recent reviews,up-to-date information,latest openings}
- Verify {ACCURACY|opening hours,seasonal closures,reservation requirements,admission fees}
- Include {BOOKING_INFO|advance booking links,contact information,reservation tips}

## Use Case Description

This template helps build customized travel itineraries by combining specific personal preferences with practical constraints. The approach instructs Claude to research current recommendations, incorporate realistic timing and distances, and format the output for mobile use with alternatives for when venues are unavailable. It emphasizes filtering information through particular interests rather than generating comprehensive attraction lists.

## Variables Explanation

- **DURATION**: Length of trip in days
- **DESTINATION**: City or region being visited
- **TIME_PERIOD**: When the trip will occur
- **DINING_PREFERENCE**: Type of restaurants preferred
- **INTERESTS**: Main areas of interest
- **ACTIVITY_LEVEL**: Physical activity preference
- **QUALITY_FILTER**: What level of attractions to include
- **ARCHITECTURAL_STYLES**: Specific architectural interests
- **CULTURAL_EXPERIENCES**: Types of cultural activities wanted
- **ACTIVITY_PREFERENCES**: What to include or avoid
- **BREAK_PREFERENCES**: Pacing of the itinerary
- **DISTANCE_INFO**: Logistical details to include
- **ALTERNATIVES**: Backup options to provide
- **OUTPUT_FORMAT**: How to format the itinerary
- **RECENCY**: How current the information should be
- **ACCURACY**: What details to verify
- **BOOKING_INFO**: Reservation details to include
