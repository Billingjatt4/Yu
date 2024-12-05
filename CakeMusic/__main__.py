import os, asyncio, importlib
from pathlib import Path 
from pyrogram import idle  
from CakeMusic import bot, app, call

loop = asyncio.get_event_loop()

async def main():
      plugins_path = Path("./plugins")  # Get the plugins directory
      plugin_files = [f.stem for f in plugins_path.glob("*.py") if f.is_file() and not f.stem.startswith("__")]

      for plugin in plugin_files:
          try:
             importlib.import_module(f"plugins.{plugin}")
             print(f"Successfully imported plugin: {plugin}")
          except Exception as e:
             print(f"Failed to import plugin: {plugin}. Error: {e}")

      await bot.start() 
      await app.start()
      await call.start() 
      await idle()
    
if __name__ == "__main__":
     print("Bot is starting...")
     main()
     print("All plugins imported successfully.")
     loop.run_until_complete(main())
      
