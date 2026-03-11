import os
from fastapi import FastAPI
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

app = FastAPI()

# Используем токен из настроек Render (безопаснее всего)
TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я бот NAMYS-SWIM. Я готов записывать детей на тренировки!")

if TOKEN:
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    
    # Запуск бота в фоновом режиме
    @app.on_event("startup")
    async def startup_event():
        await application.initialize()
        await application.start()
        await application.updater.start_polling()

@app.get("/")
async def root():
    return {"status": "Bot is running"}
