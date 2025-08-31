# backend/services/__init__.py
# NLP using OpenAI or Hugging Face transformers
# This example uses Hugging Face, but swap out for OpenAI if desired
from transformers import pipeline

nlp = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

def parse_query_nlp(query):
    candidate_labels = ["cheap", "strong", "sustainable", "lightweight", "metal", "polymer", "wood"]
    result = nlp(query, candidate_labels)
    # Map labels and scores to filter keys/values
    filters = {}
    for label, score in zip(result['labels'], result['scores']):
        if score > 0.5:
            filters[label] = True
    return filters
    
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
