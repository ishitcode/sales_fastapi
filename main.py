from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from routes import router as item_router

app = FastAPI(
    title="Sales API",
    description="FastAPI backend using CSV dataset",
    version="1.0"
)

# Root endpoint
@app.get("/")
def home():
    return {"message": "FastAPI backend running"}


# Register item routes
app.include_router(item_router)


# Global exception handler
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"error": "Internal server error"}
    )