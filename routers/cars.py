from fastapi import APIRouter, Request, status, Body, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from models import CarBase, CarDB
from typing import Optional, List

router = APIRouter()

@router.get("/", response_description="List all cars")
async def list_all_cars(
    request: Request,
    min_price: int=0,
    max_price: int=100000,
    brand: Optional[str]=None
) -> List[CarDB]:
    query = {"price":{"$lt": max_price, "$gt": min_price}}
    
    if brand:
        query["brand"] = brand
    
    full_query = request.app.mongodb['cars1'].find(query).sort("_id", 1)
    
    results = [CarDB(**raw_car) async for raw_car in full_query]
    
    return results


@router.post("/", response_description="Add new car")
async def create_car(request: Request, car: CarBase = Body(...)):
    car = jsonable_encoder(car)
    new_car = await request.app.mongodb["cars1"].insert_one(car)
    created_car = await request.app.mongodb["cars1"].find_one({"_id": new_car.inserted_id})
    
    
@router.get("/{id}", response_description="Get a single car")
async def show_car(id: str, request: Request):
    if (car := await request.app.mongodb["cars1"].find_one({"_id": id})) is not None:
        return CarDB(**car)
    raise HTTPException(status_code=404, detail=f"Car with {id} not found")

