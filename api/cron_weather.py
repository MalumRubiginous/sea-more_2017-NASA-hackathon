#coding:utf-8
import requests
import xmltodict
import json
from collections import OrderedDict
from datetime import datetime
from dateutil.relativedelta import relativedelta
from dateutil.parser import parse
import io
from flask_apscheduler import APScheduler
from flask import Flask,request,Response

WEATHER_ID = "F-D0047-089"
UV_ID = "O-A0005-001"
TIDE_ID = "F-A0021-001"
OCEAN_ID = "O-A0018-001"

CWBKEY = "KEY"

WEATHER_URL = "http://opendata.cwb.gov.tw/opendataapi?dataid={}&authorizationkey={}".format(WEATHER_ID, CWBKEY)
UV_URL = "http://opendata.cwb.gov.tw/opendataapi?dataid={}&authorizationkey={}".format(UV_ID, CWBKEY)
TIDE_URL = "http://opendata.cwb.gov.tw/opendataapi?dataid={}&authorizationkey={}".format(TIDE_ID, CWBKEY)
OCEAN_URL = "http://opendata.cwb.gov.tw/opendataapi?dataid={}&authorizationkey={}".format(OCEAN_ID, CWBKEY)
#UV_URL = "http://opendata.epa.gov.tw/webapi/api/rest/datastore/355000000I-000004?sort=PublishTime&offset=0&limit=1000"


app = Flask(__name__)
data = {}
candidate = {}
data_latest_version = ""

def ocean():
    print "Getting Ocean data..."
    r = requests.get(OCEAN_URL)
    o = xmltodict.parse(r.text)
    loc = {
        "46699A":u"花蓮縣",
        "46757B":u"新竹縣",
        "46694A":u"新北縣",
        "46714D":u"高雄縣",
        "WRA007":u"臺東縣",
        "46735A":u"澎湖縣",
        "46706A":u"宜蘭縣",
        "46787A":u"金門縣",
        "46759A":u"屏東縣",
        "4P21":u"苗栗縣",
        "COMC07":u"基隆市",
        "46778A":u"臺南縣"
    }
    tmp = [x for x in o["cwbopendata"]["dataset"]["location"] if x['stationId'] in loc.keys()]
    data = {}
    for i,each in enumerate(tmp):
        _data = {}
        if i%8==0:
            l = loc[each["stationId"]]
            data[l] = []

        _data_ = {}

        t = each["time"]["obsTime"]
        wind = each["time"]["weatherElement"][1]["elementValue"]["value"] # 平均風
        temp = each['time']["weatherElement"][8]["elementValue"]["value"] # 海溫
        try:
            temp = float(temp) / 10
        except:
            temp = None
        _data_[t] = [wind, temp]
        data[l].append(_data_)
    with io.open("../data/ocean.json","w", encoding="utf-8") as f:
        f.write(json.dumps(data, ensure_ascii=False, indent=4))
    print "Done for job ocean"


def tide():
    print "Getting Tide data..."
    r = requests.get(TIDE_URL)
    o = xmltodict.parse(r.text)
    for each in o['cwbopendata']['dataset']['location']:
        data.update({each['locationName']: []})
        for time in each['time']:
            time['validTime']['startTime']
            data[each['locationName']].append(time)
    for loc in data:
        month_data = OrderedDict()
        for i in range(len(data[loc])):
            _data = OrderedDict()
            for each in data[loc][i]['weatherElement'][2]['time']:
                tide = each['weatherElement'][0]['value']
                time = each['weatherElement'][1]['value']
                height = each['weatherElement'][3]['elementValue']['value']
                _data.update({time:[tide, height]})
            month_data.update(_data)
        data[loc].append(month_data)
    final_data = {}
    for loc in data:
        final_data.update({loc:data[loc][-1]})
    with io.open("../data/tide.json","w", encoding="utf-8") as f:
        f.write(json.dumps(final_data, ensure_ascii=False, indent=4))
    print "Done for job tide"




