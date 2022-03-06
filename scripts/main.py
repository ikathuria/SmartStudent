from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import redis

r = redis.from_url('your_redis_db_url') # connection to the databse
db_keys = r.keys(pattern='*')  # allows us to fetch data

updater = Updater(token='1605329753:AAGy9Hukl7Nc8CzUJ0tcfndxR_tctvKDCRI', use_context=True)
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


def start(update, context):
    user_id = update.message.from_user.id
    user_name = update.message.from_user.name
    r.set(user_name, user_id)
    message = 'Welcome to the bot'
    context.bot.send_message(chat_id=update.effective_chat.id,text=message)


def echo(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=update.message.text)


# give a name to the command and add it to the dispaatcher
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
updater.start_polling() # enable bot to get updates

echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)
