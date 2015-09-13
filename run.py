#Import
import pifm
import glob, os

#Setup Vars
songs = [""]

#Find Music in directory
os.chdir("Music")
for file in glob.glob("*.wav"):
    currentid = currentid + 1
    print(file)
    songs.append(file)


os.chdir("..")
while True:
	pifm.play(str(songs[random.randint(1,len(songs)-1)]))
	pifm.play_message()
