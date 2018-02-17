#!/usr/bin/env python3
import requests
import os
from papirus import PapirusTextPos

outdoor = requests.get(os.environ['REST_ENDPOINT_OUTDOOR'])
indoor = requests.get(os.environ['REST_ENDPOINT_INDOOR'])
text = PapirusTextPos(False) # Don't update the screen immediately

outdoor_temperature_formatted = outdoor.json()['temperature'] + '\u00B0'
indoor_temperature_formatted = indoor.json()['temperature'] + '\u00B0'

outdoor_humidity_formatted = str(outdoor.json()['humidity']) + '%'
indoor_humidity_formatted = str(indoor.json()['humidity']) + '%'

text.AddText('Outdoor', 0, 0, size=16, fontPath='/usr/share/fonts/truetype/freefont/FreeSansBold.ttf')
text.AddText(outdoor_temperature_formatted, 0, 16, size=32, fontPath='/usr/share/fonts/truetype/freefont/FreeSans.ttf')
text.AddText(outdoor_humidity_formatted, 120, 16, size=32, fontPath='/usr/share/fonts/truetype/freefont/FreeSans.ttf')

text.AddText('Indoor', 0, 48, size=16, fontPath='/usr/share/fonts/truetype/freefont/FreeSansBold.ttf')
text.AddText(indoor_temperature_formatted, 0, 62, size=32, fontPath='/usr/share/fonts/truetype/freefont/FreeSans.ttf')
text.AddText(indoor_humidity_formatted, 120, 62, size=32, fontPath='/usr/share/fonts/truetype/freefont/FreeSans.ttf')

text.WriteAll()
