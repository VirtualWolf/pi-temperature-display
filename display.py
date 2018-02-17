#!/usr/bin/env python3
import requests
import os
from papirus import PapirusTextPos

outdoor = requests.get(os.environ['REST_ENDPOINT_OUTDOOR'])
indoor = requests.get(os.environ['REST_ENDPOINT_INDOOR'])
text = PapirusTextPos(False) # Don't update the screen immediately

outdoor_formatted = outdoor.json()['temperature'] + '\u00B0 and ' + str(outdoor.json()['humidity']) + '%'
indoor_formatted = indoor.json()['temperature'] + '\u00B0 and ' + str(indoor.json()['humidity']) + '%'

text.AddText('Outdoor', 0, 0, size=24, fontPath='/usr/share/fonts/truetype/freefont/FreeSansBold.ttf')
text.AddText(outdoor_formatted, 0, 24, fontPath='/usr/share/fonts/truetype/freefont/FreeSans.ttf')

text.AddText('Indoor', 0, 52, size=24, fontPath='/usr/share/fonts/truetype/freefont/FreeSansBold.ttf')
text.AddText(indoor_formatted, 0, 76, fontPath='/usr/share/fonts/truetype/freefont/FreeSans.ttf')

text.WriteAll()
