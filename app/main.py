from datetime import datetime, time
from threading import Timer
from tg.bot import send_channel, TOKEN
from decide_lunch import getDecision, getTxt
import os
from telegram.ext import Updater, CommandHandler
from telegram import ParseMode

time2decide = os.environ.get('MSG_TIME', '12:15')

def getDateTime():
    now = datetime.now()
    current_time = now.strftime('%Y/%m/%d %H:%M:%S')
    return current_time

def printT(msg):
    print('[{}] {}'.format(getDateTime(), msg))

def check_within_weekdays():
    return 1 <= datetime.today().isoweekday() <= 5

def check_time2decide():
    now = datetime.now()
    return now.strftime("%H:%M") == time2decide

def recur_check():
    # Decide and send message at {{time2decide}} in weekdays
    if check_time2decide() and check_within_weekdays():
       send_decision()

    # Repeat every minutes
    timer_interval_sec = 60
    t = Timer(timer_interval_sec, recur_check)
    t.start()

def decision_msg(decision_today):
    return '根據沉默大多數愛好和平同事的主流意見\n今日lunch決定食:\n<i><u><b>{}</b></u></i>'.format(decision_today)

def send_decision():
    decision_today = getDecision()
    printT(decision_today)
    msg = decision_msg(decision_today)
    send_channel(msg)

def start_updater():
    def showAllCommands(update, context):
        msg = """\
/reroll
/list, /ls, /ps
/add - <COMING SOON>
/remove, /rm - <COMING SOON>
"""        
        update.message.reply_text(msg)
    
    def reroll(update, context):
        decision_today = getDecision()
        update.message.reply_text(text=decision_msg(decision_today), 
                    parse_mode=ParseMode.HTML)

    def showlist(update, context):
        msg = getTxt()
        update.message.reply_text(msg)
    
    def comingsoon(update, context):
        msg = 'COMING SOON'
        update.message.reply_text(msg)
    
    updater = Updater(TOKEN, use_context=True)

    updater.dispatcher.add_handler(CommandHandler(('help', 'start'), showAllCommands))
    updater.dispatcher.add_handler(CommandHandler('reroll', reroll))
    updater.dispatcher.add_handler(CommandHandler(('list', 'ls', 'ps'), showlist))
    # TODO add restaurants
    updater.dispatcher.add_handler(CommandHandler('add', comingsoon))
    # TODO remove restaurants
    updater.dispatcher.add_handler(CommandHandler(('remove', 'rm'), comingsoon))

    updater.start_polling()
    # updater.idle()

if __name__ == '__main__':
    
    printT('Program Start!')
    printT('The decision time on weekdays: {}'.format(time2decide))
    # send_channel("Program Start!")
    
    start_updater()
    # send_decision()
    recur_check()