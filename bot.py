from dotenv import load_dotenv
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

load_dotenv()  # Load environment variables from .env file
token = os.getenv("TELEGRAM_BOT_TOKEN")  # Replace "TOKEN" with the actual name of your token in the .env file

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def track_food(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print(update.message)
    await update.message.reply_text(f'Your message: {update.message.text}')

app = ApplicationBuilder().token(token=token).build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("track", track_food))

app.run_polling()