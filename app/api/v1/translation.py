from fastapi import APIRouter

router = APIRouter(
    prefix="/translation",
    tags=["Translation"],
)


@router.post("")
async def translate():

    return {
        "message": "Translation endpoint coming soon."
    }