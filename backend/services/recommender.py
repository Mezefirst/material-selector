from typing import List, Dict
import os

# Import AI logic from ai_recommender.py when models are available
try:
    from backend.ai_recommender import filter_materials, find_alternatives, simulate_tradeoff as ai_simulate_tradeoff
    AI_AVAILABLE = True
except ImportError:
    AI_AVAILABLE = False

# Optional ML model loading - only if models exist
ML_MODELS_AVAILABLE = False
try:
    import joblib
    import numpy as np
    if os.path.exists("models/xgb_recommender.joblib") and os.path.exists("models/nn_recommender.joblib"):
        xgb_model = joblib.load("models/xgb_recommender.joblib")
        nn_model = joblib.load("models/nn_recommender.joblib")
        ML_MODELS_AVAILABLE = True
except (ImportError, FileNotFoundError):
    pass

def recommend_materials_ml(features, model_type="xgb"):
    """ML-based recommendation - only available if models are loaded"""
    if not ML_MODELS_AVAILABLE:
        raise ValueError("ML models not available")
    
    if model_type == "xgb":
        preds = xgb_model.predict(features)
    elif model_type == "nn":
        preds = nn_model.predict(features)
    else:
        raise ValueError("Unknown model type")
    return preds

def recommend_materials(filters: Dict) -> List[Dict]:
    """Main recommendation function with rule-based filtering"""
    from data.materials import MATERIALS
    results = MATERIALS.copy()

    # Filter by types
    if filters.get("types"):
        results = [m for m in results if m["type"] in filters["types"]]
    
    # Filter by colors
    if filters.get("colors"):
        results = [m for m in results if m["color"] in filters["colors"]]
    
    # Range filters
    min_strength = filters.get("min_strength", 0)
    max_strength = filters.get("max_strength", 2000)
    results = [m for m in results if min_strength <= m["strength"] <= max_strength]
    
    min_cost = filters.get("min_cost", 0)
    max_cost = filters.get("max_cost", 1000)
    results = [m for m in results if min_cost <= m["cost"] <= max_cost]
    
    min_sustainability = filters.get("min_sustainability", 0)
    max_sustainability = filters.get("max_sustainability", 10)
    results = [m for m in results if min_sustainability <= m["sustainability"] <= max_sustainability]
    
    # Fuzzy search and full-text match
    if filters.get("search"):
        query = filters["search"].lower()
        results = [m for m in results if 
                  query in m["name"].lower() or 
                  query in m.get("properties", "").lower() or 
                  query in m.get("description", "").lower()]
    
    # Use AI filtering if available
    if AI_AVAILABLE and results:
        try:
            min_strength = filters.get("min_strength", 0)
            max_cost = filters.get("max_cost", float("inf"))
            min_sustainability = filters.get("min_sustainability", 0)
            results = filter_materials(results, min_strength, max_cost, min_sustainability)
        except Exception:
            pass  # Fall back to rule-based results
    
    return results

def suggest_alternatives(material: Dict) -> List[Dict]:
    """Suggest alternative materials"""
    from data.materials import MATERIALS
    
    if AI_AVAILABLE:
        try:
            return find_alternatives(MATERIALS, material, n_alts=3)
        except Exception:
            pass
    
    # Fallback: simple rule-based alternatives
    alternatives = []
    for m in MATERIALS:
        if (m["name"] != material["name"] and 
            abs(m["strength"] - material["strength"]) < 200 and
            abs(m["sustainability"] - material["sustainability"]) < 3):
            alternatives.append(m)
    
    return alternatives[:3]

def simulate_tradeoff(material_a: Dict, material_b: Dict) -> Dict:
    """Simulate performance trade-offs between materials"""
    if AI_AVAILABLE:
        try:
            return ai_simulate_tradeoff(material_a, material_b)
        except Exception:
            pass
    
    # Fallback: simple difference calculation
    return {
        "strength_diff": material_b["strength"] - material_a["strength"],
        "cost_diff": material_b["cost"] - material_a["cost"],
        "sustainability_diff": material_b["sustainability"] - material_a["sustainability"],
        "recommendation": "Higher values indicate material_b performs better in that category"
    }
