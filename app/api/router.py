from fastapi import APIRouter

from app.api.routes.invoice_routes import router as invoice_router

api_router = APIRouter()

api_router.include_router(invoice_router)