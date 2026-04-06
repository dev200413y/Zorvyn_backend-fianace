#!/bin/bash
python -m alembic upgrade head
python app/telegram_bot.py &
uvicorn app.main:app --host 0.0.0.0 --port 8000