import os
import uvicorn
from fastapi import FastAPI
from telegram.ext import ApplicationBuilder, CommandHandler

app = FastAPI()
TOKEN = os.getenv("BOT_TOKEN")

async def start(update, context):
    await update.message.reply_text("Привет! Я бот NAMYS-SWIM!")

if TOKEN:
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))

    @app.on_event("startup")
    async def startup_event():
        await application.initialize()
        await application.start()
        await application.updater.start_polling()

@app.get("/")
async def root():
    return {"status": "Bot is running"}

if __name__ == "__main__":
    uvicorn.run("main_new:app", host="0.0.0.0", port=10000)
