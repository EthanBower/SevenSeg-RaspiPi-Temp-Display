#This script will read the current CPU temperature and output it to the seven segment displays
#Here is a diagram of the segment display:
# _________
#|    c    |
#|  -----  |
#|b|     |d|
#| |     | |
#|  --a--  |
#|e|     |g|
#| |     | |
#|  --f--  |
#|_________|

import RPi.GPIO as gpio
import time
import sys
import os

dictonary = {
  'seg_1a' : 7, 'seg_1b' : 11, 'seg_1c' : 12, 'seg_1d' : 13, 'seg_1e' : 15, 'seg_1f' : 16, 'seg_1g' : 18,
  'seg_2a' : 40, 'seg_2b' : 38, 'seg_2c' : 37, 'seg_2d' : 36, 'seg_2e' : 35, 'seg_2f' : 33, 'seg_2g' : 32
  }

def initializeGPIO(): #this is responsible for doing basic setup on the GPIO pins. it will set the referance to BOARD and set everything in the dictionary to gpio.OUT
  gpio.setmode(gpio.BOARD) #tell raspi that i want to referance the physical pin number, not by CPU number
  for segmentName, pinValue in dictonary.items(): #this for loop will look at everything in the dictonary and set those pins to gpio.OUT
    gpio.setup(dictonary[segmentName],gpio.OUT)

def get_temp(): #this will get the CPU temp
  temp = os.popen("vcgencmd measure_temp").readline() #do a terminal command which reads temp
  temp = temp.replace("temp=","") #removes temp=, which was given from console command
  temp = temp.replace("'C","") #removes 'C
  temp = temp.rstrip("\n\r") #removes the newline that the console command gave
  temp = int(float(temp)) #converts string to float, and float to int. gets rid of decimal point as well due to int properties
  return (temp) #return temp in

def errordisplay(): #display "Er" if overheating OR temp is too cool (under 10C)
  gpio.output(dictonary["seg_2a"], 1)
  gpio.output(dictonary["seg_2b"], 1)
  gpio.output(dictonary["seg_2c"], 1)
  gpio.output(dictonary["seg_2d"], 0)
  gpio.output(dictonary["seg_2e"], 1)
  gpio.output(dictonary["seg_2f"], 1)
  gpio.output(dictonary["seg_2g"], 0)
  
  gpio.output(dictonary["seg_1a"], 1)
  gpio.output(dictonary["seg_1b"], 0)
  gpio.output(dictonary["seg_1c"], 0)
  gpio.output(dictonary["seg_1d"], 0)
  gpio.output(dictonary["seg_1e"], 1)
  gpio.output(dictonary["seg_1f"], 0)
  gpio.output(dictonary["seg_1g"], 0)


