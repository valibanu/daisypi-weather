import os
import requests
import xively
import time
import datetime

# extract feed_id and api_key from environment variables
FEED_ID = os.environ["FEED_ID"]
API_KEY = os.environ["API_KEY"]

# initialize api client
api = xively.XivelyAPIClient(API_KEY)

# initilalize SHT11 object
from sht1x.Sht1x import Sht1x as SHT1x
dataPin = 11
clkPin = 15
sht1x = SHT1x(dataPin, clkPin, SHT1x.GPIO_BOARD)

# Initialise the BMP085 and use STANDARD mode (default value)
from Adafruit_BMP085.Adafruit_BMP085 import BMP085
bmp = BMP085(0x77)


# function to return a datastream object. This either creates a new datastream,
# or returns an existing one
def get_datastream(feed, datastream_name):
  try:
    datastream = feed.datastreams.get(datastream_name)
    return datastream
  except:
    tag = "{}_01".format(datastream_name.lower().split('_')[0])
    datastream = feed.datastreams.create(datastream_name, tags=tag)
    return datastream

def round_to_two_decimals(float_nr):
  return int(float_nr * 100) / 100.0

def run():
  feed = api.feeds.get(FEED_ID)
  measurements = {"Temperatura": 0, "Presiune_Atmosferica": 0, "Umiditatea_Aerului": 0}
  for measurement in measurements:
    datastream = get_datastream(feed, measurement)
    datastream.max_value = None
    datastream.min_value = None

  while True:
    # read temperature & humidity from SHT11
    temp_sht11x = sht1x.read_temperature_C()
    humidity = sht1x.read_humidity()

    # read temperature & air pressure from BMP085
    temp_bmp085 = bmp.readTemperature()
    pressure = bmp.readPressure()

    measurements["Temperatura"] = round_to_two_decimals((temp_sht11x + temp_bmp085) / 2)
    measurements["Presiune_Atmosferica"] = int(pressure)
    measurements["Umiditatea_Aerului"] = round_to_two_decimals(humidity)

    for measurement in measurements:
      datastream = get_datastream(feed, measurement)   
      datastream.current_value = measurements[measurement]
      datastream.at = datetime.datetime.utcnow()
      try:
        datastream.update()
      except requests.HTTPError as e:
        print "HTTPError({0}): {1}".format(e.errno, e.strerror)
    time.sleep(60)
 
run()
