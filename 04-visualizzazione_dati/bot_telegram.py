from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
from datetime import datetime 
import csv

async def get_location(update, context: ContextTypes.DEFAULT_TYPE): 
    msg = update.edited_message if update.edited_message else update.message

    if msg.location:
        gps = msg.location 
        sender = msg.from_user.username
        tm = datetime.now().strftime("%H:%M:%S")

        with open('LOG.CSV', 'a', newline='') as f: 
            writer = csv.writer(f) 
            writer.writerow([sender, gps.latitude, gps.longitude, tm])
        await context.bot.send_message(chat_id=msg.chat.id, text=f"Coordinate:\nLatitudine: {gps.latitude}, Longitudine: {gps.longitude}") 

def main():
    app = ApplicationBuilder().token('TOKEN TELEGRAM PERSONALE').build()
    app.add_handler(MessageHandler(filters.LOCATION, get_location))
    app.run_polling()

if __name__ == '__main__':
    print('BOT in funzione')
    main()
