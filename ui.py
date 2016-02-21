import os
import sys
import radio

selected = ""

def clear():
	os.system("clear")

def picksong():
	global selected
	selected = raw_input("Song To Play: ")
	selected = int(selected)

clear()
print("|--------------------------------|")
print("|===========PyRate Radio=========|")
print("|=====http://marleyplant.com=====|")
print("|--------------------------------|")
radio.refreshFiles()
radio.listSongs()

picksong()
radio.play(selected)
