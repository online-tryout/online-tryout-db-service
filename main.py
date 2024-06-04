from fastapi import FastAPI
from auth.router import router as auth_router
from tryout.router import router as tryout_router
from payment.router import router as payment_router

app = FastAPI(docs_url="/api/db/docs"))

app.include_router(auth_router, prefix="/api/db/auth")
app.include_router(tryout_router, prefix="/api/db/tryout")
app.include_router(payment_router, prefix="/api/db/payment")

@app.get("/api/db/health")
async def main():
    return {"message" : "Hello World"}
