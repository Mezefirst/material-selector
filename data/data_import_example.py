import csv
from models import Material
def import_matweb_csv(file_path, session):
    with open(file_path) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            material = Material(
                name=row['Material Name'],
                category=row['Category'],
                cost_per_kg=float(row.get('Cost', 0)),
                tensile_strength=float(row.get('Tensile Strength', 0)),
                yield_strength=float(row.get('Yield Strength', 0)),
                modulus=float(row.get('Modulus', 0)),
                elongation=float(row.get('Elongation', 0)),
                hardness=float(row.get('Hardness', 0)),
                embodied_energy=float(row.get('Embodied Energy', 0)),
                co2_footprint=float(row.get('CO2 Footprint', 0)),
                recyclability=row.get('Recyclability', ''),
                availability=row.get('Availability', ''),
                datasheet_url=row.get('Datasheet URL', '')
            )
            session.add(material)
        session.commit()
