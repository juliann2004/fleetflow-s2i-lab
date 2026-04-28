from fastapi import FastAPI
import socket

app = FastAPI()

@app.get("/")
def read_root():
    hostname = socket.gethostname()
    # Version 1.1 (Blue Environment)
    return {"version": "Blue (v1.1)", "pod": hostname}
