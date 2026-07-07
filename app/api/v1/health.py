from fastapi import APIRouter

router = APIRouter(
    prefix="/health",
    tags=["Platform"],
)


@router.get("")
async def health():

    return {
        "status": "healthy",
        "service": "nativee-engine",
    }