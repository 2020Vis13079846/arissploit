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
import os
import traceback

# Append
sys.path.append(os.path.dirname(os.path.realpath(__file__)))

# Import core modules
from core import command_handler
from core.module_manager import ModuleManager
from core.apistatus import *
api.enabled = True

# Exceptions
import core.exceptions

class arissploitapi:
	mm = None
	ch = None
	allowPrint = False
	ModuleError = False

	def disablePrint(self):
		if self.allowPrint == False:
			f = open(os.devnull, 'w')
			sys.stdout = f

	def enablePrint(self):
		if self.allowPrint == False:
			sys.stdout = sys.__stdout__

	def __init__(self, allowPrint):
		self.allowPrint = allowPrint
		self.mm = ModuleManager
		self.ch = command_handler.Commandhandler(self.mm, True)

	def loadModule(self, module):
		self.disablePrint()
		try:
			self.ch.handle("use "+module)
			modadd = sys.modules["modules."+module]
			if modadd.conf['apisupport'] == False:
				raise ApiNotSupported("["+colors.bold+colors.red+"err"+colors.end+"] This module doesn't support API!")
		except core.exceptions.ModuleNotFound:
			self.enablePrint()
			raise ModuleNotFound("["+colors.bold+colors.red+"err"+colors.end+"] Module is not found!")
		except:
			self.enablePrint()
			raise

		self.enablePrint()

	def unloadModule(self):
		self.disablePrint()
		try:
			self.ch.handle("back")
		except:
			self.enablePrint()
			raise
		self.enablePrint()

	def setVariable(self, target, value):
		self.disablePrint()
		try:
			self.ch.handle("set "+target+" "+value)
		except core.exceptions.VariableError:
			self.enablePrint()
			raise VariableError("["+colors.bold+colors.red+"err"+colors.end+"] Variable is not found!")
		except:
			self.enablePrint()
			raise

		self.enablePrint()

	def runModule(self):
		self.ModuleError = False
		self.disablePrint()
		try:
			answer = self.ch.handle("run")
		except:
			self.enablePrint()
			raise
		self.enablePrint()

		if type(answer) is core.exceptions.ModuleError:
			self.ModuleError = True

		return answer

	def customCommand(self, command):
		self.disablePrint()
		try:
			answer = self.ch.handle(command)
		except:
			self.enablePrint()
			raise

		self.enablePrint()
		return answer

	def runCommand(self, command):
		self.disablePrint()
		try:
			self.ch.handle(command)
		except:
			self.enablePrint()
			raise

		self.enablePrint()


class ModuleNotFound(Exception):
	pass

class VariableError(Exception):
	pass

class ApiNotSupported(Exception):
	pass
