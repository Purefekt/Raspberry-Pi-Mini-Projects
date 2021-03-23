from sense_hat import SenseHat
from time import sleep
import random

sense = SenseHat()
speed = 0.4
bat = [7,4]
score = 0
up_down = -1

w = (0,0,0) #bg color
r = (255,0,0) #ball color
b = (0,0,255) #bat color

game_space = [
  w,w,w,w,w,w,w,w,
  w,w,w,w,w,w,w,w,
  w,w,w,w,w,w,w,w,
  w,w,w,w,w,w,w,w,
  w,w,w,w,w,w,w,w,
  w,w,w,w,w,w,w,w,
  w,w,w,w,w,w,w,w,
  w,w,w,b,b,w,w,w]
  
def update_space(x,y,color):
  p = 8 * x + y
  game_space[p] = color
  sense.set_pixels(game_space)
  
def left(event):
  if event.action == 'pressed':
    if bat[1] - 1 == 0:
      pass
    else:
      update_space(bat[0], bat[1], w)
      bat[1] -= 1
      update_space(bat[0], bat[1] - 1, b)
  
def right(event):
  if event.action == 'pressed':
    if bat[1] + 1 == 8:
      pass
    else:
      update_space(bat[0], bat[1] - 1, w)
      bat[1] += 1
      update_space(bat[0], bat[1], b)
      
sense.stick.direction_left = left
sense.stick.direction_right = right

sense.clear()
sense.set_pixels(game_space)
game_alive = True

while game_alive:
  x = 0
  y = random.randint(0,7)
  d = random.choice([-1, 1]) #left, right
  
  update_space(x,y,r) #ball vars changed so update ball's pixels (r)
  
  while True:
    sleep(speed)
    #past values of ball must vanish so draw to (w)
    update_space(x,y,w)
    
    if x == 7:
      if y == bat[1] or y == bat[1] - 1:
        #bat pixel and ball pixel overlap so after ball moves update it w bat color (b)
        update_space(x,y,b)
        score += 1
        up_down = 1
      else:
        game_alive = False
        break
    elif  x == 0 and up_down == 1:
      up_down = -1
    
    if y == 7 and d == 1:
      d = -1
    elif y == 0 and d == -1:
      d = 1
      
    if up_down == -1:
      x += 1
    elif up_down == 1:
      x -= 1
      
    y += d
    #ball vars changed so update to (r)
    update_space(x,y,r)
      
sense.clear()
sense.show_message('Game Over!', scroll_speed = 0.05, back_colour = w)
sense.show_message('Score: ' + str(score), scroll_speed = 0.05, back_colour = w)