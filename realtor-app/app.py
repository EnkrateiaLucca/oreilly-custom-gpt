# /// script
# requires-python = ">=3.12"
# dependencies = ["fastapi", "uvicorn", "sqlalchemy", "jinja2"]
# ///
from pathlib import Path

import uvicorn
from fastapi import Depends, FastAPI, HTTPException, Request
from sqlalchemy import or_
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from sqlalchemy.orm import Session

from database import House, get_db, init_db

app = FastAPI(title="Realtor App")
app.mount("/static", StaticFiles(directory=Path(__file__).parent / "static"), name="static")
templates = Jinja2Templates(directory=Path(__file__).parent / "templates")


class HouseCreate(BaseModel):
    title: str
    price: float
    bedrooms: int
    bathrooms: int
    sqft: int
    address: str
    description: str = ""
    image_url: str = ""


class HouseUpdate(BaseModel):
    title: str | None = None
    price: float | None = None
    bedrooms: int | None = None
    bathrooms: int | None = None
    sqft: int | None = None
    address: str | None = None
    description: str | None = None
    image_url: str | None = None


# ─── HTML Pages ───────────────────────────────────────────


@app.get("/", response_class=HTMLResponse)
def customer_page(request: Request):
    return templates.TemplateResponse("customer.html", {"request": request})


@app.get("/agent", response_class=HTMLResponse)
def agent_page(request: Request):
    return templates.TemplateResponse("agent.html", {"request": request})


# ─── API Endpoints ────────────────────────────────────────


@app.get("/api/houses")
def list_houses(
    search: str = "",
    min_price: float | None = None,
    max_price: float | None = None,
    db: Session = Depends(get_db),
):
    query = db.query(House)

    if search:
        pattern = f"%{search}%"
        query = query.filter(
            or_(
                House.title.ilike(pattern),
                House.address.ilike(pattern),
                House.description.ilike(pattern),
            )
        )
    if min_price is not None:
        query = query.filter(House.price >= min_price)
    if max_price is not None:
        query = query.filter(House.price <= max_price)

    houses = query.order_by(House.created_at.desc()).all()
    return [
        {
            "id": h.id,
            "title": h.title,
            "price": h.price,
            "bedrooms": h.bedrooms,
            "bathrooms": h.bathrooms,
            "sqft": h.sqft,
            "address": h.address,
            "description": h.description,
            "image_url": h.image_url,
        }
        for h in houses
    ]


@app.post("/api/houses")
def create_house(house: HouseCreate, db: Session = Depends(get_db)):
    db_house = House(**house.model_dump())
    db.add(db_house)
    db.commit()
    db.refresh(db_house)
    return {"id": db_house.id, "message": "House created"}


@app.put("/api/houses/{house_id}")
def update_house(house_id: int, house: HouseUpdate, db: Session = Depends(get_db)):
    db_house = db.query(House).filter(House.id == house_id).first()
    if not db_house:
        raise HTTPException(status_code=404, detail="House not found")
    for field, value in house.model_dump(exclude_unset=True).items():
        setattr(db_house, field, value)
    db.commit()
    return {"message": "House updated"}


@app.delete("/api/houses/{house_id}")
def delete_house(house_id: int, db: Session = Depends(get_db)):
    db_house = db.query(House).filter(House.id == house_id).first()
    if not db_house:
        raise HTTPException(status_code=404, detail="House not found")
    db.delete(db_house)
    db.commit()
    return {"message": "House deleted"}


if __name__ == "__main__":
    init_db()
    uvicorn.run(app, host="0.0.0.0", port=8000)
