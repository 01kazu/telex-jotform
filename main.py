from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from integration_conf import router as integration_router
from webhook import router as webhook_router
from config import settings

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(integration_router, prefix=settings.API_PREFIX)
app.include_router(webhook_router, prefix=settings.API_PREFIX)


@app.get("/healthcheck")
async def health_check():
    """Checks if server is active."""
    return {"status": "active"}