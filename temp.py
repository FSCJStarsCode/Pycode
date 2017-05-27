from sense_hat import SenseHat
import time

sense = SenseHat()

#Take one temp reading every second for 5 seconds
print("Please Wait...")
t1 = sense.get_temperature()
time.sleep(1)
t2 = sense.get_temperature()
time.sleep(1)
t3 = sense.get_temperature()
time.sleep(1)
t4 = sense.get_temperature()
time.sleep(1)
t5 = sense.get_temperature()
time.sleep(1)



#run forever
while True:
	#un-comment to slow loop
	time.sleep(1)
	#get temp everytime the loop runs, conv to F for cmd line output
	t = sense.get_temperature()*1.8+32

	#average out the first temp readings, conv to F for cmd line output
	avtemp = ((t1+t2+t3+t4+t5)/5)*1.8+32
    
	#set vars for colours
	red = 0
	green = 0
	blue = 0

	#output to cmd line
	print("------")
	print(round(avtemp,2))
	print(round(t,2))

	#decide if current temp is higher or lower then first readings and set colour
	if (t - avtemp > 0.1):
		red = 255
	elif (t - avtemp < -0.1):
		blue = 255
	else:
		green = 255

	sense.clear(red,green,blue)