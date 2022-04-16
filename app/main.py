import os
from fastapi import FastAPI

app = FastAPI(title="Wishlist API")

if os.environ["REMOTE_DEBUGGER"]:
    try:
        import ptvsd
        ptvsd.enable_attach(address=("0.0.0.0", 5678))
        print("\nAttached remote debugger on http://0.0.0.0:5678/")
    except Exception:
        raise Exception("Something went wrong - Could not attach the remote debugger")


@app.get("/")
async def root():
    return {"message": "Hello World"}
