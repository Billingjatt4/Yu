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
    

if __name__ == "__main__":
     print("Bot is starting...")
     loop.run_until_complete(main())
