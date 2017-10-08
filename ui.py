import os
import sys
import lib.radio as radio

antenna = radio.antenna(103.3, True)

selected = ""

def clear():
	os.system("clear")

def picksong():
	global selected
	selected = input("Song To Play: ")
	selected = int(selected)

clear()
print("|--------------------------------|")
print("|===========PyRate Radio=========|")
print("|=====http://marleyplant.com=====|")
print("|--------------------------------|")
antenna.loadFiles()
antenna.list()

while True:
	picksong()
	antenna.play(selected)
