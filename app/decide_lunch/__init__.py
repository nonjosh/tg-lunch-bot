import random

LIST_PATH = "decide_lunch/list.txt"

def getTxt():
    my_file = open(LIST_PATH, "r")
    content = my_file.read()
    return content

def getList():
    content_list = getTxt().split("\n")
    return content_list

def getDecision():
    return random.choice(getList())