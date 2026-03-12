import os
import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Читаем данные из переменных окружения
TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = os.getenv("ADMIN_ID")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    # Ответ пользователю
    await update.message.reply_text("Привет! Бот запущен и работает!")
    
    # Уведомление админу
    if ADMIN_ID:
        try:
            await context.bot.send_message(
                chat_id=int(ADMIN_ID), 
                text=f"🔔 Новый пользователь: {user.first_name} (ID: {user.id}) нажал /start"
            )
        except Exception as e:
            print(f"Ошибка отправки админу: {e}")

if __name__ == '__main__':
    if not TOKEN:
        print("Ошибка: BOT_TOKEN не найден!")
    else:
        application = ApplicationBuilder().token(TOKEN).build()
        application.add_handler(CommandHandler("start", start))
        print("Бот запущен...")
        application.run_polling()
