from fastapi import FastAPI
from auth.router import router as auth_router
from tryout.router import router as tryout_router

app = FastAPI()

app.include_router(auth_router, prefix="/api/auth")
app.include_router(tryout_router, prefix="/api/db/tryout")

@app.get("/api/auth/health")
async def main():
    return {"message" : "Hello World"}
