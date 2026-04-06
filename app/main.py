from fastapi import FastAPI
from app.routers import auth, records, summary, users

app = FastAPI(
    title="Zorvyn Finance System Backend",
    description="""
Python based finance tracking Api

## Live Links
- **API Docs**: [Swagger UI](https://zorvyn-backend-fianace.onrender.com/docs)
- **Telegram Bot**: [ZorvynWealth Bot](https://t.me/ZorvynWealth_Bot)
- **GitHub**: [Source Code](https://github.com/dev200413y/zorvyn-finance-backend)
    """,
    version="1.0.0"
)

app.include_router(auth.router)
app.include_router(records.router)
app.include_router(summary.router)
app.include_router(users.router)

@app.get("/")
def health_check():
    return {
        "status": "running",
        "message": "Zorvyn Finance System Backend Api is live",
        "docs": "https://zorvyn-backend-fianace.onrender.com/docs",
        "telegram_bot": "https://t.me/ZorvynWealth_Bot",
        "github": "https://github.com/dev200413y/zorvyn-finance-backend"
    }