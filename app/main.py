from fastapi import FastAPI

app = FastAPI(title="Wishlist API")

@app.get("/")
async def root():
    return {"message": "Hello World"}
