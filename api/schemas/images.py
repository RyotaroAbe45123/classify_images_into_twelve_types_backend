from pydantic import BaseModel

from fastapi import UploadFile


class Image(BaseModel):
    image: UploadFile


class ImageResponse(BaseModel):
    image_type: int