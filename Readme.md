# FastAPI CSV Backend API

This project is a **FastAPI backend application** that loads a CSV dataset using **Pandas** and exposes it as a **REST API**.

The dataset is treated as an **in-memory database**, allowing you to perform basic CRUD operations.

---

# Features

* FastAPI REST APIs
* CSV dataset as data source
* Pydantic request validation
* Business logic validation
* Pagination support (`skip`, `limit`)
* Filtering by `country`
* Global exception handling
* Swagger UI API testing

---

# Project Structure

```
fastapi/
│
├── main.py
├── routes.py
├── services.py
├── models.py
├── data_loader.py
├── requirements.txt
│
└── dataset/
      ML-Dataset.csv
```

---

# Requirements

Install dependencies:

```
pip install -r requirements.txt
```

Dependencies include:

* fastapi
* uvicorn
* pandas
* pydantic
* python-multipart
* email-validator

---

# Running the Application

Start the FastAPI server:

```
python -m uvicorn main:app --reload --port 8001
```

Server will run at:

```
http://127.0.0.1:8001
```

---

# API Documentation

Swagger UI:

```
http://127.0.0.1:8001/docs
```

Alternative documentation:

```
http://127.0.0.1:8001/redoc
```

---

# API Endpoints

## Get All Items

```
GET /items
```

Example:

```
http://127.0.0.1:8001/items
```

Pagination:

```
http://127.0.0.1:8001/items?skip=0&limit=5
```

Filter by country:

```
http://127.0.0.1:8001/items?country=India
```

---

## Get Item By ID

```
GET /items/{item_id}
```

Example:

```
http://127.0.0.1:8001/items/1
```

Response Example:

```
{
  "RegionName": "Asia",
  "CountryName": "India",
  "ProductName": "Laptop",
  "CategoryName": "Electronics"
}
```

---

## Create Item

```
POST /items
```

Example Request Body:

```
{
  "RegionName": "Asia",
  "CountryName": "India",
  "ProductName": "Laptop",
  "CategoryName": "Electronics",
  "ProductListPrice": 1000,
  "Profit": 200,
  "CustomerName": "Rahul",
  "CustomerEmail": "rahul@example.com",
  "OrderDate": "2024-01-01",
  "OrderItemQuantity": 2,
  "PerUnitPrice": 1000
}
```

Example Response:

```
{
  "message": "Item added successfully",
  "total_items": 401
}
```

---

## Delete Item

```
DELETE /items/{item_id}
```

Example:

```
DELETE http://127.0.0.1:8001/items/3
```

Response Example:

```
{
  "message": "Item deleted successfully"
}
```

---

# Error Handling

Example: Invalid item ID

```
GET /items/9999
```

Response:

```
{
  "detail": "Item not found"
}
```

Example: Invalid request body

```
POST /items
```

```
{
  "ProductListPrice": -100
}
```

Response:

```
{
  "detail": [
    {
      "msg": "ensure this value is greater than 0"
    }
  ]
}
```

---

# Business Logic Rules

The API enforces the following validations:

* Product price must be greater than 0
* Order quantity must be greater than 0
* Profit cannot exceed product price
* Email must be valid
* `skip` must be ≥ 0
* `limit` must be between 1 and 100
* Invalid country returns `404`

---

# Development Notes

The CSV dataset is loaded into memory using **Pandas**:

```
df = pd.read_csv("dataset/ML-Dataset.csv")
data = df.to_dict(orient="records")
```

This allows the dataset to behave like a simple **in-memory database**.

---

# Future Improvements

Possible enhancements:

* PostgreSQL database integration
* SQLAlchemy ORM
* Redis caching
* Authentication with JWT
* Docker containerization
* Analytics APIs

---

# Author

Backend API built using **FastAPI + Pandas**.
