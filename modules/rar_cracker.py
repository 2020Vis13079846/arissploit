#!/usr/bin/env python3

from core.arissploit import *
import rarfile
import threading, queue
from core import getpath
from os.path import relpath
import os
import sys

conf = {
	"name": "rar_cracker", # Module's name (should be same as file name)
	"version": "1.0", # Module version
	"shortdesc": "Rar file brute-force attack.", # Short description
	"author": "Entynetproject", # Author
	"initdate": "25.12.2019", # Initial date
	"lastmod": "3.1.2019",
	"apisupport": True, # Api support
}

# List of the variables
variables = OrderedDict((
	("file", ["", "Input rar file."]),
	("dict", ["", "Dictionary of words."]),
	("tc", [8, "Thread count."]),
	("exto", ["", "Extract directory."])
))

# Simple changelog
changelog = "Version 1.0:\nrelease"

class PwdHolder:
	pwd = None
	error = None
	kill = False

	def __init__(self):
		self.pwd = None
		self.error = None
		self.kill = False

	def reset():
		PwdHolder.pwd = None
		PwdHolder.error = None
		PwdHolder.kill = False

class Worker(threading.Thread):
	pwdh = None
	words = None
	def __init__(self, words, pwdh):
		self.pwdh = pwdh
		self.words = words
		threading.Thread.__init__(self)

	def run(self):
		if variables["file"][0] == "":
			printError("No rar file specified!")
			return ModuleError("No rar file specified!")
		
		file = variables["file"][0]
		
		if os.path.exists(file):
			if os.path.isdir(file):
				printError("Error: "+file+": is a directory!")
				return ModuleError("Error: "+file+": is a directory!")
			else:
				rf = rarfile.RarFile(file)
		else:
			printError("Input file: "+file+": does not exist!")
			return ModuleError("Input file: "+file+": does not exist!")
		
		for word in self.words:
			if self.pwdh.pwd != None:
				return
			elif self.pwdh.error != None:
				return
			elif self.pwdh.kill == True:
				return
			try:
				word = word.decode("utf-8").replace("\n", "")
				if word[0] == "#":
					continue
				#animline("trying password: "+word)
				rf.extractall(path=variables["exto"][0], pwd=word)
				self.pwdh.pwd = word
				return
			except rarfile.RarCRCError:
				pass
			except rarfile.RarUserBreak:
				self.pwdh.kill = True
			except rarfile.RarSignalExit:
				pass


def run():
	if variables["dict"][0] == "":
		printError("No wordlist file specified!")
		return ModuleError("No wordlist file specified!")
	
	dicti = variables["dict"][0]
		
	if os.path.exists(dicti):
		if os.path.isdir(dicti):
			printError("Error: "+dicti+": is a directory!")
			return ModuleError("Error: "+dicti+": is a directory!")
		else:
			wordlist = open(dicti, "rb")
	else:
		printError("Input file: "+dicti+": does not exist!")
		return ModuleError("Input file: "+dicti+": does not exist!")
		
	printInfo("Reading wordlist...")
	words = wordlist.read().splitlines()
	printInfo("Starting brute-force attack...")

	pwdh = PwdHolder
	pwdh.reset()

	try:
		u = int(variables["tc"][0])
	except TypeError:
		printError("Invalid thread count!")
		return ModuleError("Invalid thread count!")
	threads = []

	for i in range(variables["tc"][0]):
		t = Worker(words[i::u], pwdh)
		threads.append(t)
		t.start()
		
	printInfo("Now cracking...")
	try:
		for thread in threads:
			thread.join()
	except KeyboardInterrupt:
		pwdh.kill = True
		printWarning("Brute-force attack terminated.")

	if pwdh.pwd != None:
		printSuccess("Password found: "+pwdh.pwd)
		return pwdh.pwd

	elif pwdh.error != None:
		printError(pwdh.error)
		return ModuleError(pwdh.error)
