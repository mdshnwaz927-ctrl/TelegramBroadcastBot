from flask import Flask
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ParseMode
import config


app = Flask(__name__)


users = set() # store subscribed users


def start(update, context):
users.add(user_id)
update.message.reply_text("You are subscribed to broadcast messages.")




def broadcast(update, context):
if update.effective_user.id != config.OWNER_ID:
return update.message.reply_text("Not allowed.")


msg = " ".join(context.args)


if not msg:
return update.message.reply_text("Usage: /broadcast Your message here")


count = 0
for uid in users:
try:
context.bot.send_message(chat_id=uid, text=msg, parse_mode=ParseMode.HTML)
count += 1
except:
pass


update.message.reply_text(f"Broadcast sent to {count} users.")




def webhook():
return "Bot Running", 200




@app.route('/')
def home():
return "OK", 200




def run_bot():
updater = Updater(config.BOT_TOKEN, use_context=True)
dp = updater.dispatcher


dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("broadcast", broadcast))


updater.start_polling()
updater.idle()




if __name__ == "__main__":
run_bot()
