from fastapi import APIRouter


router = APIRouter()

@router.post("/image", tags=["images"], response_model=None)
async def classify_image_into_twelve_types(body):
    print(body)