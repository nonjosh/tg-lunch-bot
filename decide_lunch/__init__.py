import random
import logging, logging.config
logger = logging.getLogger(__name__)


LIST_PATH = "decide_lunch/list.txt"

def getTxt():
    my_file = open(LIST_PATH, "r")
    content = my_file.read()
    return content

def getList():
    new_list = []
    content_list = getTxt().split("\n")
    for item in content_list:
        if(not item.startswith("##") and item != ''):
            new_list.append(item)
    
    print(new_list)
    return new_list

def getLunchDecision():

    logger.info("calling : getLunchDecision"  )
    whole_msg = '根據沉默大多數愛好和平同事的主流意見\n今日lunch決定食:\n<i><u><b>{}</b></u></i>'.format(random.choice(getList()))
    return whole_msg