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

import sys

# Import core modules
from core.module_manager import ModuleManager
from core import colors
from core import command_handler

shellface = "["+colors.bold+"arissploit"+colors.end+"]:"
mm = ModuleManager

def run():
	global shellface
	global mm

	ch = command_handler.Commandhandler(mm, False)

	while True:
		try:
			setFace()
			command = input(shellface+" ")

			ch.handle(command)
		except KeyboardInterrupt:
			if mm.moduleLoaded == 0:
				print()
				sys.exit(0)
			else:
				print()
				mm.moduleLoaded = 0
				mm.moduleName = ""
				print(colors.bold + colors.red + "Ctrl + C detected, going back..." + colors.end)

def setFace():
	global shellface
	global mm
	if mm.moduleLoaded == 0:
		shellface = "["+colors.bold+"arissploit"+colors.end+"]:"
	else:
		shellface = "["+colors.bold+"arissploit"+colors.end+"]"+"("+colors.red+mm.moduleName+colors.end+"):"
