#!/usr/bin/python
import requests
from bs4 import BeautifulSoup
import json
import logging, logging.config
logger = logging.getLogger(__name__)


def grep_traffic():
    logger.info("calling : grep_traffic")
    url = 'https://www.881903.com/news/traffic'
    r = requests.get(url)
    if r.status_code == requests.codes.ok:
        soup = BeautifulSoup(r.text, "html.parser")
        scripts = soup.find_all('script')
        target_script = scripts[-1]
        target_script = str(target_script).replace("<script>VueApp.main(", "")
        target_script = str(target_script).replace(")</script>", "")
        target_script = str(target_script).replace("\'", "\"")
        target_script = str(target_script).replace("None", "\"None\"")
        json_content = json.loads(target_script)
        content = ""
        for i in range(5):
            temp = json_content['traffic_info']['content'][i]['title']
            #print(temp)
            content = content + temp + "\n"
        print(content)
        return content