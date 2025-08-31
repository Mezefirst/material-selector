from typing import List, Dict
# Import AI logic from ai_recommender.py (as previously discussed)
from ai_recommender import filter_materials, find_alternatives, simulate_tradeoff
import joblib
import numpy as np

# Load pre-trained models (assuming you have .joblib files)
xgb_model = joblib.load("models/xgb_recommender.joblib")
nn_model = joblib.load("models/nn_recommender.joblib")

def recommend_materials_ml(features, model_type="xgb"):
    if model_type == "xgb":
        preds = xgb_model.predict(features)
    elif model_type == "nn":
        preds = nn_model.predict(features)
    else:
        raise ValueError("Unknown model type")
    return preds


def recommend_materials(filters):
    # Example: filter locally; replace with DB queries as needed
    from backend.data.materials import MATERIALS
    results = MATERIALS

    # Filter by types
    if filters.get("types"):
        results = [m for m in results if m["type"] in filters["types"]]
    # Filter by colors
    if filters.get("colors"):
        results = [m for m in results if m["color"] in filters["colors"]]
    # Range filters
    results = [m for m in results if filters.get("min_strength", 0) <= m["strength"] <= filters.get("max_strength", 2000)]
    results = [m for m in results if filters.get("min_cost", 0) <= m["cost"] <= filters.get("max_cost", 1000)]
    results = [m for m in results if filters.get("min_sustainability", 0) <= m["sustainability"] <= filters.get("max_sustainability", 10)]
    # Fuzzy search and full-text match
    if filters.get("search"):
        query = filters["search"].lower()
        results = [m for m in results if query in m["name"].lower() or query in m.get("properties", "").lower() or query in m.get("description", "").lower()]
    return results
    
from backend.services.nlp import parse_query_nlp

def recommend_materials(filters, query=None, model_type="xgb"):
    # NLP parsing
    if query:
        nlp_filters = parse_query_nlp(query)
        filters.update(nlp_filters)
    # Build feature vector from filters
    features = np.array([filters.get("strength", 0), filters.get("cost", 0), filters.get("sustainability", 0)])
    # ML-based recommendation
    material_ids = recommend_materials_ml(features.reshape(1, -1), model_type)
    # Retrieve material details
    from backend.data.materials import MATERIALS
    results = [m for m in MATERIALS if m["id"] in material_ids]
    return results
    
# Extend rule-based logic as needed    
def recommend_materials(filters: Dict):
    # Load materials from DB in a real implementation
    materials = [
        {"name": "Steel", "strength": 500, "cost": 2.0, "sustainability": 5},
        {"name": "Aluminum", "strength": 300, "cost": 3.0, "sustainability": 7},
        {"name": "Bamboo", "strength": 100, "cost": 1.0, "sustainability": 10}
    ]
    min_strength = filters.get("min_strength", 0)
    max_cost = filters.get("max_cost", float("inf"))
    min_sustainability = filters.get("min_sustainability", 0)
    return filter_materials(materials, min_strength, max_cost, min_sustainability)

def suggest_alternatives(material: Dict):
    # Load materials from DB in a real implementation
    materials = [
        {"name": "Steel", "strength": 500, "cost": 2.0, "sustainability": 5},
        {"name": "Aluminum", "strength": 300, "cost": 3.0, "sustainability": 7},
        {"name": "Bamboo", "strength": 100, "cost": 1.0, "sustainability": 10}
    ]
    return find_alternatives(materials, material)

def simulate_tradeoff(material_a: Dict, material_b: Dict):
    return simulate_tradeoff(material_a, material_b)
