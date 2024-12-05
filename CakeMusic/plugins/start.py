from CakeMusic import bot
from CakeMusic.plugins.play import add_served_user, delete_cb_query, back_to_home_menu
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@bot.on_message(filters.command(["start", "help"]))
async def start_message_private(client, message):
    user_id = message.from_user.id
    mention = message.from_user.mention
    await add_served_user(user_id)
    if len(message.text.split()) > 1:
        name = message.text.split(None, 1)[1]
        if name[0:5] == "verify":
            pass
            
    else:
        caption = f"""**➻ Hello, {mention}

🥀 I am An ≽ Advanced ≽ High Quality
Bot, I Can Stream 🌿 Audio & Video In
Your ♚ Channel And Group.

🐬 Must Click ❥ Open Command List
Button ⋟ To Get More Info's 🦋 About
My All Commands.

💐 Feel Free ≽ To Use Me › And Share
With Your ☛ Other Friends.**"""
        buttons = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="🥀 Add Me In Your Chat ✨",
                        url=f"https://t.me/{bot.me.username}?startgroup=true",
                    )
                ],
                [
                    InlineKeyboardButton(
                        text="🌺 Open Command List 🌷",
                        callback_data="open_command_list",
                    )
                ],
            ]
        )
        if START_IMAGE_URL:
            try:
                return await message.reply_photo(
                    photo=START_IMAGE_URL, caption=caption, reply_markup=buttons
                )
            except Exception as e:
                LOGGER.info(f"🚫 Start Image Error: {e}")
                try:
                    return await message.reply_text(text=caption, reply_markup=buttons)
                except Exception as e:
                    LOGGER.info(f"🚫 Start Error: {e}")
                    return
        else:
            try:
                return await message.reply_text(text=caption, reply_markup=buttons)
            except Exception as e:
                LOGGER.info(f"🚫 Start Error: {e}")
                return




@bot.on_callback_query(filters.command("open_command_list"))
async def open_command_list_alert(client, query):
    caption = """**🥀 All Members Can Use:**
/play - Stream Only Audio On VC.
/vplay - Stream Audio With Video.

**👾 Only For Chat Admins:**
/pause - Pause Running Stream.
/resume - Resume Paused Stream.
/skip - Skip Current Stream To Next.
/end - Stop Current Running Stream.

**Note:** All Commands Will Work
Only in Channels/Groups."""
    buttons = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="🔙 Back",
                    callback_data="back_to_home",
                )
            ],
        ]
    )
    try:
        return await query.edit_message_text(text=caption, reply_markup=buttons)
    except Exception as e:
        LOGGER.info(f"🚫 Cmd Menu Error: {e}")
        return


@bot.on_callback_query(filters.command("back_to_home"))
async def back_to_home_menu(client, query):
    mention = query.from_user.mention
    caption = f"""**➻ Hello, {mention}

🥀 I am An ≽ Advanced ≽ High Quality
Bot, I Can Stream 🌿 Audio & Video In
Your ♚ Channel And Group.

🐬 Must Click ❥ Open Command List
Button ⋟ To Get More Info's 🦋 About
My All Commands.

💐 Feel Free ≽ To Use Me › And Share
With Your ☛ Other Friends.**"""
    buttons = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="🥀 Add Me In Your Chat ✨",
                    url=f"https://t.me/{bot.me.username}?startgroup=true",
                )
            ],
            [
                InlineKeyboardButton(
                    text="🌺 Open Command List 🌷",
                    callback_data="open_command_list",
                )
            ],
        ]
    )
    try:
        return await query.edit_message_text(text=caption, reply_markup=buttons)
    except Exception as e:
        LOGGER.info(f"🚫 Back Menu Error: {e}")
        return


@bot.on_callback_query(filters.command("force_close"))
async def delete_cb_query(client, query):
    try:
        return await query.message.delete()
    except Exception:
        return
