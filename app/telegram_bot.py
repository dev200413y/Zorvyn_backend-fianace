import os
import httpx
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from mistralai.client import Mistral
from dotenv import load_dotenv

load_dotenv()

client = Mistral(api_key=os.getenv("MISTRAL_API_KEY"))
#fastapi backend ka base url
API_BASE = "http://127.0.0.1:8000"

#fastapi backend base url 
user_tokens = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hello! I am ZorvynWealth Bot 🤖\n\n"
        "Commands:\n"
        "/register - Create new account\n"
        "/login - Login to your account\n"
        "/balance - Check your balance\n"
        "/summary - Monthly summary\n"
        "/add - Add income or expense\n"
        "/help - View all commands\n\n"
        "Or ask me any finance question!"
    )

async def register(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) < 3:
        await update.message.reply_text(
            "Usage: /register username email password\n"
            "Example: /register dev dev@test.com test1234"
        )
        return
    username, email, password = context.args[0], context.args[1], context.args[2]
    async with httpx.AsyncClient() as http:
        response = await http.post(f"{API_BASE}/auth/register", json={
            "username": username,
            "email": email,
            "password": password
        })
    if response.status_code == 200:
        await update.message.reply_text("Account created successfully! Use /login to login.")
    elif response.status_code == 400:
        detail = response.json().get("detail", "Registration failed")
        await update.message.reply_text(f"Registration failed: {detail}")
    else:
        await update.message.reply_text("Registration failed: Username or email already exists.")
async def login(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) < 2:
        await update.message.reply_text(
            "Usage: /login email password\n"
            "Example: /login dev@test.com test1234"
        )
        return
    email, password = context.args[0], context.args[1]
    async with httpx.AsyncClient() as http:
        response = await http.post(f"{API_BASE}/auth/login", json={
            "email": email,
            "password": password
        })
    if response.status_code == 200:
        token = response.json()["access_token"]
        user_tokens[update.effective_user.id] = token
        await update.message.reply_text("Login successful! Welcome to ZorvynWealth 🎉")
    else:
        await update.message.reply_text("Login failed. Check your email and password.")

#balance fetch karta hai fastapi summary endpoint se 
async def balance(update: Update, context: ContextTypes.DEFAULT_TYPE):
    token = user_tokens.get(update.effective_user.id)
    if not token:
        await update.message.reply_text("Please login first using /login email password")
        return
    async with httpx.AsyncClient() as http:
        response = await http.get(f"{API_BASE}/summary/", headers={"Authorization": f"Bearer {token}"})
    if response.status_code == 200:
        data = response.json()
        await update.message.reply_text(
            f"💰 Your Financial Summary:\n\n"
            f"Total Income: ₹{data['total_income']}\n"
            f"Total Expense: ₹{data['total_expense']}\n"
            f"Balance: ₹{data['balance']}"
        )
    else:
        await update.message.reply_text("Could not fetch balance. Please try again.")

async def summary(update: Update, context: ContextTypes.DEFAULT_TYPE):
    token = user_tokens.get(update.effective_user.id)
    if not token:
        await update.message.reply_text("Please login first using /login email password")
        return
    async with httpx.AsyncClient() as http:
        response = await http.get(f"{API_BASE}/summary/monthly", headers={"Authorization": f"Bearer {token}"})
    if response.status_code == 200:
        data = response.json()
        if not data:
            await update.message.reply_text("No records found yet. Add some records first!")
            return
        msg = "📊 Monthly Summary:\n\n"
        for item in data:
            msg += f"{item['month'][:7]} | {item['type']} | ₹{item['total']}\n"
        await update.message.reply_text(msg)
    else:
        await update.message.reply_text("Could not fetch summary. Please try again.")

async def add_record(update: Update, context: ContextTypes.DEFAULT_TYPE):
    token = user_tokens.get(update.effective_user.id)
    if not token:
        await update.message.reply_text("Please login first using /login email password")
        return
    if len(context.args) < 3:
        await update.message.reply_text(
            "Usage: /add type amount category\n"
            "Example: /add expense 500 food\n"
            "Example: /add income 5000 salary"
        )
        return
    record_type, amount, category = context.args[0], context.args[1], context.args[2]
    from datetime import datetime
    async with httpx.AsyncClient() as http:
        response = await http.post(
            f"{API_BASE}/records/",
            headers={"Authorization": f"Bearer {token}"},
            json={
                "type": record_type,
                "amount": float(amount),
                "category": category,
                "date": datetime.utcnow().isoformat()
            }
        )
    if response.status_code == 200:
        await update.message.reply_text(f"Record added successfully!\n{record_type.title()} of ₹{amount} in {category}")
    else:
        await update.message.reply_text("Could not add record. Please try again.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    response = client.chat.complete(
        model="mistral-small-latest",
        messages=[
            {
                "role": "system",
                "content": "You are a personal finance assistant. Give short, helpful and clear responses in English only."
            },
            {
                "role": "user",
                "content": user_message
            }
        ]
    )
    await update.message.reply_text(response.choices[0].message.content)

def main():
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    app = Application.builder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("register", register))
    app.add_handler(CommandHandler("login", login))
    app.add_handler(CommandHandler("balance", balance))
    app.add_handler(CommandHandler("summary", summary))
    app.add_handler(CommandHandler("add", add_record))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("ZorvynWealth Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()