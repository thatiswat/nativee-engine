from fastapi import FastAPI

from app.api.v1.conversation import router as conversation_router
from app.api.v1.health import router as health_router
from app.api.v1.speech import router as speech_router
from app.api.v1.synthesis import router as synthesis_router
from app.api.v1.translation import router as translation_router
from app.api.v1.version import router as version_router

app = FastAPI(
    title="Nativee Engine",
    version="1.0.0",
)

# ==========================================================
# Platform
# ==========================================================

app.include_router(
    health_router,
)

app.include_router(
    version_router,
)

# ==========================================================
# Engine
# ==========================================================

app.include_router(
    conversation_router,
)

app.include_router(
    speech_router,
)

app.include_router(
    translation_router,
)

app.include_router(
    synthesis_router,
)