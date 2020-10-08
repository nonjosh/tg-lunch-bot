import os

class BotConfig:
    # bot
    token = os.environ.get("TOKEN", '1332942054:AAFrASzNpBqrCoiVzTGn65YKCQ7prHEvz98')

class ChannelConfig:
    # channel
    # check by https://api.telegram.org/bot<YourBOTToken>/getUpdates

    #https://api.telegram.org/bot1332942054:AAFrASzNpBqrCoiVzTGn65YKCQ7prHEvz98/getUpdates
    #chat_id = os.environ.get("CHAT_ID", '-400962750')
    chat_id = os.environ.get("CHAT_ID", '-1001210702490')