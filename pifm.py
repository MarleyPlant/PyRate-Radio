#!/usr/bin/python

from subprocess import call
import os

def play(filename):
   os.system("sudo ./pyfm " + filename + " 88.0 " + " 46485" + " stereo")

def play_message():
	os.system("./WelcomeMessage")
