CREATE TABLE materials (
  id SERIAL PRIMARY KEY,
  name TEXT,
  category TEXT,
  cost_per_kg FLOAT,
  tensile_strength FLOAT,
  thermal_conductivity FLOAT,
  carbon_footprint FLOAT,
  supplier TEXT
);
