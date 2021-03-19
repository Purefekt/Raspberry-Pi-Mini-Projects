from sense_hat import SenseHat
import random
import time
sense = SenseHat()
#Generate a random color
def random_colour():
  #randint - random integer between an interval
  random_red = random.randint(0,255)
  random_green = random.randint(0,255)
  random_blue = random.randint(0,255)
  return (random_red, random_green, random_blue)
sense.show_letter("V",random_colour())
time.sleep(1)
sense.show_letter("E",random_colour())
time.sleep(1)
sense.show_letter("E",random_colour())
time.sleep(1)
sense.show_letter("R",random_colour())
time.sleep(1)
sense.clear()