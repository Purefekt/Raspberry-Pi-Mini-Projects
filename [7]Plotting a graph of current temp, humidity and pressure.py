from sense_hat import SenseHat
import matplotlib.pyplot as plt
import time

def plot(filename):
  #define two lists
  temp_list = []
  humi_list = []
  
  try:
    #open the file for read
    file = open(filename,'r')
    #break file content into lines
    lines = file.readlines()
    
    #go through all lines and dplit lines by ','
    for line in lines:
      values = line.split(',')
      temp_list.append(float(values[0]))
      humi_list.append(float(values[1]))
  finally:
    file.close()
  
  #create graph using the plot function from matplotlib
  #arguments of the plot function: x values, y values, line_type
  plt.plot(range(1,len(temp_list)+1),temp_list,'r--')
  plt.plot(range(1,len(humi_list)+1),humi_list,'b--')
  plt.title('Weather')
  plt.xlabel('Measurements')
  plt.ylabel('Value')
  plt.show()
def main():
  sense = SenseHat()
  #time() - return the time in seconds
  start_time = time.time()
  stop_time = time.time()
  
  filename = 'weather.txt'
  #open file for append
  file = open(filename, 'a')
  print("Data acquisition is starting...")
  
  while stop_time - start_time < 5:
    file.write(str(sense.get_temperature())+','+str(sense.get_humidity()))
    file.write('\n')
    stop_time = time.time()
  print('Stop data acquisition!')
  file.close()
  plot(filename)

if __name__ == '__main__':
  main()