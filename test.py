
from Tkinter import *
import locale
import threading
import time
import requests
import json
import traceback
import feedparser
import datetime


from PIL import Image, ImageTk
from contextlib import contextmanager

LOCALE_LOCK = threading.Lock()

ui_locale = '' # e.g. 'fr_FR' fro French, '' as default
time_format = 12 # 12 or 24
date_format = "%b %d, %Y" # check python doc for strftime() for options
news_country_code = 'us'
weather_api_token = '577aa106d3103fb09a06a112ac0c4aa0' # create account at https://darksky.net/dev/
weather_lang = 'en' # see https://darksky.net/dev/docs/forecast for full list of language parameters values
weather_unit = 'us' # see https://darksky.net/dev/docs/forecast for full list of unit parameters values
latitude = None # Set this if IP location lookup does not work for you (must be a string)
longitude = None # Set this if IP location lookup does not work for you (must be a string)
xlarge_text_size = 94
large_text_size = 48
medium_text_size = 28
small_text_size = 18
xsmall_text_size = 12
padding_x = 50
padding_y = 60

maps_api_token = 'AIzaSyB3errcMBierCO-bId7J7ugWoltd-Jr7oY'
maps_origin = '3012+Meadow Lane+Drive+Westlake+OH'
#maps_origin = '2918+Jefferson+Avenue+Cincinnati+OH'
# format: address# + address street + address street type + city + state
maps_destination = '5700+Brecksville+Road+Independence+OH'

##r = requests.get('https://api.github.com/events')
##req = requests.get(
##                    'https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial'+
##                    '&origins=' + maps_origin +
##                    '&destinations=' + maps_destination +
##                    '&key=' + maps_api_token +
##                    '&departure_time=now'+
##                    '&traffic_model=pessimistic'
##                    )
##j = req.json()
##print(j)
##print('\n')
##dump_main = json.dumps([s['elements'] for s in j['rows']], indent = 2)
##
##load_main = json.loads(dump_main)
##
##duration = load_main[0][0]['duration']['text']
##traffic = load_main[0][0]['duration_in_traffic']['text']
##
##duration_str = json.dumps(duration)
##traffic_str = json.dumps(traffic)
##
##duration_str = duration_str.replace('"','')
##
##print(duration_str)
##print(traffic_str)
@contextmanager
def setlocale(name): #thread proof function to work with locale
    with LOCALE_LOCK:
        saved = locale.setlocale(locale.LC_ALL)
        try:
            yield locale.setlocale(locale.LC_ALL, name)
        finally:
            locale.setlocale(locale.LC_ALL, saved)
with setlocale(ui_locale):
    now = datetime.datetime.now()

    d = datetime.datetime.strptime('23:30','%H:%M')

    print(now)
    print(d)

    if(now.time() < d.time()):
        print('True')

