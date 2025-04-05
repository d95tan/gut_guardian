from telegram import Update
from telegram.ext import ContextTypes

PAIN_MESSAGE_MAP = {
    1: "Let's hope it doesn't get worse",
    2: "Let's hope it doesn't get worse",
    3: "Let's hope it doesn't get worse",
    4: "It's getting worse. Keep drinking lots of water and avoid spicy foods",
    5: "It's getting worse. Keep drinking lots of water and avoid spicy foods",
    6: "It's getting worse. Keep drinking lots of water and avoid spicy foods",
    7: "It's getting worse. Keep drinking lots of water and avoid spicy foods",
    8: "It's pretty bad. You should see a doctor",
    9: "It's pretty bad. You should see a doctor",
    10: "It's pretty bad. You should see a doctor"
}


async def track_symptoms(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print(update.message)
    try:
        #TODO: get symptoms
        #TODO: get pain level
        pain_level = int(update.message.text)
        if pain_level < 1 or pain_level > 10:
            raise ValueError
    except ValueError:
        await update.message.reply_text("Please enter a number between 1 and 10")
        return
        
    #TODO: save to db
    
    
    await update.message.reply_text(PAIN_MESSAGE_MAP[pain_level])