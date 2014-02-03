from sht1x.Sht1x import Sht1x as SHT1x
dataPin = 11
clkPin = 15
sht1x = SHT1x(dataPin, clkPin, SHT1x.GPIO_BOARD)

temperature = sht1x.read_temperature_C()
humidity = sht1x.read_humidity()
dewPoint = sht1x.calculate_dew_point(temperature, humidity)

print("SHT11 Readings")
print("--------------")
print("Temperature: {:.2f} C".format(temperature))
print("Humidity:    {:.2f} %".format(humidity))
print("Dew Point:   {:.2f} %".format(dewPoint))
print("")

from Adafruit_BMP085.Adafruit_BMP085 import BMP085
# Initialise the BMP085 and use STANDARD mode (default value)
# bmp = BMP085(0x77, debug=True)
bmp = BMP085(0x77)

# To specify a different operating mode, uncomment one of the following:
# bmp = BMP085(0x77, 0)  # ULTRALOWPOWER Mode
# bmp = BMP085(0x77, 1)  # STANDARD Mode
# bmp = BMP085(0x77, 2)  # HIRES Mode
# bmp = BMP085(0x77, 3)  # ULTRAHIRES Mode

temp = bmp.readTemperature()

# Read the current barometric pressure level
pressure = bmp.readPressure()

# To calculate altitude based on an estimated mean sea level pressure
# (1013.25 hPa) call the function as follows, but this won't be very accurate
altitude = bmp.readAltitude()

# To specify a more accurate altitude, enter the correct mean sea level
# pressure level.  For example, if the current pressure level is 1023.50 hPa
# enter 102350 since we include two decimal places in the integer value
# altitude = bmp.readAltitude(102350)

print("BMP085 Readings")
print("---------------")
print("Temperature: {:.2f} C".format(temp))
print("Pressure:    {:.2f} hPa".format(pressure / 100.0))
print("Altitude:    {:.2f}".format(altitude))
