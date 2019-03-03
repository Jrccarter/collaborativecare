import matplotlib.pyplot as plt
import random
import numpy as np
import math
import smtplib
import serial



insul = 0
carbo = 60

ser = serial.Serial('/dev/tty.usbserial', 9600)
while True:
    print ser.readline()
#this calculates the amount of insuling to give the patient based on carbs
def insul_Cal(carb):
    return int(carb/13)

#print(str(insul_Cal(carbo)))

#This is the file for the Arduino to read
Ardf =open("Ardfile.txt", "w")
Ardf.write("\n" + str(insul_Cal(carbo)))

#This is the graph
import numpy as np
import math
#x = np.linspace(0,5,50)
#y = []
#for i in range(len(x)):
#    y.append(math.sin(x[i]))


#plt.plot(x,y)
list = [80,60,70,65,63,60,95,179,100,100,100,100,185,120,110,100,100,179,130,
        120,110,100,95,90,85]
output = ""
time = 0
print("time(minutes)"+ "\t" +"Bloodsugar level" )
for num in list:
    if num <60:
        output="Your bloodsugar list is dangerously low get to a hospital immediately"
    if num>59 and num<90:
        output = "Your bloodsugar is low but normal"
    if num>89 and num<120:
        output = "Your bloodsugar is normal"
    if num>119 and num<180:
        output = "Your bloodsugar is high"
    if num>179:
        output = "Your bloodsugar is too high get to a hospital immediately"
        
    print(str(time) + "\t \t" +output)   
    time +=100
    

plt.ylabel("Blood Sugar Levels")
plt.xlabel("Time(hours)")

sam_File = open("Sample.txt")
num =0




plt.plot(list)   
plt.xlim([0,24])
plt.ylim([40,300])
plt.show()