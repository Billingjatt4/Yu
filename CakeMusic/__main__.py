from pyrogram import Client, filters
from pyrogram.types import Message
import logging
import os
import asyncio
from pyrogram import idle
from CakeMusic import bot, app, call

loop = asyncio.get_event_loop()

async def main():
      # Run Bot
      await bot.start()  
      # Run Assistant
      await app.start() 
      # Run Py-TgCalls
      await call.start() 
      # Make client On
      await idle() 
    



# Enable logging to view errors
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(bot)


# List of plugins to be imported
PLUGIN_DIR = "CakeMusic/plugins"
PLUGIN_LIST = []

# Load the plugins dynamically from the specified plugin directory
def load_plugins():
    try:
        for filename in os.listdir(PLUGIN_DIR):
            if filename.endswith(".py"):
                plugin_name = filename[:-3]  # Remove '.py' extension
                try:
                    __import__(f"{PLUGIN_DIR}.{plugin_name}")
                    PLUGIN_LIST.append(plugin_name)
                    logger.info(f"Plugin {plugin_name} imported successfully.")
                except Exception as e:
                    logger.error(f"Failed to import plugin {plugin_name}: {e}")
        if PLUGIN_LIST:
            send_init_message()
        else:
            logger.warning("No plugins were loaded.")
    except Exception as e:
        logger.error(f"Error loading plugins: {e}")

# Send a confirmation message to the bot when all plugins are loaded
def send_init_message():
    try:
        bot.send_message(
            chat_id="-1002356967761",  # Replace with the chat ID or channel
            text="All plugins have been imported successfully, and the bot is ready to work!"
        )
        logger.info("Initialization message sent successfully.")
    except Exception as e:
        logger.error(f"Failed to send initialization message: {e}")

# Handler for starting the bot
@bot.on_message(filters.command("start"))
def start(client: Client, message: Message):
    message.reply("Bot is running with the plugins successfully loaded!")

# Main function to start the bot and load plugins
def main():
    load_plugins()
    bot.run()

if __name__ == "__main__":
     print("Bot is starting...")
     loop.run_until_complete(main())
