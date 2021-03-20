from sense_hat import SenseHat

sense = SenseHat()

p = sense.get_pressure()
P = (p/1013.25) #P/P0
c = (1/5.2558) 
PP = pow(P, c) #(P/P0)^(1/5.2558)
#Altitude
A = 44331 * (1-PP)

print('Your altitiude is: ' + str(A) + 'm')