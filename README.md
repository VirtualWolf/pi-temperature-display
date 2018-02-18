# Pi Temperature Display
This is a simple example Python 3 script for use with the Raspberry Pi Zero and [PaPiRus ePaper display](https://www.pi-supply.com/product/papirus-zero-epaper-screen-phat-pi-zero/). To be used in conjunction with my [Pi Sensor Reader](https://bitbucket.org/VirtualWolfCo/pi-sensor-reader) Node.js app (or at least it expects data in the same format as that produces). It assumes the display size is the 2.0" 200x96-sized display.

This script runs once then exits, so can be triggered via `cron` to update on a schedule.

## Example usage
    TIMEZONE="Australia/Sydney" \
    REST_ENDPOINT_OUTDOOR="https://example.com/outdoor" \
    REST_ENDPOINT_INDOOR="https://example.com/indoor" \
    ./display.py
