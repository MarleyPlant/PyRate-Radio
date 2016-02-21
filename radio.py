import glob
import subprocess
import os
songs = [""]
songs_path = [""]
def refreshFiles():
	os.chdir("Music")
	for file in glob.glob("*.wav"):
		songs_path.append("Music/" + file)
		songs.append(file)

def stop(stop):
	player.kill()

def play(selected):
	print(songs_path[selected])
	player = subprocess.call("./pyfm " + str(songs_path[selected]) + " 103.3 22050 stereo")

def listSongs():
	i = 0
	for item in songs:
		i = i+1
		print("[" + str(i-1) + "]" + item)
