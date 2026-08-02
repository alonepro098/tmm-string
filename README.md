<h1 align="center">
  ❄️ FrozenTools String Session Generator ❄️
</h1>

<p align="center">
  <b>A powerful, high-speed, and secure Telegram String Session Generator Bot built with Pyrogram v2 & Telethon.</b>
</p>

<p align="center">
  <a href="https://www.python.org">
    <img src="https://img.shields.io/badge/Python-3.11%2B-blue?style=for-the-badge&logo=python" alt="Python Version" />
  </a>
  <a href="https://docs.pyrogram.org">
    <img src="https://img.shields.io/badge/Pyrogram-v2.0-red?style=for-the-badge&logo=telegram" alt="Pyrogram v2" />
  </a>
  <a href="https://docs.telethon.dev">
    <img src="https://img.shields.io/badge/Telethon-v1.36-orange?style=for-the-badge&logo=telegram" alt="Telethon" />
  </a>
  <a href="https://t.me/frozentools">
    <img src="https://img.shields.io/badge/Channel-@frozentools-0088cc?style=for-the-badge&logo=telegram" alt="Channel" />
  </a>
</p>

---

## ✨ Features

- ⚡ **Pyrogram V2 Support**: Generates latest 351-character Pyrogram V2 String Sessions.
- 📱 **Telethon Support**: Generates standard Telethon String Sessions.
- 🔐 **Secure & Encrypted**: OTPs and 2FA Passwords are processed live and never logged or stored.
- 💬 **Force Join Support**: Enforce channel subscription before users can access session generation.
- 🚀 **One-Click Deployment**: Deploy easily on Heroku, Render, Koyeb, or VPS.

---

## 🛠️ Required Environment Variables

| Variable | Description | Required | Default |
| :--- | :--- | :---: | :---: |
| `API_ID` | Telegram API ID from [my.telegram.org](https://my.telegram.org) | Yes | - |
| `API_HASH` | Telegram API HASH from [my.telegram.org](https://my.telegram.org) | Yes | - |
| `BOT_TOKEN` | Telegram Bot Token from [@BotFather](https://t.me/BotFather) | Yes | - |
| `MUST_JOIN` | Channel username for force subscription (without `@`) | No | `frozentools` |
| `DATABASE_URL` | PostgreSQL Database URL for storing bot user stats | No | - |

---

## 🚀 Deployment

### 1️⃣ Deploy on Heroku

<p align="center">
  <a href="https://dashboard.heroku.com/new?template=https://github.com/alonepro098/tmm-string">
    <img src="https://img.shields.io/badge/Deploy%20To%20Heroku-purple?style=for-the-badge&logo=heroku" width="220" height="40"/>
  </a>
</p>

### 2️⃣ Run Locally

```bash
# Clone the repository
git clone https://github.com/alonepro098/tmm-string.git
cd tmm-string

# Install requirements
pip install -r requirements.txt

# Create .env file with your credentials
cp .env.sample .env # Fill API_ID, API_HASH, BOT_TOKEN

# Run the bot
python bot.py
```

---

## 📢 Credits & Channel

- **Maintained & Powered By**: [@frozentools](https://t.me/frozentools)
- **Frameworks**: [Pyrogram](https://github.com/pyrogram/pyrogram) & [Telethon](https://github.com/LonamiWebs/Telethon)

---
<p align="center">
  Made with ❤️ by <b>@frozentools</b>
</p>
