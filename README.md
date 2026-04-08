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

## Live Links
- **API**: https://zorvyn-backend-fianace.onrender.com
- **Swagger Docs**: https://zorvyn-backend-fianace.onrender.com/docs
- **Telegram Bot**: @ZorvynWealth_Bot (Mistral AI powered)

## Known Limitations
- Render free tier spins down after inactivity — first request may take 50+ seconds
- Telegram Bot commands like /register and /login call the Render API — if API is sleeping, these may fail. Visit the API URL first to wake it up, then use bot commands
- Mistral AI general finance questions work independently and are always available

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

## Environment Variables
```env
DATABASE_URL=postgresql://...
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
TELEGRAM_BOT_TOKEN=your-telegram-bot-token
MISTRAL_API_KEY=your-mistral-api-key
API_BASE=https://zorvyn-backend-fianace.onrender.com
```

## API Endpoints
| Method | Endpoint | Description | Auth |
|--------|----------|-------------|------|
| POST | /auth/register | Register user | No |
| POST | /auth/login | Login | No |
| POST | /records/ | Create record | Yes |
| GET | /records/ | Get all records | Yes |
| PUT | /records/{id} | Update record | Yes |
| DELETE | /records/{id} | Delete record | Yes |
| GET | /summary/ | Total summary | Yes |
| GET | /summary/categories | Category breakdown | Yes |
| GET | /summary/monthly | Monthly summary | Yes |
| GET | /users/me | Get profile | Yes |
| GET | /users/ | All users (admin) | Yes |

## Why Telegram Bot & AI?
The assignment required a backend system. I built that completely. But I also wanted to show real-world value — so I added a Telegram Bot powered by Mistral AI. This allows actual users to register, login, track expenses and get financial advice directly from Telegram without any technical knowledge.# Zorvyn Finance System Backend

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

## Live Links
- **API**: https://zorvyn-backend-fianace.onrender.com
- **Swagger Docs**: https://zorvyn-backend-fianace.onrender.com/docs
- **Telegram Bot**: @ZorvynWealth_Bot (Mistral AI powered)

## Known Limitations
- Render free tier spins down after inactivity — first request may take 50+ seconds
- Telegram Bot commands like /register and /login call the Render API — if API is sleeping, these may fail. Visit the API URL first to wake it up, then use bot commands
- Mistral AI general finance questions work independently and are always available

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

## Environment Variables
```env
DATABASE_URL=postgresql://...
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
TELEGRAM_BOT_TOKEN=your-telegram-bot-token
MISTRAL_API_KEY=your-mistral-api-key
API_BASE=https://zorvyn-backend-fianace.onrender.com
```

## API Endpoints
| Method | Endpoint | Description | Auth |
|--------|----------|-------------|------|
| POST | /auth/register | Register user | No |
| POST | /auth/login | Login | No |
| POST | /records/ | Create record | Yes |
| GET | /records/ | Get all records | Yes |
| PUT | /records/{id} | Update record | Yes |
| DELETE | /records/{id} | Delete record | Yes |
| GET | /summary/ | Total summary | Yes |
| GET | /summary/categories | Category breakdown | Yes |
| GET | /summary/monthly | Monthly summary | Yes |
| GET | /users/me | Get profile | Yes |
| GET | /users/ | All users (admin) | Yes |

## Why Telegram Bot & AI?
The assignment required a backend system. I built that completely. But I also wanted to show real-world value — so I added a Telegram Bot powered by Mistral AI. This allows actual users to register, login, track expenses and get financial advice directly from Telegram without any technical knowledge.# Zorvyn Finance System Backend

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

## Live Links
- **API**: https://zorvyn-backend-fianace.onrender.com
- **Swagger Docs**: https://zorvyn-backend-fianace.onrender.com/docs
- **Telegram Bot**: @ZorvynWealth_Bot (Mistral AI powered)

## Known Limitations
- Render free tier spins down after inactivity — first request may take 50+ seconds
- Telegram Bot commands like /register and /login call the Render API — if API is sleeping, these may fail. Visit the API URL first to wake it up, then use bot commands
- Mistral AI general finance questions work independently and are always available

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

## Environment Variables
```env
DATABASE_URL=postgresql://...
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
TELEGRAM_BOT_TOKEN=your-telegram-bot-token
MISTRAL_API_KEY=your-mistral-api-key
API_BASE=https://zorvyn-backend-fianace.onrender.com
```

## API Endpoints
| Method | Endpoint | Description | Auth |
|--------|----------|-------------|------|
| POST | /auth/register | Register user | No |
| POST | /auth/login | Login | No |
| POST | /records/ | Create record | Yes |
| GET | /records/ | Get all records | Yes |
| PUT | /records/{id} | Update record | Yes |
| DELETE | /records/{id} | Delete record | Yes |
| GET | /summary/ | Total summary | Yes |
| GET | /summary/categories | Category breakdown | Yes |
| GET | /summary/monthly | Monthly summary | Yes |
| GET | /users/me | Get profile | Yes |
| GET | /users/ | All users (admin) | Yes |

## Why Telegram Bot & AI?
The assignment required a backend system. I built that completely. But I also wanted to show real-world value — so I added a Telegram Bot powered by Mistral AI. This allows actual users to register, login, track expenses and get financial advice directly from Telegram without any technical knowledge.# Zorvyn Finance System Backend

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

