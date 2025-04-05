from dotenv import load_dotenv
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

from handlers.track_food import track_food
from handlers.track_symptoms import track_symptoms


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

def main():
    
    load_dotenv()  # Load environment variables from .env file
    token = os.getenv("TELEGRAM_BOT_TOKEN")  # Replace "TOKEN" with the actual name of your token in the .env file
    
    app = ApplicationBuilder().token(token=token).build()

    # Register command handlers
    app.add_handler(CommandHandler("hello", hello))
    app.add_handler(CommandHandler("food", track_food))
    app.add_handler(CommandHandler("symptoms", track_symptoms))

    app.run_polling()
    
if __name__ == "__main__":
    main()