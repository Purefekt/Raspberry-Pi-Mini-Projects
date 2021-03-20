from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

while True:
  t = sense.get_temperature()
  p = sense.get_pressure()
  h = sense.get_humidity()
  #round() - round the values to some decimal places
  t = round(t,1)
  p = round(p,1)
  h = round(h,1)
  #str() - convert a value to a string
  message = "Temperature: " + str(t) + "C "  + "Pressure: " + str(p) + "hPa " + "Humidity: " + str(h) + "%"
  print(message)
  sleep(1)
 