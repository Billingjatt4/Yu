import asyncio, sys, logging
from pyrogram import idle
from CakeMusic import bot
from CakeMusic.plugins.play import app, call

LOGGER = logging.getLogger("YukkiMusic")

loop = asyncio.get_event_loop()

async def main():
      
      await app.start()
      await idle()
    
if __name__ == "__main__":
    loop.run_until_complete(main())
    print("Bot is starting...")
       
