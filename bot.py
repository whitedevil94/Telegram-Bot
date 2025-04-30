from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext

# Replace 'YOUR_API_TOKEN' with your actual bot token
API_TOKEN = '8078715278:AAESclosJfTVIxcQoZGhBRFqQMqlhkVQPBM'

# Function to handle /start command
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text(
        "Welcome to the Student Resource Bot! 🎓\n"
        "Here are the commands you can use:\n"
        "/links - Get useful links\n"
        "/pdfs - Access PDF resources\n"
        "/stop - Stop interacting with the bot"
    )

# Function to handle /links command
async def links(update: Update, context: CallbackContext):
    await update.message.reply_text(
        "📚 Useful Links:\n"
        "1. [Google](https://www.google.com)\n"
        "2. [Wikipedia](https://www.wikipedia.org)\n"
        "3. [Khan Academy](https://www.khanacademy.org)"
    )

# Function to handle /pdfs command
async def pdfs(update: Update, context: CallbackContext):
    await update.message.reply_text(
        "📂 PDF Resources:\n"
        "1. [Computer Science (OS)](https://os.ecci.ucr.ac.cr/slides/Abraham-Silberschatz-Operating-System-Concepts-10th-2018.pdf)\n"
        "2. [Programming Guide](https://codewithharry.com)\n"
        "3. [Physics Cheatsheet](https://udrc.lkouniv.ac.in//Content/DepartmentContent/SM_86bddd2a-7e9a-4c0d-984a-6b8668b0666c_37.pdf)"
    )

# Function to handle /stop command
async def stop(update: Update, context: CallbackContext):
    await update.message.reply_text("Goodbye! 👋 The bot is now stopping. Have a great day!")

# Main function to set up the bot
def main():
    # Create an Application instance using the bot token
    application = Application.builder().token(API_TOKEN).build()

    # Register command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("links", links))
    application.add_handler(CommandHandler("pdfs", pdfs))
    application.add_handler(CommandHandler("stop", stop))

    # Run the bot
    application.run_polling()

# Execute the program
if __name__ == "__main__":
    main()