def uv():
    r = requests.get(UV_URL)
    o = xmltodict.parse(r.text)
    print "Getting UV data..."
    with open("./location_code.json","r") as f:
        locode = json.load(f)
    locode_inv = dict((v,k) for k, v in locode.iteritems())
    data = {}
    tmp = o['cwbopendata']['dataset']['weatherElement']['location']
    for each in tmp:
        try:
            loc = locode_inv[each['locationCode']]
            v = each["value"]
            data.update({loc:v})
        except:
            pass
    data.update({u"臺中市":[x['value'] for x in tmp if x['locationCode']=="467490"][0]})
    data.update({u"嘉義縣":[x['value'] for x in tmp if x['locationCode']=="467480"][0]})
    data.update({u"雲林縣":[x['value'] for x in tmp if x['locationCode']=="467480"][0]})
    data.update({u"新竹縣":[x['value'] for x in tmp if x['locationCode']=="467570"][0]})
    data.update({u"苗栗縣":[x['value'] for x in tmp if x['locationCode']=="467570"][0]})
    data.update({u"金門縣":[x['value'] for x in tmp if x['locationCode']=="467110"][0]})
    with io.open("../data/max_uv.json","w", encoding="utf-8") as f:
        f.write(json.dumps(data, ensure_ascii=False, indent=4))
    print "Done for job UV"

#def uv():
#    r = requests.get(UV_URL)
#    print "Getting UV data..."
#    j = json.loads(r.text)
#    data = {}
#    for each in j['result']['records']:
#        data.update({each['County']:each['UVI']})
#    with io.open("../data/uv.json","w", encoding="utf-8") as f:
#        f.write(json.dumps(data, ensure_ascii=False, indent=4))
#    print "Done for job UV"



def country_weather():
    r = requests.get(WEATHER_URL)
    print "Getting country weather data from CWB..."
    raw = xmltodict.parse(r.text)
    all_data = OrderedDict()
    for weather in raw['cwbopendata']['dataset']["location"]:#['location']:
        data = OrderedDict()
        for each in weather["weatherElement"]:
            if each['elementName'] == "T": # 溫度

                data['T'] = OrderedDict()
                for t in each['time']:
                    time = t['dataTime']
                    value = t['elementValue']["value"]
                    data['T'].update({time:value})

            if each['elementName'] == "RH": #相對濕度

                data['RH'] = OrderedDict()
                for t in each['time']:
                    time = t['dataTime']
                    value = t['elementValue']["value"]
                    data['RH'].update({time:value})

            if each['elementName'] == "PoP6h": #降雨機率

                data['PoP6h'] = OrderedDict()
                for t in each['time'][:-1]:
                    time = t['startTime']
                    value = t['elementValue']["value"]
                    data['PoP6h'].update({time:value})
                    time = parse(time) + relativedelta(hours=3)
                    time = time.isoformat()
                    data['PoP6h'].update({time:value})


            if each['elementName'] == "Wx": #天氣

                data['Wx'] = OrderedDict()
                for t in each['time']:
                    time = t['startTime']
                    value = t['elementValue']["value"]
                    data['Wx'].update({time:value})

            if each['elementName'] == "Wind": # 風

                data["Wind"] = OrderedDict()
                for t in each['time']:
                    time = t['dataTime']
                    value = t['parameter']
                    data['Wind'].update({time:value})
        loc = weather["locationName"]
        tmp =  OrderedDict()
        tmp[loc] = data

        all_data.update(tmp)
    with io.open("../data/country_weather.json","w", encoding="utf-8") as f:
        f.write(json.dumps(all_data, ensure_ascii=False, indent=4))
    print "Done for job country weather"

class Config(object):
    JOBS = [
        {
            'id': 'ocean',
            'func': ocean,
            'trigger': 'interval',
            'seconds': 1800
        },
        {
            'id': 'tide',
            'func': tide,
            'trigger': 'interval',
            'seconds': 7200
        },
        {
            'id': 'country_weather',
            'func': country_weather,
            'trigger': 'interval',
            'seconds': 3600
        },
        {
            'id': 'uv',
            'func': uv,
            'trigger': 'interval',
            'seconds': 3600
        }
    ]
    SCHEDULER_API_ENABLED = True

if __name__ == "__main__":
    ocean()
    tide()
    uv()
    country_weather()
    app.config.from_object(Config())
    scheduler = APScheduler()
    scheduler.init_app(app)
    scheduler.start()
    app.run(host='0.0.0.0',port=8090,threaded=True)
