from fastapi import APIRouter

router = APIRouter(
    prefix="/speech",
    tags=["Speech"],
)


@router.post("/transcribe")
async def transcribe():

    return {
        "message": "Speech endpoint coming soon."
    }