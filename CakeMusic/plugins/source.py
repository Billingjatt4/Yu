# source code function

@bot.on_message(cdx(["repo", "repository"]) & ~pyrofl.bot)
async def git_repo_link(client, message):
    if message.sender_chat:
        mention = message.sender_chat.title
    else:
        mention = message.from_user.mention
    if message.chat.type == ChatType.PRIVATE:
        caption = f"""**➻ Hello, {mention}
    
🥀 I am An ≽ Advanced ≽ High Quality
Bot, I Can Stream 🌿 Audio & Video In
Your ♚ Channel And Group.

🐬 Feel Free ≽ To Use Me › And Share
With Your ☛ Other Friends.**"""
    else:
        caption = f"**➻ Hello, {mention}.**"
    buttons = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="🌺 Open Repository Link 🦋",
                    url="https://github.com/AdityaHalder/AdityaPlayer",
                )
            ],
            [
                InlineKeyboardButton(
                    text="🗑️ Close",
                    callback_data="force_close",
                )
            ],
        ]
    )
    try:
        await message.reply_photo(
            photo=START_IMAGE_URL, caption=caption, reply_markup=buttons
        )
    except Exception as e:
        LOGGER.info(f"🚫 Error: {e}")
        return
