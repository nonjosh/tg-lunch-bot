#!/usr/bin/python
import requests
from bs4 import BeautifulSoup
import json
import logging, logging.config
logger = logging.getLogger(__name__)


def grep_weather():
    logger.info("calling : grep_traffic")
    url = 'https://www.hko.gov.hk/json/DYN_DAT_MINDS_FLW.json'
    r = requests.get(url)
    if r.status_code == requests.codes.ok:
        soup = BeautifulSoup(r.text, "html.parser")
        print(r.text)
        print( " Type of r : {} ".format(type(r.text)) )
        json_content = json.loads(r.text)
        content = ''
        content = content + "\n" +  json_content['DYN_DAT_MINDS_FLW']['FLW_WxForecastGeneralSituation']['Val_Chi']
        content = content + "\n" + json_content['DYN_DAT_MINDS_FLW']['FLW_WxForecastTCInfo']['Val_Chi']
        content = content + "\n" + json_content['DYN_DAT_MINDS_FLW']['FLW_WxForecastPeriod']['Val_Chi']
        content = content + "\n" + json_content['DYN_DAT_MINDS_FLW']['FLW_WxForecastWxDesc']['Val_Chi']
        content = content + "\n" + json_content['DYN_DAT_MINDS_FLW']['FLW_WxOutlookContent']['Val_Chi']

        print(content)
        return content
# grep_weather()