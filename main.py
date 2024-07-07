import uvicorn
from fastapi import FastAPI
from routes.authorRoutes import router as author_router # type: ignore
from database import mongodb

app = FastAPI()

# Include routers
app.include_router(author_router)

# Startup and shutdown events
@app.on_event("startup")
async def startup_db_client():
    await mongodb.connect()

@app.on_event("shutdown")
async def shutdown_db_client():
    await mongodb.close()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
