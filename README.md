# Telegram Broadcast Bot

This is a versatile Telegram bot designed to broadcast messages to multiple groups. It supports broadcasting of various content types including text, photos, videos, audio, documents, voice messages, and stickers.

## Features

- Broadcast various types of content to multiple groups
- Automatically register groups when the bot is added
- Track the number of groups the bot is in
- Admin-only commands for broadcasting and getting bot info
- Logging of broadcast activities

## Commands

- `/start` - Initializes the bot in a group or greets a user in private chat
- `/ping` - Check if the bot is running
- `/info` - (Admin only) Get information about the number of groups and bot uptime
- `/broadcast` - (Admin only) Broadcast a message to all registered groups

## Setup

1. Clone this repository:
   ```
   https://github.com/invaderinvalid/broadcast-messgae-app-telegram.git
   ```
   ```
   cd broadcast-messgae-app-telegram
   ```
2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```
3. Edit `.env`:
```
BOT_TOKEN=Your_bot_Token_here
LOG_CHANNEL= channel/chat_id 
AUTH_ADMINS=admin1_id,admin2_id
```

## Project Structure

- `main.py`: Main entry point of the bot
- `handlers.py`: Contains all the command handlers
- `utils.py`: Utility functions and database operations

## Database

The bot uses SQLite to store information about registered groups and broadcast history. Two tables are created:

1. `groups`: Stores information about registered groups
2. `broadcasts`: Logs all broadcast activities

## Broadcasting

To broadcast a message, reply to any message (text or media) with the `/broadcast` command. Only authorized admins can use this command.

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to check [issues page](https://github.com/invaderinvalid/broadcast-messgae-app-telegram/issues) if you want to contribute.

   
