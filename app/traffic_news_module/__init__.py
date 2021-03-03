#!/usr/bin/python
import requests
from bs4 import BeautifulSoup
import json




def grep_traffic():
    url = 'https://www.881903.com/news/traffic'
    headers = {'user-agent': 'your-own-user-agent/0.0.1'}
    r = requests.get(url, headers=headers)
    print(r.status_code)
    if r.status_code == requests.codes.ok:
        soup = BeautifulSoup(r.text, "html.parser")
        # print("========")
        scripts = soup.find_all('script')
        # print(r.text)
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