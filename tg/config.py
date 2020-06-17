import os

class BotConfig:
    # botA
    token = os.environ.get("TOKEN", '<your token>')

class ChannelConfig:
    # channelA
    # check by https://api.telegram.org/bot<YourBOTToken>/getUpdates
    chat_id = os.environ.get("CHAT_ID", '<your chat_id>')