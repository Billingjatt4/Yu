import asyncio
from CakeMusic import bot
from CakeMusic.plugins.play import app, call

async def main():
      try:
          await call.start()
          await bot.start() 
          await app.start() 


# Run the bot
if __name__ == "__main__":
    print("Bot is starting...")
