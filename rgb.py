#!/usr/bin/python
from sense_hat import SenseHat

sense = SenseHat()

print("Welcome to the RGB program! Press Ctrl-C to exit\n")

while True:
	try:
		red = int(input("Please enter a number between 0 and 255 for red: "))
		blue = int(input("Please enter a number between 0 and 255 for blue: "))
		green = int(input("Please enter a number between 0 and 255 for green: "))

		sense.clear(red, green, blue)
		print("")
	except KeyboardInterrupt:
		sense.clear(0,0,0)
		print("\nexiting")
		exit()