def segment_output(segment, number): #segment specifies which segment the number will be displayed on. number is the number to be outputted
  if number == 0:
    gpio.output(dictonary[segment + "a"], 0)
    gpio.output(dictonary[segment + "b"], 1)
    gpio.output(dictonary[segment + "c"], 1)
    gpio.output(dictonary[segment + "d"], 1)
    gpio.output(dictonary[segment + "e"], 1)
    gpio.output(dictonary[segment + "f"], 1)
    gpio.output(dictonary[segment + "g"], 1) 
  elif number == 1:
    gpio.output(dictonary[segment + "a"], 0)
    gpio.output(dictonary[segment + "b"], 0)
    gpio.output(dictonary[segment + "c"], 0)
    gpio.output(dictonary[segment + "d"], 1)
    gpio.output(dictonary[segment + "e"], 0)
    gpio.output(dictonary[segment + "f"], 0)
    gpio.output(dictonary[segment + "g"], 1)
  elif number == 2:
    gpio.output(dictonary[segment + "a"], 1)
    gpio.output(dictonary[segment + "b"], 0)
    gpio.output(dictonary[segment + "c"], 1)
    gpio.output(dictonary[segment + "d"], 1)
    gpio.output(dictonary[segment + "e"], 1)
    gpio.output(dictonary[segment + "f"], 1)
    gpio.output(dictonary[segment + "g"], 0)
  elif number == 3:
    gpio.output(dictonary[segment + "a"], 1)
    gpio.output(dictonary[segment + "b"], 0)
    gpio.output(dictonary[segment + "c"], 1)
    gpio.output(dictonary[segment + "d"], 1)
    gpio.output(dictonary[segment + "e"], 0)
    gpio.output(dictonary[segment + "f"], 1)
    gpio.output(dictonary[segment + "g"], 1)
  elif number == 4:
    gpio.output(dictonary[segment + "a"], 1)
    gpio.output(dictonary[segment + "b"], 1)
    gpio.output(dictonary[segment + "c"], 0)
    gpio.output(dictonary[segment + "d"], 1)
    gpio.output(dictonary[segment + "e"], 0)
    gpio.output(dictonary[segment + "f"], 0)
    gpio.output(dictonary[segment + "g"], 1)
  elif number == 5:
    gpio.output(dictonary[segment + "a"], 1)
    gpio.output(dictonary[segment + "b"], 1)
    gpio.output(dictonary[segment + "c"], 1)
    gpio.output(dictonary[segment + "d"], 0)
    gpio.output(dictonary[segment + "e"], 0)
    gpio.output(dictonary[segment + "f"], 1)
    gpio.output(dictonary[segment + "g"], 1)
  elif number == 6:
    gpio.output(dictonary[segment + "a"], 1)
    gpio.output(dictonary[segment + "b"], 1)
    gpio.output(dictonary[segment + "c"], 1)
    gpio.output(dictonary[segment + "d"], 0)
    gpio.output(dictonary[segment + "e"], 1)
    gpio.output(dictonary[segment + "f"], 1)
    gpio.output(dictonary[segment + "g"], 1)
  elif number == 7:
    gpio.output(dictonary[segment + "a"], 0)
    gpio.output(dictonary[segment + "b"], 0)
    gpio.output(dictonary[segment + "c"], 1)
    gpio.output(dictonary[segment + "d"], 1)
    gpio.output(dictonary[segment + "e"], 0)
    gpio.output(dictonary[segment + "f"], 0)
    gpio.output(dictonary[segment + "g"], 1)
  elif number == 8:
    gpio.output(dictonary[segment + "a"], 1)
    gpio.output(dictonary[segment + "b"], 1)
    gpio.output(dictonary[segment + "c"], 1)
    gpio.output(dictonary[segment + "d"], 1)
    gpio.output(dictonary[segment + "e"], 1)
    gpio.output(dictonary[segment + "f"], 1)
    gpio.output(dictonary[segment + "g"], 1)
  elif number == 9:
    gpio.output(dictonary[segment + "a"], 1)
    gpio.output(dictonary[segment + "b"], 1)
    gpio.output(dictonary[segment + "c"], 1)
    gpio.output(dictonary[segment + "d"], 1)
    gpio.output(dictonary[segment + "e"], 0)
    gpio.output(dictonary[segment + "f"], 0)
    gpio.output(dictonary[segment + "g"], 1)
    
try: #Run this chunk of code. If an error occurs, go to one of the excepts
  initializeGPIO()
  
  while True:
    temp = get_temp()
    if temp >= 9 and temp < 100: #if two digits are used
      segment_output("seg_2", int(str(temp)[0:1]))
      segment_output("seg_1", int(str(temp)[1:2]))
    else:
      errordisplay()
    time.sleep(10)
      
except KeyboardInterrupt: #Run this expeption is CTRL+C is pressed
    print("CTRL+C has been pressed. Turning off the seven segment displays.")
  
except:  
    print("An error has occured. Turning off the seven segment displays.") 
  
finally: #This assures that every gpio pin is turned off safely   
    gpio.cleanup()
    sys.exit()
