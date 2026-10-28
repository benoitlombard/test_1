import os

import llm
from vocab import guess_fields, guess_years

SYSTEM_PROMPT = (
    "Extract hiring requirements from the RFQ. Return JSON with keys: "
    "role, seniority, min_experience (integer years), location, "
    "languages (list), certifications (list)."
)


def extract_requirements(rfq_text):
    if os.environ.get("OPENAI_API_KEY") or os.environ.get("AZURE_OPENAI_KEY"):
        return llm.call(SYSTEM_PROMPT, rfq_text)
    return _mock_extract(rfq_text)


def _mock_extract(rfq_text):
    text_lower = rfq_text.lower()
    role, seniority, location, languages, certifications = guess_fields(text_lower)
    return {
        "role": role,
        "seniority": seniority,
        "min_experience": guess_years(text_lower),
        "location": location,
        "languages": languages,
        "certifications": certifications,
    }
