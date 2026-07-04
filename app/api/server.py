from fastapi import FastAPI, status

from app.api.router import api_router

app = FastAPI(
    title="Invoice API",
    version="1.0.0",
)

@app.get('/', status_code=status.HTTP_200_OK)
def home():
    return {"message": "Invoice server is running..."}

app.include_router(api_router)

