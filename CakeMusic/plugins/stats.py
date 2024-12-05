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


@bot.on_callback_query(rgx("check_stats"))
async def check_total_stats(client, query):
    try:
        user_id = query.from_user.id
        runtime = __start_time__
        boot_time = int(time.time() - runtime)
        uptime = get_readable_time((boot_time))
        served_chats = len(await get_served_chats())
        served_users = len(await get_served_users())
        activ_chats = len(ACTIVE_MEDIA_CHATS)
        audio_chats = len(ACTIVE_AUDIO_CHATS)
        video_chats = len(ACTIVE_VIDEO_CHATS)
        
        return await query.answer(
            f"""⏱️ Bot Run Time [Boot]
☛ {uptime}

🔴 Served Chats: {served_chats}
🔵 Served Users: {served_users}

🦋 Total Active Chats [{activ_chats}]
✿⋟ Audio Stream: {audio_chats}
✿⋟ Video Stream: {video_chats}""",
            show_alert=True
        )
    except Exception as e:
        LOGGER.info(f"🚫 Stats Error: {e}")
        pass
