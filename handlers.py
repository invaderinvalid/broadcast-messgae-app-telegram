from telegram import Update
from telegram.ext import ContextTypes
from datetime import datetime
import utils
import os
from dotenv import load_dotenv

load_dotenv()
START_TIME = datetime.now()
LOG_CHANNEL = int(os.getenv('LOG_CHANNEL'))
AUTH_ADMINS = [int(id) for id in os.getenv('AUTH_ADMINS').split(',')]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message.chat.type in ['group', 'supergroup']:
        group_id = update.message.chat_id
        group_name = update.message.chat.title
        existing_groups = utils.get_all_group_ids()
        
        if group_id not in existing_groups:
            utils.add_group(group_id, group_name)
            await update.message.reply_text("Group registered successfully!")
        
        await update.message.reply_text("Hello! I'm a broadcast bot.")
    else:
        await update.message.reply_text("Hello! I'm a broadcast bot. Please add me to a group to use my features.")

async def ping(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Pong!")

async def info(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.effective_user.id not in AUTH_ADMINS:
        await update.message.reply_text("You're not authorized to use this command.")
        return

    uptime = datetime.now() - START_TIME
    group_count = utils.get_group_count()

    await update.message.reply_text(f"Number of groups: {group_count}\nUptime: {uptime}")

async def broadcast(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.effective_user.id not in AUTH_ADMINS:
        await update.message.reply_text("You're not authorized to use this command.")
        return

    if not update.message.reply_to_message:
        await update.message.reply_text("Please reply to a message to broadcast.")
        return

    reply = update.message.reply_to_message
    sender_id = update.effective_user.id
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    groups = utils.get_all_group_ids()
    success_count = 0
    
    for group_id in groups:
        try:
            if reply.text:
                await context.bot.send_message(chat_id=group_id, text=reply.text)
            elif reply.photo:
                await context.bot.send_photo(chat_id=group_id, photo=reply.photo[-1].file_id, caption=reply.caption)
            elif reply.video:
                await context.bot.send_video(chat_id=group_id, video=reply.video.file_id, caption=reply.caption)
            elif reply.audio:
                await context.bot.send_audio(chat_id=group_id, audio=reply.audio.file_id, caption=reply.caption)
            elif reply.document:
                await context.bot.send_document(chat_id=group_id, document=reply.document.file_id, caption=reply.caption)
            elif reply.voice:
                await context.bot.send_voice(chat_id=group_id, voice=reply.voice.file_id, caption=reply.caption)
            elif reply.sticker:
                await context.bot.send_sticker(chat_id=group_id, sticker=reply.sticker.file_id)
            else:
                print(f"Unsupported message type for group {group_id}")
                continue

            success_count += 1
        except Exception as e:
            print(f"Failed to send message to group {group_id}: {str(e)}")

    # Save broadcast info to database
    content_type = "text" if reply.text else "media"
    utils.save_broadcast(content_type, sender_id, timestamp)

    log_message = f"A {content_type} message was broadcasted by user {sender_id} at {timestamp}. Sent to {success_count}/{len(groups)} groups."
    await context.bot.send_message(chat_id=LOG_CHANNEL, text=log_message)

    await update.message.reply_text(f"Broadcast sent successfully to {success_count}/{len(groups)} groups!")