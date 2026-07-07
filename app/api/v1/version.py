from fastapi import APIRouter

router = APIRouter(
    prefix="/version",
    tags=["Platform"],
)


@router.get("")
async def version():

    return {
        "service": "nativee-engine",
        "version": "1.0.0",
        "providers": {
            "speech": "groq",
            "translation": "google",
            "voice": "edge",
        },
    }