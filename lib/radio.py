import glob
from subprocess import call
import os

class antenna:
	def __init__(self, freq, stereo):
		self.frequency = freq
		self.stereo = stereo
		self.songs = []
		self.songs_path = []


	def loadFiles(self):
		os.chdir("music")
		for file in glob.glob("*.wav"):
			self.songs_path.append(os.path.realpath(file))
			self.songs.append(file)
		os.chdir("..")

	def stop(self):
		player.kill()

	def play(self, selected):
		player = os.system("./lib/pifm " + str(self.songs_path[selected]) + " 103.3 22050 stereo")

	def list(self):
		i = 0
		if self.songs != []:
			for item in self.songs:
				i = i+1
				print("[" + str(i-1) + "]" + item)
