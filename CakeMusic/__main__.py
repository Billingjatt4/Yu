import asyncio, logging
from pyrogram import idle  
from CakeMusic import bot, app, call
from CakeMusic.plugins import ALL_MODULES

loop = asyncio.get_event_loop()

LOGGER = logging.getLogger("YukkiMusic")

async def main():
      LOGGER.info("✅ All Directories Updated.")
      await asyncio.sleep(1)
      for all_module in ALL_MODULES:
          importlib.import_module("CakeMusic.plugins" + all_module)
      LOGGER.info("CakeMusic.plugins")
      await bot.start() 
      await app.start()
      await call.start() 
      await idle()

if __name__ == "__main__":
     print("Bot is starting...")
     loop.run_until_complete(main())
