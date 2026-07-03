from fastapi import APIRouter

router = APIRouter(
    prefix="/health",
    tags=["Health"],
)


@router.get("")
async def health():

    return {
        "status": "healthy",
        "engine": "nativeee-engine",
        "version": "1.0.0",
    }