#Import
import pifm
import glob, os
import random
import time

#Setup Vars
songs = [""]
randomNum = 0

#Find Music in directory
os.chdir("Music")
for file in glob.glob("*.wav"):
    songs.append("Music/" + file)

os.chdir("..")
while True:
	randomNum = random.randint(1,len(songs)-1)
	print("Playing Song: " + str(songs[randomNum]))
	pifm.play(str(songs[randomNum]))
	pifm.play_message()
	time.sleep(1.5)
