#!/usr/bin/python

from subprocess import call

def play( filename ):
   call(["./pifm", filename, "88.0", "88307"])
   return

def play_message():
	call(["./WelcomeMessage"])
	return 