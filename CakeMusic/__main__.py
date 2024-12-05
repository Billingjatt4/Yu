import asyncio
from pyrogram import idle  
from CakeMusic import bot, app, call
from CakeMusic.plugins import ALL_MODULES

#loop = asyncio.get_event_loop()

def main():
      for all_module in ALL_MODULES:
        importlib.import_module("CakeMusic.plugins" + all_module)
      bot.start() 
      app.start()
      call.start() 
      idle()
    
if __name__ == "__main__":
   #  print("Bot is starting...")
    # print("All plugins imported successfully.")
    # loop.run_until_complete(main())
     main()
