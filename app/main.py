from fastapi import FastAPI
from app.routers import auth, records, summary, users
app = FastAPI(
    title="Zorvyn Finance System Backend",
    description="python based finance tracking Api",
    version="1.0.0"
)
app.include_router(auth.router)
app.include_router(records.router)
app.include_router(summary.router)
app.include_router(users.router)
@app.get("/")
def health_check():
    return { "status":"running","message":"Zorvyn Finance System Backend Api is live "}