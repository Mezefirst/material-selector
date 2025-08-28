import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.cluster import KMeans

def filter_materials(materials, min_strength, max_cost, min_sustainability):
    return [
        m for m in materials
        if m["strength"] >= min_strength and m["cost"] <= max_cost and m["sustainability"] >= min_sustainability
    ]

def find_alternatives(materials, target_material, n_alts=3):
    features = np.array([[m["strength"], m["cost"], m["sustainability"]] for m in materials])
    kmeans = KMeans(n_clusters=min(len(materials), n_alts + 1)).fit(features)
    clusters = kmeans.labels_
    target_idx = next(i for i, m in enumerate(materials) if m["name"] == target_material["name"])
    target_cluster = clusters[target_idx]
    return [materials[i] for i, c in enumerate(clusters) if c == target_cluster and i != target_idx][:n_alts]

def simulate_tradeoff(material_a, material_b):
    return {
        "strength_diff": material_b["strength"] - material_a["strength"],
        "cost_diff": material_b["cost"] - material_a["cost"],
        "sustainability_diff": material_b["sustainability"] - material_a["sustainability"],
    }
