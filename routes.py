from fastapi import APIRouter, Query
from models import Item
import services

router = APIRouter(
    prefix="/items",
    tags=["Items"]
)


@router.get("/")
def get_items(
    skip: int = Query(0),
    limit: int = Query(10),
    country: str | None = None
):
    return services.get_all_items(skip, limit, country)


@router.get("/{item_id}")
def get_item(item_id: int):
    return services.get_item(item_id)


@router.post("/")
def create_item(item: Item):
    return services.create_item(item)


@router.delete("/{item_id}")
def delete_item(item_id: int):
    return services.delete_item(item_id)