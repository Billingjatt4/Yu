import asyncio, sys, logging
from pyrogram import idle
from CakeMusic import bot
from CakeMusic.plugins.play import app, call

LOGGER = logging.getLogger("YukkiMusic")

async def main():
      try:
          await call.start()
          await bot.start() 
          await app.start() 
      except Exception:
          pass
      LOGGER.info("✅ Bot Started.")

# Run the bot
if __name__ == "__main__":
    print("Bot is starting...")
