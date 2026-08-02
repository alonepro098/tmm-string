from asyncio.exceptions import TimeoutError
from Data import Data
from pyrogram import Client, filters
from telethon import TelegramClient
from telethon.sessions import StringSession
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import (
    ApiIdInvalid,
    PhoneNumberInvalid,
    PhoneCodeInvalid,
    PhoneCodeExpired,
    SessionPasswordNeeded,
    PasswordHashInvalid,
)
from telethon.errors import (
    ApiIdInvalidError,
    PhoneNumberInvalidError,
    PhoneCodeInvalidError,
    PhoneCodeExpiredError,
    SessionPasswordNeededError,
    PasswordHashInvalidError,
)


@Client.on_message(filters.private & ~filters.forwarded & filters.command(["generate", "gen"]))
async def main(_, msg):
    await msg.reply(
        "**Please choose the Telegram library for string session generation:**",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("🧑‍💻 Pyrogram V2", callback_data="pyrogram"),
                    InlineKeyboardButton("⚡ Telethon", callback_data="telethon"),
                ]
            ]
        ),
    )


async def generate_session(bot, msg, telethon=False):
    lib_name = "Telethon" if telethon else "Pyrogram v2"
    await msg.reply(f"🚀 **Starting {lib_name} Session Generation...**")
    user_id = msg.chat.id

    api_id_msg = await bot.ask(
        user_id, "📱 **Please send your `API_ID`:**\n\n*(Send /cancel to abort)*", filters=filters.text
    )
    if await cancelled(api_id_msg):
        return
    try:
        api_id = int(api_id_msg.text.strip())
    except ValueError:
        await api_id_msg.reply(
            "❌ **Invalid API_ID.** It must be an integer.\nPlease start again.",
            quote=True,
            reply_markup=InlineKeyboardMarkup(Data.generate_button),
        )
        return

    api_hash_msg = await bot.ask(
        user_id, "🔑 **Please send your `API_HASH`:**\n\n*(Send /cancel to abort)*", filters=filters.text
    )
    if await cancelled(api_hash_msg):
        return
    api_hash = api_hash_msg.text.strip()

    phone_number_msg = await bot.ask(
        user_id,
        "📞 **Please send your `PHONE_NUMBER` with Country Code:**\n\n*Example:* `+19876543210`\n*(Send /cancel to abort)*",
        filters=filters.text,
    )
    if await cancelled(phone_number_msg):
        return
    phone_number = phone_number_msg.text.strip()

    await msg.reply("📲 **Sending OTP code to your Telegram account...**")

    if telethon:
        client = TelegramClient(StringSession(), api_id, api_hash)
    else:
        client = Client(name="user_session", api_id=api_id, api_hash=api_hash, in_memory=True)

    await client.connect()
    try:
        if telethon:
            code = await client.send_code_request(phone_number)
        else:
            code = await client.send_code(phone_number)
    except (ApiIdInvalid, ApiIdInvalidError):
        await msg.reply(
            "❌ **API_ID and API_HASH combination is invalid.**\nPlease try again.",
            reply_markup=InlineKeyboardMarkup(Data.generate_button),
        )
        await client.disconnect()
        return
    except (PhoneNumberInvalid, PhoneNumberInvalidError):
        await msg.reply(
            "❌ **PHONE_NUMBER is invalid.**\nPlease try again.",
            reply_markup=InlineKeyboardMarkup(Data.generate_button),
        )
        await client.disconnect()
        return
    except Exception as e:
        await msg.reply(f"❌ **Error:** `{str(e)}`")
        await client.disconnect()
        return

    try:
        phone_code_msg = await bot.ask(
            user_id,
            "💬 **Please check for the OTP in your official Telegram account.**\n\n"
            "If OTP is `12345`, **please send it as** `1 2 3 4 5` (with spaces).\n\n"
            "⏰ *Time limit: 10 minutes*",
            filters=filters.text,
            timeout=600,
        )
        if await cancelled(phone_code_msg):
            await client.disconnect()
            return
    except TimeoutError:
        await msg.reply(
            "⏱️ **Time limit of 10 minutes reached.** Please try again.",
            reply_markup=InlineKeyboardMarkup(Data.generate_button),
        )
        await client.disconnect()
        return

    phone_code = phone_code_msg.text.replace(" ", "").strip()

    try:
        if telethon:
            await client.sign_in(phone_number, phone_code, password=None)
        else:
            await client.sign_in(phone_number, code.phone_code_hash, phone_code)
    except (PhoneCodeInvalid, PhoneCodeInvalidError):
        await msg.reply(
            "❌ **OTP is invalid.** Please try again.",
            reply_markup=InlineKeyboardMarkup(Data.generate_button),
        )
        await client.disconnect()
        return
    except (PhoneCodeExpired, PhoneCodeExpiredError):
        await msg.reply(
            "⏰ **OTP is expired.** Please try again.",
            reply_markup=InlineKeyboardMarkup(Data.generate_button),
        )
        await client.disconnect()
        return
    except (SessionPasswordNeeded, SessionPasswordNeededError):
        try:
            two_step_msg = await bot.ask(
                user_id,
                "🔐 **Two-Step Verification (2FA) is enabled on your account.**\nPlease send your password:",
                filters=filters.text,
                timeout=300,
            )
        except TimeoutError:
            await msg.reply(
                "⏱️ **Time limit of 5 minutes reached.** Please try again.",
                reply_markup=InlineKeyboardMarkup(Data.generate_button),
            )
            await client.disconnect()
            return

        if await cancelled(two_step_msg):
            await client.disconnect()
            return

        try:
            password = two_step_msg.text.strip()
            if telethon:
                await client.sign_in(password=password)
            else:
                await client.check_password(password=password)
        except (PasswordHashInvalid, PasswordHashInvalidError):
            await two_step_msg.reply(
                "❌ **Invalid Password provided.** Please try again.",
                quote=True,
                reply_markup=InlineKeyboardMarkup(Data.generate_button),
            )
            await client.disconnect()
            return

    if telethon:
        string_session = client.session.save()
    else:
        string_session = await client.export_session_string()

    session_text = (
        f"**{lib_name.upper()} STRING SESSION**\n\n"
        f"`{string_session}`\n\n"
        f"⚠️ *Do NOT share this session string with anyone!*\n"
        f"Generated by @frozentools ❄️"
    )

    try:
        await client.send_message("me", session_text)
    except Exception:
        pass

    await client.disconnect()

    await phone_code_msg.reply(
        f"✅ **Successfully generated {lib_name} String Session!**\n\n"
        f"📩 **Please check your Saved Messages in Telegram.**\n\n"
        f"Powered by **@frozentools** ❄️"
    )


async def cancelled(msg):
    if not msg or not msg.text:
        return False
    if "/cancel" in msg.text:
        await msg.reply(
            "🚫 **Cancelled the session generation process!**",
            quote=True,
            reply_markup=InlineKeyboardMarkup(Data.generate_button),
        )
        return True
    elif "/restart" in msg.text:
        await msg.reply(
            "🔄 **Process restarted!**",
            quote=True,
            reply_markup=InlineKeyboardMarkup(Data.generate_button),
        )
        return True
    elif msg.text.startswith("/"):
        await msg.reply("🚫 **Cancelled the generation process.**", quote=True)
        return True
    return False
