import asyncio
from pyrogram import idle
from CakeMusic import bot
from CakeMusic.plugins.play import app, call


loop = asyncio.get_event_loop()

async def main():
      await bot.start() 
      await app.start()
      await call.start() 
      await idle()
    
if __name__ == "__main__":
   # loop.run_until_complete(main())
    print("Bot is starting...")
       
