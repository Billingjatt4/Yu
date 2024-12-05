# stats function

@bot.on_message(cdx(["stats"]) & ~pyrofl.private)
async def check_bot_stats(client, message):
    try:
        await message.delete()
    except:
        pass
    photo = START_IMAGE_URL
    caption = "**⏤͟͞ADITYA PLAYER STATS ༗**"
    buttons = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="🐬 Check Stats",
                    callback_data="check_stats",
                )
            ],
            [
                InlineKeyboardButton(
                    text="🗑️ Close",
                    callback_data="force_close",
                )
            ]
        ]
    )
    return await message.reply_photo(
        photo=photo,
        caption=caption,
        reply_markup=buttons,
    )
