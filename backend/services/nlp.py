# NLP service for parsing user queries
# Lightweight rule-based parser with optional ML enhancement

import re
from typing import Dict

def parse_query_nlp(query: str) -> Dict:
    """Enhanced NLP parsing using keyword matching and pattern recognition"""
    query = query.lower().strip()
    filters = {}
    
    # Extract numeric values
    numbers = re.findall(r'\d+(?:\.\d+)?', query)
    
    # Cost-related terms
    if any(word in query for word in ['cheap', 'inexpensive', 'low cost', 'affordable']):
        filters['max_cost'] = 5.0 if not numbers else min(float(numbers[0]), 10.0)
    elif any(word in query for word in ['expensive', 'premium', 'high cost']):
        filters['min_cost'] = 10.0 if not numbers else max(float(numbers[0]), 5.0)
    
    # Strength-related terms
    if any(word in query for word in ['strong', 'strength', 'durable', 'tough', 'robust']):
        filters['min_strength'] = 400 if not numbers else max(float(numbers[0]), 100)
    elif any(word in query for word in ['weak', 'soft', 'fragile']):
        filters['max_strength'] = 200 if not numbers else min(float(numbers[0]), 500)
    
    # Sustainability terms
    if any(word in query for word in ['sustainable', 'eco', 'green', 'environmental', 'recyclable']):
        filters['min_sustainability'] = 7 if not numbers else max(float(numbers[0]), 5)
    
    # Material type detection
    if any(word in query for word in ['metal', 'steel', 'aluminum', 'titanium']):
        filters['types'] = ['Metal']
    elif any(word in query for word in ['composite', 'carbon', 'fiber']):
        filters['types'] = ['Composite']
    elif any(word in query for word in ['natural', 'wood', 'bamboo']):
        filters['types'] = ['Natural']
    
    # Weight-related terms
    if any(word in query for word in ['light', 'lightweight', 'low weight']):
        # Prefer aluminum and composites for lightweight
        filters['types'] = filters.get('types', []) + ['Composite']
    
    # General search terms
    search_terms = []
    for word in query.split():
        if len(word) > 3 and word not in ['cheap', 'strong', 'sustainable', 'light', 'heavy']:
            search_terms.append(word)
    
    if search_terms:
        filters['search'] = ' '.join(search_terms)
    
    return filters

def parse_user_query(query: str) -> Dict:
    """Main function for parsing user queries"""
    if not query or not query.strip():
        return {}
    
    try:
        # Use enhanced NLP parsing
        return parse_query_nlp(query)
    except Exception:
        # Fallback to simple keyword matching
        query = query.lower()
        filters = {}
        
        if "cheap" in query:
            filters["max_cost"] = 3.0
        if "strong" in query:
            filters["min_strength"] = 400
        if "sustainable" in query:
            filters["min_sustainability"] = 8
        if "light" in query:
            filters["max_cost"] = 20.0  # Lightweight materials tend to be more expensive
        
        return filters
