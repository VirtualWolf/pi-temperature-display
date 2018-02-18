#!/usr/bin/env python3
import requests
import os
import arrow
from papirus import PapirusTextPos

outdoor = requests.get(os.environ['REST_ENDPOINT_OUTDOOR'])
indoor = requests.get(os.environ['REST_ENDPOINT_INDOOR'])
text = PapirusTextPos(False) # Don't update the screen immediately

outdoor_temperature_formatted = outdoor.json()['temperature'] + '\u00B0'
indoor_temperature_formatted = indoor.json()['temperature'] + '\u00B0'

outdoor_humidity_formatted = str(outdoor.json()['humidity']) + '%'
indoor_humidity_formatted = str(indoor.json()['humidity']) + '%'

timestamp = arrow.get(int(outdoor.json()['timestamp'])/1000).to(os.environ['TIMEZONE']).format('HH:mm')

text.AddText(timestamp, 164, -2, size=12, fontPath='/usr/share/fonts/truetype/freefont/FreeSansBold.ttf')

text.AddText('Outdoor', 0, -2, size=12, fontPath='/usr/share/fonts/truetype/freefont/FreeSansBold.ttf')
text.AddText(outdoor_temperature_formatted, 0, 3, size=48, fontPath='/usr/share/fonts/truetype/freefont/FreeSans.ttf')
text.AddText(outdoor_humidity_formatted, 140, 19, size=28, fontPath='/usr/share/fonts/truetype/freefont/FreeSans.ttf')

text.AddText('Indoor', 0, 47, size=12, fontPath='/usr/share/fonts/truetype/freefont/FreeSansBold.ttf')
text.AddText(indoor_temperature_formatted, 0, 52, size=48, fontPath='/usr/share/fonts/truetype/freefont/FreeSans.ttf')
text.AddText(indoor_humidity_formatted, 140, 70, size=28, fontPath='/usr/share/fonts/truetype/freefont/FreeSans.ttf')

text.WriteAll()
