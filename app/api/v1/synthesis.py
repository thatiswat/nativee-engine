from fastapi import APIRouter

router = APIRouter(
    prefix="/synthesis",
    tags=["Synthesis"],
)


@router.post("")
async def synthesize():

    return {
        "message": "Synthesis endpoint coming soon."
    }