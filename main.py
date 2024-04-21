from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"]
)

@app.get("/")
def get_public():
    return {"message": "Home"}

@app.get("/public")
def get_public():
    return {"message": "Ce endpoint est public"}

@app.options("/private")
def get_options():
    return {"message": "Ce endpoint est public"}


@app.get("/private")
def get_private():
    return {"message": "Ce endpoint est privé"}