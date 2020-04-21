#!/usr/bin/env python3

#            ---------------------------------------------------
#                           Arissploit Framework                                 
#            ---------------------------------------------------
#                Copyright (C) <2019-2020>  <Entynetproject>
#
#        This program is free software: you can redistribute it and/or modify
#        it under the terms of the GNU General Public License as published by
#        the Free Software Foundation, either version 3 of the License, or
#        any later version.
#
#        This program is distributed in the hope that it will be useful,
#        but WITHOUT ANY WARRANTY; without even the implied warranty of
#        MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#        GNU General Public License for more details.
#
#        You should have received a copy of the GNU General Public License
#        along with this program.  If not, see <http://www.gnu.org/licenses/>.

from core.arissploit import *
from core import colors
import zipfile
import threading, queue
from core import getpath
from os.path import relpath
import os
import sys

conf = {
	"name": "zip_cracker", # Module's name (should be same as file name)
	"version": "1.0", # Module version
	"shortdesc": "Zip file brute-force attack using wordlist.", # Short description
	"author": "Entynetproject", # Author
	"initdate": "22.12.2016", # Initial date
	"lastmod": "3.1.2017",
	"apisupport": True, # Api support
}

# List of the variables
variables = OrderedDict((
	("file", ["", "Target zip file."]),
	("dict", ["", "Dictionary of words."]),
	("tc", [8, "Thread count."]),
	("exto", ["", "Extract directory."])
))

# Simple changelog
changelog = "Version 1.0:\nrelease"

def init():
	variables["exto"][0] = relpath(getpath.tmp(), getpath.main_module())
	variables["dict"][0] = relpath(getpath.db() + "dazzlepod.txt", getpath.main_module())

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
		    printError("No zip file specified!")
		    return ModuleError("No zip file specified!")
		
		file = variables["file"][0]
		
		if os.path.exists(file):
		    zipf = zipfile.ZipFile(file)
		else:
		    printError("Local file: "+file+": does not exist!")
		    return ModuleError("Local file: "+file+": does not exist!")
		
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
				zipf.extractall(variables["exto"][0], pwd=word.encode("utf-8"))
				self.pwdh.pwd = word
				return
			except RuntimeError:
				pass
			except zipfile.BadZipFile:
				pass

def run():
	if variables["dict"][0] == "":
	    printError("No wordlist file specified!")
	    return ModuleError("No wordlist file specified!")
	
	dicti = variables["dict"][0]
		
	if os.path.exists(dicti):
	    wordlist = open(dicti, "rb")
	else:
	    printError("Local file: "+dicti+": does not exist!")
	    return ModuleError("Local file: "+dicti+": does not exist!")
	
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
		printInfo("Brute-force attack terminated!")

	if pwdh.pwd != None:
		printSuccess("Password found: "+pwdh.pwd)
		return pwdh.pwd

	elif pwdh.error != None:
		printError(pwdh.error)
		return ModuleError(pwdh.error)
