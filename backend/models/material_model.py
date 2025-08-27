import csv

class Material:
    def __init__(self, name, density, strength, melting_point):
        self.name = name
        self.density = float(density)
        self.strength = float(strength)
        self.melting_point = float(melting_point)

def load_materials(file_path):
    materials = []
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            mat = Material(row['Material'], row['Density (g/cm³)'], row['Tensile Strength (MPa)'], row['Melting Point (°C)'])
            materials.append(mat)
    return materials
