from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [
        InlineKeyboardButton("⚡ ꜱᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ ꜱᴇꜱꜱɪᴏɴ ⚡", callback_data="generate")
    ]

    home_buttons = [
        generate_single_button,
        [InlineKeyboardButton(text="🏠 ʀᴇᴛᴜʀɴ ʜᴏᴍᴇ 🏠", callback_data="home")],
    ]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [
            InlineKeyboardButton("❓ ʜᴏᴡ ᴛᴏ ᴜꜱᴇ", callback_data="help"),
            InlineKeyboardButton("📜 ᴀʙᴏᴜᴛ", callback_data="about"),
        ],
        [
            InlineKeyboardButton("📢 ᴏꜰꜰɪᴄɪᴀʟ ᴄʜᴀɴɴᴇʟ 📢", url="https://t.me/frozentools"),
        ],
    ]

    START = """
✨ **ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ꜱᴛʀɪɴɢ ꜱᴇꜱꜱɪᴏɴ ɢᴇɴᴇʀᴀᴛᴏʀ** ✨

👋 Hello {},

Welcome to **{}**!
I am a powerful bot designed to generate **Pyrogram v2** & **Telethon** string sessions safely and quickly.

🔒 **Security Notice:**
• Never share your OTP or 2FA password with anyone!
• Your API Credentials and Session keys are encrypted and never stored.

Click the buttons below to generate your session or learn more!
Powered by **@frozentools** ❄️
"""

    HELP = """
🚀 **ᴀᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅꜱ** 🚀

• `/start` - Start the bot & view main menu
• `/generate` - Start generating String Session
• `/help` - Show usage & tutorial
• `/about` - About this bot & version
• `/repo` - Get source code link
• `/cancel` - Cancel ongoing session generation process
• `/restart` - Restart the session generation process
"""

    ABOUT = """
❄️ **ᴀʙᴏᴜᴛ ᴛʜɪꜱ ʙᴏᴛ** ❄️

• **Name**: String Session Generator Bot
• **Language**: [Python 3.11+](https://www.python.org)
• **Framework**: [Pyrogram v2](https://docs.pyrogram.org) & [Telethon](https://docs.telethon.dev)
• **Channel**: [@frozentools](https://t.me/frozentools)
• **Source Code**: [GitHub](https://github.com/alonepro098/tmm-string)

⚡ Powered & Maintained by **@frozentools**
"""

    REPO = """
━━━━━━━━━━━━━━━━━━━━━━━━━━
✨ **FROZENTOOLS STRING BOT** ✨
━━━━━━━━━━━━━━━━━━━━━━━━━━
A powerful, updated, and fast String Session Generator for Telegram.

• **Channel**: [@frozentools](https://t.me/frozentools)
• **Support**: [@frozentools](https://t.me/tmm_support_chat)
• **Source Code**: [Click Here](https://github.com/alonepro098/tmm-string)
━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
