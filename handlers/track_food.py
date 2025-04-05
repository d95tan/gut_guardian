from telegram import Update
from telegram.ext import ContextTypes

async def track_food(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print(update.message)
    await update.message.reply_text(f'Your message: {update.message.text}')