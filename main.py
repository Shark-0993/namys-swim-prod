import os
from fastapi import FastAPI
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8690330172:AAFyloVC0P9QCn9bUmHc5YC96HyB2tjiA2Y" # Твой токен здесь

app = FastAPI()

# Функция команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я бот NAMYS-SWIM. Я готов записывать детей на тренировки!")

# Настройка бота
application = ApplicationBuilder().token(TOKEN).build()
application.add_handler(CommandHandler("start", start))

@app.get("/")
async def root():
    return {"status": "Bot is running"}

# Запуск бота при старте FastAPI
@app.on_event("startup")
async def startup_event():
    await application.initialize()
    await application.start()
    await application.updater.start_polling()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=10000)


