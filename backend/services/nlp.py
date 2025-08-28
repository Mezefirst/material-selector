# backend/services/__init__.py
# NLP using OpenAI or Hugging Face transformers
# This example uses Hugging Face, but swap out for OpenAI if desired

def parse_user_query(query: str):
    # Placeholder: return hardcoded filters for demo
    # In production, use transformers pipeline or OpenAI API to extract intents/entities
    if "cheap" in query.lower():
        return {"max_cost": 2.0}
    if "strong" in query.lower():
        return {"min_strength": 400}
    if "sustainable" in query.lower():
        return {"min_sustainability": 8}
    # Add more parsing as needed
    return {}
