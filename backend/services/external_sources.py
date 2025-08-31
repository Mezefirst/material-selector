import requests

def fetch_matweb_materials(query: str):
    # Hypothetical example; adapt to real API details
    url = f"https://api.matweb.com/search?query={query}"
    headers = {"Authorization": "Bearer YOUR_TOKEN"}
    response = requests.get(url, headers=headers)
    return response.json()

def fetch_material_project_materials(query: str):
    url = f"https://materialsproject.org/rest/v2/materials/{query}/vasp"
    headers = {"X-API-KEY": "YOUR_KEY"}
    response = requests.get(url, headers=headers)
    return response.json()
