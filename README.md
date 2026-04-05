# Zorvyn Finance System Backend

A Python-based Finance Tracking System with Telegram Bot integration, built with FastAPI, PostgreSQL, Docker, and Jenkins CI/CD.

## Tech Stack
- FastAPI
- PostgreSQL
- SQLAlchemy + Alembic
- JWT Authentication
- Mistral AI (Finance Assistant)
- Telegram Bot
- Docker + Docker Compose
- Jenkins CI/CD
- Pytest

## Features
- User registration and login with JWT
- Income and expense tracking
- Financial summary and analytics
- Category-wise breakdown
- Monthly summary reports
- AI-powered finance assistant via Telegram
- Role-based access (Viewer/Admin)

## Setup & Run

### Without Docker
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### With Docker
```bash
docker-compose up --build
```

### Telegram Bot
```bash
python app/telegram_bot.py
```

## Telegram Bot Commands
| Command | Description |
|---------|-------------|
| /start | Start the bot |
| /register username email password | Create account |
| /login email password | Login |
| /balance | Check financial summary |
| /summary | Monthly breakdown |
| /add type amount category | Add record |

## API Endpoints
| Method | Endpoint | Description | Auth |
|--------|----------|-------------|------|
| POST | /auth/register | Register user | No |
| POST | /auth/login | Login | No |
| POST | /records/ | Create record | Yes |
| GET | /records/ | Get all records | Yes |
| GET | /records/{id} | Get one record | Yes |
| PUT | /records/{id} | Update record | Yes |
| DELETE | /records/{id} | Delete record | Yes |
| GET | /summary/ | Total summary | Yes |
| GET | /summary/categories | Category breakdown | Yes |
| GET | /summary/monthly | Monthly summary | Yes |
| GET | /users/me | Get profile | Yes |
| PUT | /users/me | Update profile | Yes |
| GET | /users/ | All users (admin) | Yes |

## Environment Variables
```env
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/finance_db
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
TELEGRAM_BOT_TOKEN=telegram-bot-token
MISTRAL_API_KEY=mistral-api-key
```

## API Documentation
Visit `http://localhost:8000/docs` for Swagger UI.

## Why Telegram Bot & AI?

The assignment required a backend system. We built that — but we went one step further.

### Telegram Bot
Instead of only exposing API endpoints, we added a Telegram Bot so real users can interact with the system without needing Postman or any technical knowledge. Anyone can register, login, add expenses, and check their balance directly from Telegram.

### Mistral AI
Numbers alone are not enough.as ai is need in every software therefore, i integrated Mistral AI so users can ask natural language questions like "how should I manage my budget?" and get intelligent responses — making this a smart finance assistant, not just a data store

### The Bigger Picture
This project is not just an assignment submission. It is a production-ready finance management system that real users can actually use.