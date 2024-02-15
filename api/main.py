from fastapi import FastAPI, UploadFile
from starlette.middleware.cors import CORSMiddleware

from api.routers import images


app = FastAPI()
app.include_router(images.router)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# app.post("/upload")
# async def upload(file: UploadFile):
#     data = await file.read()
#     print(type(data))
#     return data.filename