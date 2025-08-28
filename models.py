from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table, Boolean
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

material_supplier = Table(
    'material_supplier', Base.metadata,
    Column('material_id', Integer, ForeignKey('materials.id')),
    Column('supplier_id', Integer, ForeignKey('suppliers.id'))
)

class Material(Base):
    __tablename__ = 'materials'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    category = Column(String)
    cost_per_kg = Column(Float)
    tensile_strength = Column(Float)
    yield_strength = Column(Float)
    modulus = Column(Float)
    elongation = Column(Float)
    hardness = Column(Float)
    embodied_energy = Column(Float)
    co2_footprint = Column(Float)
    recyclability = Column(String)
    availability = Column(String)
    datasheet_url = Column(String)
    suppliers = relationship("Supplier", secondary=material_supplier, back_populates="materials")

class Supplier(Base):
    __tablename__ = 'suppliers'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    contact_email = Column(String)
    region = Column(String)
    is_local = Column(Boolean)
    materials = relationship("Material", secondary=material_supplier, back_populates="suppliers")
