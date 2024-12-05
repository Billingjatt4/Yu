import asyncio, logging, sys, os
from pyrogram import idle  
from CakeMusic import bot, app, call
from CakeMusic.plugins import ALL_MODULES

loop = asyncio.get_event_loop()

LOGGER = logging.getLogger("YukkiMusic")

async def main():
      LOGGER.info("✅ All Directories Updated.")
      

if __name__ == "__main__":
    loop.run_until_complete(main())
