import glob
from subprocess import call
import os
songs = [""]
songs_path = [""]
def refreshFiles():
	os.chdir("Music")
	for file in glob.glob("*.wav"):
		songs_path.append(os.path.realpath(file))
		songs.append(file)
	os.chdir("..")

def stop(stop):
	player.kill()

def play(selected):
	print(str(songs_path[selected]))
	player = os.system("./pifm " + str(songs_path[selected]) + " 103.3 22050 stereo")

def listSongs():
	i = 0
	for item in songs:
		i = i+1
		print("[" + str(i-1) + "]" + item)
