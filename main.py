from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from flight_search import search_flights
from config import TELEGRAM_BOT_TOKEN

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome! Use /find ORIGIN DEST YYYY-MM-DD to search business class flights.")

async def find(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        origin, dest, date = context.args
        results = search_flights(origin, dest, date)
        for r in results:
            await update.message.reply_text(r)
    except Exception as e:
        await update.message.reply_text(f"Error: {e}\nExample: /find LAX JFK 2025-06-10")

def main():
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("find", find))
    print("Bot running...")
    app.run_polling()

if __name__ == "__main__":
    main()
