
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ParseMode
from datetime import datetime, time
from pytz import timezone
from threading import Timer
import os, sys, inspect, traceback


from decide_lunch import getLunchDecision, getTxt
from traffic_news import grep_traffic
from setting import BotConfig, ChannelConfig, TimestampConfig, ReplyStrMap
from bot_basic_handler import *
tz = timezone(TimestampConfig.time_zone)


import logging, logging.config
logging.basicConfig(
    filename = 'app.log',
    level=logging.INFO,
    # format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s',
    format='%(asctime)s %(levelname)s %(module)s - %(funcName)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
)
logger = logging.getLogger(__name__)


TOKEN = BotConfig.token
chat_id = ChannelConfig.chat_id
controller_id = ChannelConfig.controller_id
bot = telegram.Bot(token=TOKEN)
count_dict = dict()

def notice_control_room():
    now = datetime.now()
    current_time = now.strftime('%Y/%m/%d %H:%M:%S')
    msg = '[{}] {}'.format(current_time,"Bot Start .... Chat Room id  : " )
    bot.sendMessage(chat_id=controller_id,
                    text= msg + str(chat_id) ,
                    parse_mode=telegram.ParseMode.HTML)

def send_channel(content='No input content'):
    bot.sendMessage(chat_id=chat_id,
                    text=content,
                    parse_mode=telegram.ParseMode.HTML)

def del_msg(update):
    bot.delete_message(chat_id=str(chat_id), message_id=update.message.message_id)

def boardcast(update, context):
    print("boardcast")
    print(context.args[0])
    msg = context.args[0]
    send_channel(msg)


def filter_handler(update, context):
    print(" Function : " + str(inspect.currentframe().f_code.co_name))
    content = str(update.message.text)
    print(content)
    if(content.startswith('/')):
        print("return")
        return
    elif "收皮" in content:
        update.message.reply_text(ReplyStrMap.please_reroll)
    elif "DLLM" in content:
        update.message.reply_text(ReplyStrMap.foul_1)
    else:
        pass
        #update.message.reply_text(ReplyStrMap.too_noisy)
    

def reroll(update, context):
    print(" Function : " + str(inspect.currentframe().f_code.co_name))
    global count_dict
    user_id, first_name, last_name, user_name = get_user_info(update)
    print("User id Reroll : {}".format(user_id))
    if user_id in count_dict:
        print("Count of Reroll : {}".format(count_dict[user_id]))
        if(count_dict[user_id] >= 2):
            update.message.reply_text(text="滾動不能，每天僅重新滾動兩次" , parse_mode=ParseMode.HTML)
        else:
            update.message.reply_text(text=getLunchDecision(), parse_mode=ParseMode.HTML)  
        count_dict[user_id] = count_dict[user_id] + 1
    else:
        print("Count of Reroll : {}".format("Zero"))
        count_dict[user_id] = 1
        update.message.reply_text(text=getLunchDecision(), parse_mode=ParseMode.HTML)        


def traffic(update, context):
    try:
        print("Group Chat Id : {}".format(update.message.chat.id))
        print(" Function : " + str(inspect.currentframe().f_code.co_name))
        content = grep_traffic()
        msg_json = update.message.reply_text(text=content, parse_mode=ParseMode.HTML)     
        print(msg_json['message_id'])
        bot.pinChatMessage(chat_id = update.message.chat.id, message_id = msg_json['message_id'] )
    except Exception:
        error_msg = traceback.format_exc(limit=None, chain=True)
        #traceback.print_exc()
        print(error_msg)
        #update.message.reply_text(error_msg)


def showlist(update, context):
    print(" Function : " + str(inspect.currentframe().f_code.co_name))
    msg = getTxt()
    update.message.reply_text(msg)

def getCommands(update, context):
    print(bot.getMyCommands())

def recur_check():
    current_time_stamp = get_hhmm()
    if( current_time_stamp == TimestampConfig.time_lunch and check_within_weekdays()):
        logger.info("calling : getLunchDecision" )
        send_channel(getLunchDecision())
    #print(TimestampConfig.time_traffic)
    if(current_time_stamp in TimestampConfig.time_traffic and check_within_weekdays()):
        logger.info("calling : grep_traffic" )
        send_channel(grep_traffic())
    timer_interval_sec = 60
    t = Timer(timer_interval_sec, recur_check)
    t.start()

if __name__ == '__main__':

    notice_control_room()
    updater = Updater(TOKEN, use_context=True)

    # ------ Lunch Relatated
    updater.dispatcher.add_handler(CommandHandler('reroll', reroll))
    updater.dispatcher.add_handler(CommandHandler(('list', 'ls', 'ps'), showlist))
    #updater.dispatcher.add_handler(CommandHandler('add', comingsoon))
    #updater.dispatcher.add_handler(CommandHandler(('remove', 'rm'), comingsoon))

    # ------ Traffic Relatated
    updater.dispatcher.add_handler(CommandHandler('traffic', traffic))

    # boardcast and text filter
    updater.dispatcher.add_handler(CommandHandler('boardcast', boardcast))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, filter_handler))


    updater.dispatcher.add_handler(CommandHandler('gc', getCommands))

    updater.start_polling()
    recur_check()