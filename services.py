from fastapi import HTTPException
from data_loader import load_dataset

data = load_dataset()


def get_all_items(skip=0, limit=10, country=None):

    # skip validation
    if skip < 0:
        raise HTTPException(
            status_code=400,
            detail="skip must be >= 0"
        )

    # limit validation
    if limit <= 0 or limit > 100:
        raise HTTPException(
            status_code=400,
            detail="limit must be between 1 and 100"
        )

    result = data

    # country filter
    if country:

        filtered = [
            item for item in result
            if item["CountryName"].lower() == country.lower()
        ]

        if len(filtered) == 0:
            raise HTTPException(
                status_code=404,
                detail=f"No records found for country '{country}'"
            )

        result = filtered

    return result[skip: skip + limit]


def get_item(item_id):

    if item_id < 0:
        raise HTTPException(
            status_code=400,
            detail="item_id must be positive"
        )

    if item_id >= len(data):
        raise HTTPException(
            status_code=404,
            detail="Item not found"
        )

    return data[item_id]


def create_item(item):

    # business rule: profit cannot exceed price
    if item.Profit > item.ProductListPrice:
        raise HTTPException(
            status_code=400,
            detail="Profit cannot exceed product price"
        )

    # quantity rule
    if item.OrderItemQuantity > 1000:
        raise HTTPException(
            status_code=400,
            detail="Order quantity too large"
        )

    data.append(item.dict())

    return {
        "message": "Item added successfully",
        "total_items": len(data)
    }


def delete_item(item_id):

    if item_id < 0:
        raise HTTPException(
            status_code=400,
            detail="Invalid item_id"
        )

    if item_id >= len(data):
        raise HTTPException(
            status_code=404,
            detail="Item not found"
        )

    deleted = data.pop(item_id)

    return {
        "message": "Item deleted successfully",
        "deleted_item": deleted
    }