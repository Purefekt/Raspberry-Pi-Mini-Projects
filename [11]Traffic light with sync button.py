from sense_hat import SenseHat
import time

sense = SenseHat()
delay_val = 1.0

w = (255,255,255)
n = (0,0,0)

off = [
 n, n, n, n, n, n, n, n,
 n, n, n, n, n, n, n, n,
 n, n, n, n, n, n, n, n,
 n, n, n, n, n, n, n, n,
 n, n, n, n, n, n, n, n,
 n, n, n, n, n, n, n, n,
 n, n, n, n, n, n, n, n,
 n, n, n, n, n, n, n, n
 ]


#ex2 TRAFFIC LIGHT
state = 0
w = (255,255,255)
r = (255,0,0)
g = (0,255,0)
y = (255,255,0)
n = (0,0,0)

red_yellow = [
 n, n, n, r, r, n, n, n,
 n, n, n, r, r, n, n, n,
 n, n, n, n, n, n, n, n,
 n, n, n, y, y, n, n, n,
 n, n, n, y, y, n, n, n,
 n, n, n, n, n, n, n, n,
 n, n, n, n, n, n, n, n,
 n, n, n, n, n, n, n, n
 ]

def out_of_order_state():
 sense.set_pixels(set_state_color(y, "mid"))
 time.sleep(0.5)
 sense.clear()
 time.sleep(0.5)
 
def set_state_controller(color, duration):
  sense.set_pixels(color)
  time.sleep(duration)
  sense.clear()
 
def set_state():
  global state
  # state variable has been defined outside
  if state < 3:
    state += 1
  elif state == 3:
    state = 0
  else:
    pass

def button_event(event):
  global state
  if event.action == 'released':
    if state != 4:
      state = 4
    else:
      state = 3

def set_state_color(col, pos):
  led = list(off);
  ind = 0;
  for i, val in enumerate(led):
    if str(pos) == "top":
      if i == 3 or i == 4 or i == 11 or i == 12:
        led[i] = col
    elif str(pos) == "mid":
      if i == 27 or i == 28 or i == 35 or i == 36:
        led[i] = col
    elif str(pos) == 'down':
      if i == 51 or i == 52 or i == 59 or i == 60:
        led[i] = col
  return led;

flag_state = True  

def halt(event):
  global state
  global flag_state
  if event.action == 'pressed':
    if flag_state:
      flag_state = False
    else:
      flag_state = True
      

sense.stick.direction_down = halt
sense.stick.direction_middle = button_event

while True:
  if state == 0:
    set_state_controller(set_state_color(r, "top"), 3)
  elif state == 1:
    set_state_controller(red_yellow, 1)
  elif state == 2:
    set_state_controller(set_state_color(g, "down"), 2)
  elif state == 3:
    set_state_controller(set_state_color(y, "mid"), 1)
  else:
    out_of_order_state()
  if flag_state:
    set_state()