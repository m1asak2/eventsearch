import os
from fastapi import FastAPI
from routers import connpass
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
app.include_router(connpass.router)
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}


"https://connpass.com/search/?q=python&start_from=2021/01/04&start_to=2021/07/04&prefectures=osaka&prefectures=online&selectItem=osaka&selectItem=online"

"prefectures = tokyo"
"https://connpass.com/api/v1/event/?keyword=python&prefectures=tokyo&order=1&count=10"
