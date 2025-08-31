from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.models.material import Material
from backend.schemas.material import MaterialCreate, MaterialOut
from backend.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/materials", response_model=MaterialOut)
def create_material(material: MaterialCreate, db: Session = Depends(get_db)):
    db_material = Material(**material.dict())
    db.add(db_material)
    db.commit()
    db.refresh(db_material)
    return db_material

@router.get("/materials", response_model=list[MaterialOut])
def list_materials(db: Session = Depends(get_db)):
    return db.query(Material).all()

@router.get("/materials/{material_id}", response_model=MaterialOut)
def get_material(material_id: int, db: Session = Depends(get_db)):
    mat = db.query(Material).filter(Material.id == material_id).first()
    if not mat:
        raise HTTPException(status_code=404, detail="Material not found")
    return mat

@router.put("/materials/{material_id}", response_model=MaterialOut)
def update_material(material_id: int, material: MaterialCreate, db: Session = Depends(get_db)):
    mat = db.query(Material).filter(Material.id == material_id).first()
    if not mat:
        raise HTTPException(status_code=404, detail="Material not found")
    for k, v in material.dict().items():
        setattr(mat, k, v)
    db.commit()
    db.refresh(mat)
    return mat

@router.delete("/materials/{material_id}")
def delete_material(material_id: int, db: Session = Depends(get_db)):
    mat = db.query(Material).filter(Material.id == material_id).first()
    if not mat:
        raise HTTPException(status_code=404, detail="Material not found")
    db.delete(mat)
    db.commit()
    return {"detail": "Deleted"}
