import cv2
from fastapi import APIRouter, UploadFile
import numpy as np
from numpy import ndarray

import api.schemas.images as images_schema
from api.inference import classify_image


router = APIRouter()


@router.post("/image", tags=["images"], response_model=images_schema.ImageResponse)
# フロントからリクエストされたときの名前と一致する必要がある
# formData.append("image", file) -> image
async def upload(image: UploadFile):
    img_bytes: bytes = await image.read()
    img_ndarray: ndarray = np.frombuffer(img_bytes, np.uint8)
    img_decoded: ndarray = cv2.imdecode(img_ndarray, cv2.IMREAD_UNCHANGED)
    image_type: int = classify_image(img_decoded)
    return images_schema.ImageResponse(image_type=image_type)