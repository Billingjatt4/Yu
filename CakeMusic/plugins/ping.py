
# ping function

@bot.on_message(cdx("ping") & ~pyrofl.bot)
async def check_sping(client, message):
    start = datetime.now()
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    m = await message.reply_text("**🤖 Ping...!!**")
    await m.edit(f"**🤖 Pinged...!!\nLatency:** `{ms}` ms")
