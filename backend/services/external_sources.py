import os
try:
    import requests
    REQUESTS_AVAILABLE = True
except ImportError:
    REQUESTS_AVAILABLE = False

def fetch_matweb_materials(query: str):
    """Fetch materials from MatWeb API (requires API key)"""
    if not REQUESTS_AVAILABLE:
        return {"error": "Requests library not available", "data": []}
    
    api_key = os.getenv("MATWEB_API_KEY")
    if not api_key:
        return {"error": "MatWeb API key not configured", "data": []}
    
    try:
        # Example API call - adapt to real MatWeb API
        url = f"https://api.matweb.com/search?query={query}"
        headers = {"Authorization": f"Bearer {api_key}"}
        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code == 200:
            return {"data": response.json(), "source": "matweb"}
        else:
            return {"error": f"MatWeb API returned status {response.status_code}", "data": []}
    except Exception as e:
        return {"error": f"MatWeb API request failed: {str(e)}", "data": []}

def fetch_material_project_materials(query: str):
    """Fetch materials from Materials Project API (requires API key)"""
    if not REQUESTS_AVAILABLE:
        return {"error": "Requests library not available", "data": []}
    
    api_key = os.getenv("MATERIALS_PROJECT_API_KEY")
    if not api_key:
        return {"error": "Materials Project API key not configured", "data": []}
    
    try:
        # Example API call - adapt to real Materials Project API
        url = f"https://materialsproject.org/rest/v2/materials/{query}/vasp"
        headers = {"X-API-KEY": api_key}
        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code == 200:
            return {"data": response.json(), "source": "materials_project"}
        else:
            return {"error": f"Materials Project API returned status {response.status_code}", "data": []}
    except Exception as e:
        return {"error": f"Materials Project API request failed: {str(e)}", "data": []}
