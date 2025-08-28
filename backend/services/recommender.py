from typing import List, Dict
# Import AI logic from ai_recommender.py (as previously discussed)
from ai_recommender import filter_materials, find_alternatives, simulate_tradeoff

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