## Live Links
- **API**: https://zorvyn-backend-fianace.onrender.com
- **Swagger Docs**: https://zorvyn-backend-fianace.onrender.com/docs
- **Telegram Bot**: @ZorvynWealth_Bot (Mistral AI powered)

## Known Limitations
- Render free tier spins down after inactivity — first request may take 50+ seconds
- Telegram Bot commands like /register and /login call the Render API — if API is sleeping, these may fail. Visit the API URL first to wake it up, then use bot commands
- Mistral AI general finance questions work independently and are always available

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

## Environment Variables
```env
DATABASE_URL=postgresql://...
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
TELEGRAM_BOT_TOKEN=your-telegram-bot-token
MISTRAL_API_KEY=your-mistral-api-key
API_BASE=https://zorvyn-backend-fianace.onrender.com
```

## API Endpoints
| Method | Endpoint | Description | Auth |
|--------|----------|-------------|------|
| POST | /auth/register | Register user | No |
| POST | /auth/login | Login | No |
| POST | /records/ | Create record | Yes |
| GET | /records/ | Get all records | Yes |
| PUT | /records/{id} | Update record | Yes |
| DELETE | /records/{id} | Delete record | Yes |
| GET | /summary/ | Total summary | Yes |
| GET | /summary/categories | Category breakdown | Yes |
| GET | /summary/monthly | Monthly summary | Yes |
| GET | /users/me | Get profile | Yes |
| GET | /users/ | All users (admin) | Yes |

## Why Telegram Bot & AI?
The assignment required a backend system. I built that completely. But I also wanted to show real-world value — so I added a Telegram Bot powered by Mistral AI. This allows actual users to register, login, track expenses and get financial advice directly from Telegram without any technical knowledge.# Zorvyn Finance System Backend

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

## Live Links
- **API**: https://zorvyn-backend-fianace.onrender.com
- **Swagger Docs**: https://zorvyn-backend-fianace.onrender.com/docs
- **Telegram Bot**: @ZorvynWealth_Bot (Mistral AI powered)

## Known Limitations
- Render free tier spins down after inactivity — first request may take 50+ seconds
- Telegram Bot commands like /register and /login call the Render API — if API is sleeping, these may fail. Visit the API URL first to wake it up, then use bot commands
- Mistral AI general finance questions work independently and are always available

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

## Environment Variables
```env
DATABASE_URL=postgresql://...
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
TELEGRAM_BOT_TOKEN=your-telegram-bot-token
MISTRAL_API_KEY=your-mistral-api-key
API_BASE=https://zorvyn-backend-fianace.onrender.com
```

## API Endpoints
| Method | Endpoint | Description | Auth |
|--------|----------|-------------|------|
| POST | /auth/register | Register user | No |
| POST | /auth/login | Login | No |
| POST | /records/ | Create record | Yes |
| GET | /records/ | Get all records | Yes |
| PUT | /records/{id} | Update record | Yes |
| DELETE | /records/{id} | Delete record | Yes |
| GET | /summary/ | Total summary | Yes |
| GET | /summary/categories | Category breakdown | Yes |
| GET | /summary/monthly | Monthly summary | Yes |
| GET | /users/me | Get profile | Yes |
| GET | /users/ | All users (admin) | Yes |

## Why Telegram Bot & AI?
The assignment required a backend system. I built that completely. But I also wanted to show real-world value — so I added a Telegram Bot powered by Mistral AI. This allows actual users to register, login, track expenses and get financial advice directly from Telegram without any technical knowledge.# Zorvyn Finance System Backend

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

## Live Links
- **API**: https://zorvyn-backend-fianace.onrender.com
- **Swagger Docs**: https://zorvyn-backend-fianace.onrender.com/docs
- **Telegram Bot**: @ZorvynWealth_Bot (Mistral AI powered)

## Known Limitations
- Render free tier spins down after inactivity — first request may take 50+ seconds
- Telegram Bot commands like /register and /login call the Render API — if API is sleeping, these may fail. Visit the API URL first to wake it up, then use bot commands
- Mistral AI general finance questions work independently and are always available

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

## Environment Variables
```env
DATABASE_URL=postgresql://...
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
TELEGRAM_BOT_TOKEN=your-telegram-bot-token
MISTRAL_API_KEY=your-mistral-api-key
API_BASE=https://zorvyn-backend-fianace.onrender.com
```

## API Endpoints
| Method | Endpoint | Description | Auth |
|--------|----------|-------------|------|
| POST | /auth/register | Register user | No |
| POST | /auth/login | Login | No |
| POST | /records/ | Create record | Yes |
| GET | /records/ | Get all records | Yes |
| PUT | /records/{id} | Update record | Yes |
| DELETE | /records/{id} | Delete record | Yes |
| GET | /summary/ | Total summary | Yes |
| GET | /summary/categories | Category breakdown | Yes |
| GET | /summary/monthly | Monthly summary | Yes |
| GET | /users/me | Get profile | Yes |
| GET | /users/ | All users (admin) | Yes |

## Why Telegram Bot & AI?
The assignment required a backend system. I built that completely. But I also wanted to show real-world value — so I added a Telegram Bot powered by Mistral AI. This allows actual users to register, login, track expenses and get financial advice directly from Telegram without any technical knowledge.