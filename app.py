from fastapi import FastAPI

import socket
"Initialize CI/CD Pipeline"

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "FleetFlow CI/CD Online!"}
