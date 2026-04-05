from pydantic import BaseModel, EmailStr, Field


class Item(BaseModel):

    RegionName: str
    CountryName: str

    ProductName: str
    CategoryName: str

    ProductListPrice: float = Field(..., gt=0)
    Profit: float

    CustomerName: str
    CustomerEmail: EmailStr

    OrderDate: str

    OrderItemQuantity: int = Field(..., gt=0)
    PerUnitPrice: float