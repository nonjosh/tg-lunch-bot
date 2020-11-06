import os
from dotenv import load_dotenv
load_dotenv()



class BotConfig:
    token = os.environ.get("TOKEN", '1332942054:AAFrASzNpBqrCoiVzTGn65YKCQ7prHEvz98')

class ChannelConfig:
    #https://api.telegram.org/bot1332942054:AAFrASzNpBqrCoiVzTGn65YKCQ7prHEvz98/getUpdates
    controller_id = os.environ.get("CONTROLLER_ID", '-400962750')
    #chat_id = os.environ.get("CHAT_ID", '-400962750')   #   development group :  testing lunch 
    chat_id = os.environ.get("CHAT_ID", '-1001210702490')  # production  group :  Alchemy

class TimestampConfig: 
    time_zone = os.environ.get("TIME_ZONE" , "Asia/Hong_Kong")
    time_lunch = os.environ.get('LUNCH_TIME', '11:30')
    time_traffic = str(os.environ.get('TRAFFIC_TIME', ['07:00', '12:00', '16:30'])).split(",")


class ReplyStrMap:
    please_reroll = os.environ.get("please_reroll", '')
    too_noisy = os.environ.get("too_noisy", '')
    foul_1 = os.environ.get("foul_1", '')
    



