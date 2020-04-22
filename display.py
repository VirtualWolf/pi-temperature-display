#!/usr/bin/env python3
import requests
import os
import sys
import arrow
from papirus import PapirusTextPos

bold_font = '/usr/share/fonts/truetype/freefont/FreeSansBold.ttf'
standard_font = '/usr/share/fonts/truetype/freefont/FreeSans.ttf'

outdoor = requests.get(os.environ['REST_ENDPOINT_OUTDOOR'])
indoor = requests.get(os.environ['REST_ENDPOINT_INDOOR'])

# Don't update the screen immediately
text = PapirusTextPos(False)

# If called as "display.py partial", only the changed portions of the screen will be updated.
# It's recommended to update the screen with a full refresh every few minutes:
# https://github.com/PiSupply/PaPiRus#full-and-partial-updates
if sys.argv[1] == 'partial':
    text.partialUpdates = True

outdoor_temperature_formatted = outdoor.json()['temperature'] + '\u00B0'
indoor_temperature_formatted = indoor.json()['temperature'] + '\u00B0'

outdoor_humidity_formatted = str(outdoor.json()['humidity']) + '%'
indoor_humidity_formatted = str(indoor.json()['humidity']) + '%'

timestamp = arrow.get(int(outdoor.json()['timestamp'])/1000).to(os.environ['TIMEZONE']).format('HH:mm')

text.AddText(timestamp, 160, -2, size=16, fontPath=bold_font)

text.AddText('Outdoor', 0, -2, size=12, fontPath=bold_font)
text.AddText(outdoor_temperature_formatted, 0, 3, size=48, fontPath=standard_font)
text.AddText(outdoor_humidity_formatted, 130, 14, size=36, fontPath=standard_font)

text.AddText('Indoor', 0, 47, size=12, fontPath=bold_font)
text.AddText(indoor_temperature_formatted, 0, 52, size=48, fontPath=standard_font)
text.AddText(indoor_humidity_formatted, 130, 62, size=36, fontPath=standard_font)

text.WriteAll()
