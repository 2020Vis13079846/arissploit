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
import threading, queue
import itertools
from os.path import relpath
from core import getpath
import os

conf = {
	"name": "wordlist_gen", # Module's name (should be same as file name)
	"version": "1.0", # Module version
	"shortdesc": "Wordlist generator.", # Short description
	"author": "Entynetproject", # Author
	"initdate": "26.12.2016", # Initial date
	"lastmod": "3.1.2017",
	"apisupport": True, # Api support
}

# List of the variables
variables = OrderedDict((
	("output", ["", "Output file."]),
	("chars", ["num_", "Chars."]),
	("maxlen", [4, "Max length of word."]),
	("minlen", [3, "Min length or word."]),
))

# Additional notes to options
option_notes = colors.green+" Values  Chars" + colors.end+"\n ------  ----- \n sc_  ->  a-z\n bc_  ->  A-Z\n num_ ->  0-9\n spc_ ->  !@#$%^&*?,()-=+[]/;"

# Simple changelog
changelog = "Version 1.0:\nrelease"

customcommands = {
	"addchar": "Add more chars.",
}

addchr = ""

def init():
	variables["output"][0] = relpath(getpath.db() + "wordlist", getpath.main_module())
	
class StatHolder:
	kill = False

	def __init__(self):
		self.kill = False

	def reset(self):
		self.kill = False

class Worker(threading.Thread):
	sh = None
	chars = None
	lenmax = None
	lenmin = None

	def __init__(self, sh, lenmax, lenmin, chars):
		self.sh = sh
		self.lenmax = lenmax
		self.lenmin = lenmin
		self.chars = chars
		threading.Thread.__init__(self)

	def run(self):
		ouput = variables["output"][0]
		
		if output == "":
		    printError("No output file specified!")
		    return ModuleError("No output file specified!")
		else:
		    direct = os.path.split()
		    
		    if os.path.exists(direct):
			if os.path.isdir(direct):
			    f = open(output, "a")
			else:
			    printError("Error: "+direct+": not a directory!")
			    return ModuleError("Error: "+direct+": not a directory!")
		    else:
			printError("Local directory: "+direct+": does not exist!")
			return ModuleError("Local directory: "+direct+": does not exist!")
		
		for L in range(self.lenmin, self.lenmax):
			for word in itertools.combinations_with_replacement(self.chars, L):
				if self.sh.kill == True:
					f.close()
					return
				word = ''.join(word)
				f.write(word+"\n")

		f.close()

def run():
	global addchr
	smchars = "abcdefghijklmnopqrstuvwxyz"
	bgchars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	nums = "01223456789"
	scmarks = "!@#$%^&*?,()-=+[]/;"
	chars = ""

	chars += addchr
	if "sc_" in variables["chars"][0]:
		chars += smchars
	if "bc_" in variables["chars"][0]:
		chars += bgchars
	if "num_" in variables["chars"][0]:
		chars += nums
	if "spc_" in variables["chars"][0]:
		chars += scmarks

	try:
		variables["maxlen"][0] = int(variables["maxlen"][0])
	except ValueError:
		printError("Invalid maxlen!")
		return ModuleError("Invalid maxlen!")

	try:
		variables["minlen"][0] = int(variables["minlen"][0])
	except ValueError:
		printError("Invalid minlen!")
		return ModuleError("Invalid minlen!")

	sh = StatHolder()
	sh.reset()
	threads = []

	d = variables["maxlen"][0] - variables["minlen"][0]

	if d < 0:
		printError("Minlen can't be greater than minlen!")
		return ModuleError("Minlen can't be greater than minlen!")
	for i in range(variables["minlen"][0], variables["maxlen"][0]+1):
		t = Worker(sh, i+1, i, chars)
		threads.append(t)
		t.start()

	printInfo(colors.bold+"Generating..."+colors.end)
	try:
		for thread in threads:
			thread.join()
	except KeyboardInterrupt:
		sh.kill = True
		printInfo("Wordlist generator terminated!")

	printSuccess("Wordlist genereted!")

def addchar(args):
	global addchr
	try:
		addchr += args[0]
		return "[suc] Chars added."
	except IndexError:
		printError("Args not given!")
		return ModuleError("Args not given!")
