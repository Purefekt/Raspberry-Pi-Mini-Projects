from sense_hat import SenseHat
import random
from time import sleep

sense = SenseHat()
speed = 0.4
basket = [7,4] #co-ords of right-most pixel for basket
score = 0

w = (0,0,0)
r = (255,0,0)
b = (0,0,255)

#8x8 pixel space
game_space = [
  w,w,w,w,w,w,w,w,
  w,w,w,w,w,w,w,w,
  w,w,w,w,w,w,w,w,
  w,w,w,w,w,w,w,w,
  w,w,w,w,w,w,w,w,
  w,w,w,w,w,w,w,w,
  w,w,w,w,w,w,w,w,
  w,w,w,b,b,w,w,w]
  
#function to change the color of ONE pixel in the game_space
def update_space(x,y,color):
  p = 8 *x + y
  game_space[p] = color
  sense.set_pixels(game_space)
  
def left(event):
  if event.action == 'pressed':
    if basket[1] - 1 == 0:
      pass #do nothing
    else:
      #clear the right-most pixel > move basket co-ords 1 pixel to the left > redraw on new pixel
      update_space(basket[0],basket[1],w)
      basket[1] -= 1
      update_space(basket[0],basket[1]-1,b)
      
def right(event):
  if event.action == 'pressed':
    if basket[1] + 1 == 8:
      pass #do nothing
    else: #clear left-most pixel > move basket co-ords 1 pixel to the right > redraw on new pixel
      update_space(basket[0],basket[1]-1,w)
      basket[1] += 1
      update_space(basket[0],basket[1],b)
      
sense.stick.direction_left = left
sense.stick.direction_right = right

sense.clear()
sense.set_pixels(game_space)
game_alive = True


while game_alive:
  #ball's values
  x = 0
  y = random.randint(0,7)
  d = random.choice([-1,1]) 
  #d = -1 (move the ball left)
  #d = 1 (move the ball right)
  #
  
  update_space(x,y,r)
  
  while True:
    sleep(speed) #delay between each frame
    update_space(x,y,w)
    
    #Checks if ball hits basket or not
    if x == 7:
      if y == basket[1]-1 or y == basket[1]:
        update_space(x,y,b)
        score += 1
        break
      else:
        game_alive = False
        break
      
    if y == 7 and d == 1:
      d = -1
    elif y == 0 and d == -1:
      d = 1
    
    y += d
    x += 1
    update_space(x,y,r)
    
sense.clear()
sense.show_message('Game over!',scroll_speed=0.05,back_colour=w)
sense.show_message('Score: '+str(score),scroll_speed=0.05, back_colour=w)