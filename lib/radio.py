import glob
from subprocess import call
import os
songs = []
songs_path = []


class antenna:
	def __init__(self, freq, stereo):
		self.frequency = freq
		self.stereo = stereo

	def loadFiles(self):
		os.chdir("music")
		for file in glob.glob("*.wav"):
			songs_path.append(os.path.realpath(file))
			songs.append(file)
		os.chdir("..")

	def stop(self):
		player.kill()

	def play(self, selected):
		print(str(songs_path[selected]))
		player = os.system("./pifm " + str(songs_path[selected]) + " 103.3 22050 stereo")

	def list(self):
		i = 0
		if songs == []:
			for item in songs:
				i = i+1
				print("[" + str(i-1) + "]" + item)
