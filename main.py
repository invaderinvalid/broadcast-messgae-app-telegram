import os
from telegram import Update
from telegram.ext import Application, CommandHandler
from dotenv import load_dotenv
import utils
from handlers import start, ping, info, broadcast

load_dotenv()

TOKEN =os.getenv('BOT_TOKEN')



def main() -> None:
    # Setup database
    print("Setting up Database ........\n")
    utils.setup_database()
    print("Database setup completed......")

    # Create application
    application = Application.builder().token(TOKEN).build()
    print("Application build status..... SUCCESS\n\n\n")
    # Add handlers
    print("Adding Handelers ... \n\n\n")
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("ping", ping))
    application.add_handler(CommandHandler("info", info))
    application.add_handler(CommandHandler("broadcast", broadcast))
    print("Task Completed .... \n\n\n\n\n\n\n")
    print("Everything went well BOT IS UP!")
    application.run_polling(allowed_updates=Update.ALL_TYPES)
    
if __name__ == '__main__':
    main()