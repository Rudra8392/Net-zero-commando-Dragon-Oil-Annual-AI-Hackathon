# -*- coding: utf-8 -*-
"""NLP Model to Count Wax

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1n78snUwTqMSOmL7Z9sWe6wJs4Zph9qtn
"""

import spacy
from spacy.matcher import PhraseMatcher

# Load spaCy's pre-trained language model
nlp = spacy.load("en_core_web_sm")

# List of comments (operational logs)
comments = [
    "The well is flowing on 20/64\" fixed choke to - Desander > Low Pressure Manifold system via desander 10\" m/f.",
    "Slickline team carried out wax cut operation-73m wax.",
    "GL to Casing from well 354. The GL needle valve open position 3.5/3.5 turn. (Casing GL splash oil with gas)",
    "Injecting chemical of WM-2090 to CIN - 20 L/D.",
    "Slickline team carried out wax cut operation-70m soft wax. Between 10:30-10:45 DS flushed with HD -2t.",
    "Slickline team carried out wax cut operation-75m soft wax.",
    "Slickline team carried out wax cut operation-30m soft wax. DS line flushed with HD.",
    "Slickline team carried out wax cut operation-20m soft wax.",
    "Slickline team carried out wax cut operation-50m soft wax.",
    "Slickline team carried out wax cut operation-65m wax.",
    "Slickline team carried out wax cut operation-10m wax. DS line flushed with HD.",
    "Well Head Maintenance team performed Greasing bearings of X-mass tree and Annulus gate valves.",
    "Slickline team carried out wax cut operation-35 m wax.",
    "Between 10:00-10:15 DS flushed with HD -2t.",
    "At 15:00 commenced 6hrs well test. At 21:00 stopped test.",
    "Slickline team carried out wax cut operation-40 m soft wax.",
    "Slickline team carried out wax cut operation-45 m soft wax. Gas flowed.",
    "B/W 11:00>17:00 rate test 6hrs was done. Flow rates oil:-211.29 bbl/d; water -72.28 bbl/d; gas -0.36 mmscf/d.",
    "Slickline team carried out wax cut operation-37m soft wax. US/DS line flushed with HD.",
    "Slickline team carried out wax cut operation-47 m soft wax. Gas flowed.",
    "Slickline team carried out wax cut operation-30 m soft wax.",
    "Slickline team carried out wax cut operation-10 m soft wax.",
    "Slickline team carried out wax cut operation-10m of wax."
]

# Count the number of times "wax" appears in the comments
wax_count = sum(1 for comment in comments if "wax" in comment.lower())

print(f"The term 'wax' appears {wax_count} times in the comments.")

# Define key phrases that indicate potential causes of production decline
decline_causes = [
    "wax cut", "chemical injection", "flow rates", "gas flowed", "oil production", "water production",
    "choke", "desander", "manifold system", "needle valve", "greasing", "annulus gate valve",
    "well test", "flushed with HD", "rate test"
]

# Initialize PhraseMatcher
matcher = PhraseMatcher(nlp.vocab)

# Add patterns to matcher
patterns = [nlp.make_doc(cause) for cause in decline_causes]
matcher.add("DeclineCauses", None, *patterns)

# Process each comment and identify potential decline causes
identified_causes = {}

for comment in comments:
    doc = nlp(comment)
    matches = matcher(doc)
    causes_in_comment = set()  # Store unique causes per comment

    for match_id, start, end in matches:
        span = doc[start:end]
        causes_in_comment.add(span.text)  # Extract matched cause

    if causes_in_comment:
        identified_causes[comment] = list(causes_in_comment)

# Output the identified causes
print("\nPotential causes of production decline found in comments:")
for comment, causes in identified_causes.items():
    print(f"\nComment: {comment}")
    print(f"Possible Causes: {', '.join(causes)}")