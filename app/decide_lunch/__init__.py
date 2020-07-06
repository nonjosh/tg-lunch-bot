import random

LIST_PATH = "decide_lunch/list.txt"

def getList():
    my_file = open(LIST_PATH, "r")
    content = my_file.read()
    content_list = content.split("\n")
    return content_list

def getDecision():
    return random.choice(getList())