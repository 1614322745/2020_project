from getstations import *
import json
import requests
data = []
type_data = []

def query(date,from_station,to_station):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
        'Cookie':'JSESSIONID=9A3A60B55A2ACC51B24B6742E68E6230; RAIL_EXPIRATION=1582469373862; RAIL_DEVICEID=ERLN34ss4QuQiVGSBZaJz35V5mfm37V7QotSqYowrxa7ljZeEnI-RQjWRUTV8qjMdb5w8sps-WX286eIS9RF7Y_TOr4Cj6wSa_4UIfjh8GwzQPfWOV6nz8EIIIEfX-3ciBnc11jpF14E5BBpRzAqtiV8gdANBiKr; BIGipServerpool_passport=267190794.50215.0000; route=495c805987d0f5c8c84b14f60212447d; _jc_save_toDate=2021-01-15; _jc_save_wfdc_flag=dc; _jc_save_fromDate=2021-01-15; BIGipServerotn=451936778.24610.0000; _jc_save_fromStation=%u5317%u4EAC%2CBJP; _jc_save_toStation=%u4E4C%u9C81%u6728%u9F50%2CWAR'
    }
    # headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36','Cookie':'_uab_collina=159618052151589201474313; JSESSIONID=D33C89D8BEC6A692C79CFA69FC0B0D29; BIGipServerotn=233832970.24610.0000; BIGipServerpool_passport=216859146.50215.0000; RAIL_EXPIRATION=1596443951465; RAIL_DEVICEID=nMo94O2Z21cXLblW7otLoxUZ_LP9Q01PYj_I89OqU6MqjxyX9814Jc3CH5TNwgBVJqnBaBG8OGiBWo2QtNcu5wVu-asNk6YLa49g0fMwVp03XFJQ-GkhHYHcqIgUd-nqQB_VEdWH1Om_D2yAgIu8QcEavt02pmH5; route=c5c62a339e7744272a54643b3be5bf64; _jc_save_fromStation=%u5317%u4EAC%2CBJP; _jc_save_toStation=%u5929%u6D25%2CTJP; _jc_save_fromDate=2020-07-31; _jc_save_toDate=2020-07-31; _jc_save_wfdc_flag=dc'}
    data.clear()
    url ='https://kyfw.12306.cn/otn/leftTicket/queryT?leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT'.format(date,from_station,to_station)
    response = requests.get(url,headers=headers,allow_redirects=False)
    print(response.status_code)
    response.encoding='utf-8'
    print(response.json())
    result=json.loads(response.text)
    #result =response.json()

    result=result['data']['result']
    print(result)
    if isStations()==True:
        stations= eval(read())
        if len(result)!=0:
            for i in result:
                tmp_list=i.split('|')
                from_station=list(stations.keys())[list(stations.values()).index(tmp_list[6])]
                to_station=list(stations.keys())[list(stations.values()).index(tmp_list[7])]

                seat=[tmp_list[3],from_station,to_station,tmp_list[8],tmp_list[9],tmp_list[10]
                    ,tmp_list[32],tmp_list[31],tmp_list[30],tmp_list[21]
                    ,tmp_list[23],tmp_list[33],tmp_list[28],tmp_list[24],tmp_list[29],tmp_list[26]]
                newseat= []
                for s in seat:
                    if s=="":
                        s="--"
                    else:
                        s=s
                    if s=='24:00' or s=="99:59":
                        s='列车停运'

                    newseat.append(s)
                data.append(newseat)
        return data


def g_vehicle():
    if len(data)!=0:
        for g in data:
            i = g[0].startswith('G')
            if i:
                type_data.append(g)


def r_g_vehicle():
    if len(data)!=0:
        for g in data:
            i = g[0].startswith('G')
            if i:
                type_data.remove(g)


def d_vehicle():
    if len(data)!=0:
        for d in data:
            i= d[0].startswith('D')
            if i ==True:
                type_data.append(d)

def r_d_vehicle():
     if len(data)!=0:
        for d in data:
            i= d[0].startswith('D')
            if i ==True:
                type_data.remove(d)



def z_vehicle():
     if len(data)!=0:
        for z in data:
            i= z[0].startswith('Z')
            if i ==True:
                type_data.append(z)

def r_z_vehicle():
    if len(data)!=0:
        for z in data:
            i= z[0].startswith('Z')
            if i ==True:
                type_data.remove(z)


def  t_vehicle():
    if len(data)!=0:
        for t in data:
            i= t[0].startswith('T')
            if i ==True:
                type_data.append(t)

def r_t_vehicle():
     if len(data)!=0:
        for t in data:
            i= t[0].startswith('T')
            if i ==True:
                type_data.remove(t)


def  k_vehicle():
     if len(data)!=0:
        for k in data:
            i= k[0].startswith('K')
            if i ==True:
                type_data.append(k)


def r_k_vehicle():
    if len(data)!=0:
        for k in data:
            i= k[0].startswith('K')
            if i ==True:
                type_data.remove(k)
query('2021-01-15','BJP','SHH')
