import requests
import re
import os


def getstations():
    url='https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9181'
    response = requests.get(url,verify= True)
    stations =re.findall(u'([\u4e00-\u9fa5]+)\|([A-Z]+)',response.text)
    stations=  dict(stations)
    stations =str(stations)
    write(stations)

def write(stations):
    file =open('stations.text','w',encoding='utf-8_sig')
    file.write(stations)
    file.close()
def read():
    file =open('stations.text','r',encoding='utf-8_sig')
    data= file.readline()
    file.close()
    return   data
def  isStations():
     isStations =os.path.exists('stations.text')
     return isStations

