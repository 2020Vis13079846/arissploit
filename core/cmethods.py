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
import imp
import traceback
import curses
import time
import importlib
import glob

# Import getpath for lib path
from core import getpath

# Append lib path
sys.path.append(getpath.lib())

# Import core modules

from core import helptable
from core import helpin
from core import info
from core import colors
from core import moduleop
from prettytable import PrettyTable
import core.cowsay
import core.matrix
import core.sky
from core import mscop
from core import value_holder
from core import moddbparser
from core.messages import *
from core.apistatus import *

# Import exceptions
from core.exceptions import UnknownCommand
from core.exceptions import ModuleNotFound
from core.exceptions import VariableError

class Cmethods:

	# Module manager object

	mm = None
	modadd = None

	# Init

	def __init__(self, mmi):
		self.mm = mmi

	# Module custom commands

	def mcu(self, command):
		try:
			if command[0] in self.modadd.customcommands.keys():
				call = getattr(self.modadd, command[0])
				try:
					return call(command[1:])
				except Exception as e:
					print("["+colors.bold+colors.red+"err"+colors.end+"] Unexpected error in module:\n")
					traceback.print_exc(file=sys.stdout)
					print(colors.end)
					if api.enabled == True:
						raise
			else:
				raise UnknownCommand("["+colors.bold+colors.red+"err"+colors.end+"] Unrecognized command!")
		except AttributeError:
			raise UnknownCommand("["+colors.bold+colors.red+"err"+colors.end+"] Unrecognized command!")

	# Built-in commands
	
	def exit(self, args):
		if self.mm.moduleLoaded == 1:
			self.mm.moduleLoaded = 0
			self.mm.moduleName = ""
		else:
			sys.exit()

	def clear(self, args):
		if len(args) != 0 and args[0] == "tmp":
			mscop.clear_tmp()
		else:
			sys.stderr.write("\x1b[2J\x1b[H")

	def os(self, args):
		CYAN = '\033[1;34m'
		ENDL = '\033[0m'
		os.system(' '.join(args))

	def help(self, args):
		print("")
		if self.mm.moduleLoaded == 0:
			print(helptable.generateTable(helpin.commands))
		else:
			try: 
				print(helptable.generatemTable(helpin.mcommands, self.modadd.customcommands))
			except AttributeError:
				print(helptable.generateTable(helpin.mcommands))
			try:
				print('\n',self.modadd.help_notes,'\n')
			except AttributeError:
				pass
		print("")

	def version(self, args):
		if self.mm.moduleLoaded == 1:
			try:
				print(self.modadd.conf["name"]+" "+self.modadd.conf["version"])
			except:
				print("["+colors.bold+colors.red+"err"+colors.end+"] Unexpected error in module:\n")
				traceback.print_exc(file=sys.stdout)
				print(colors.end)
				if api.enabled == True:
					raise
		else:
			print("Arissploit Framework " + info.version + " " + info.codename)

	def ifconfig(self, args):
		os.system("ifconfig"+" "+' '.join(args))

	def scan(self, args):
		network_scanner = importlib.import_module("core.network_scanner")
		network_scanner.scan()
		del network_scanner

	def use(self, args):
		if args == "":
			printError("Please enter module name!")
			sys.exit()
		init = False
		if "modules."+args[0] not in sys.modules:
			init = True

		if self.mm.moduleLoaded == 0:
			try:
				self.modadd = importlib.import_module("modules."+args[0])
				self.mm.moduleLoaded = 1
				self.mm.setName(self.modadd.conf["name"])
				try:
					print(self.modadd.conf["message"])
				except KeyError:
					pass
				try:
					if self.modadd.conf["outdated"] == 1:
						printWarning("This module is outdated and might not be working!")
				except KeyError:
					pass
				try:
					if self.modadd.conf["needroot"] == 1:
						if not os.geteuid() == 0:
							printWarning("This module requires root permissions!")
				except KeyError:
					pass
				if init == True:
					try:
						self.modadd.init()
					except AttributeError:
						pass
			except ImportError:
				print("["+colors.bold+colors.red+"err"+colors.end+"] Module is not found!")
				raise ModuleNotFound("["+colors.bold+colors.red+"err"+colors.end+"] Module is not found!")
			except IndexError:
				print("["+colors.bold+colors.red+"err"+colors.end+"] Module is not found!")
				raise ModuleNotFound("["+colors.bold+colors.red+"err"+colors.end+"] Module is not found!")
			except:
				print("["+colors.bold+colors.red+"err"+colors.end+"] Unexpected error in module:\n")
				traceback.print_exc(file=sys.stdout)
				print(colors.end)
				if api.enabled == True:
					raise
		else:
			raise UnknownCommand("["+colors.bold+colors.red+"err"+colors.end+"] Module in use!")

	def modules(self, args):
		try:
			if 1:
				t = PrettyTable([colors.bold+'Modules:', ''+colors.end])
				t.align = 'l'
				t.valing = 'm'
				t.border = False
				xml = moddbparser.parsemoddb()
				root = xml[0]
				for category in root:
					if category.tag == "category":
						t.add_row(["", ""])
						t.add_row([colors.red+colors.uline+category.attrib["name"]+colors.end, colors.red+colors.uline+"Description"+colors.end])

					for item in category:
						if item.tag == "module":
							for child in item:
								if child.tag == "shortdesc":
									t.add_row([item.attrib["name"], child.text])
									break
				print("")
				print(t)
				print("")

	def options(self, args):
		try:
			moduleop.printoptions(self.modadd)
		except:
			print("["+colors.bold+colors.red+"err"+colors.end+"] Unexpected error in module:\n")
			traceback.print_exc(file=sys.stdout)
			print(colors.end)
			if api.enabled == True:
				raise
		except IndexError:
			raise UnknownCommand("["+colors.bold+colors.red+"err"+colors.end+"] Unrecognized command!")

	def back(self, args):
		if self.mm.moduleLoaded == 1:
			self.mm.moduleLoaded = 0
			self.mm.moduleName = ""
		else:
			raise UnknownCommand("["+colors.bold+colors.red+"err"+colors.end+"] Unrecognized command!")

	def reload(self, args):
		try:
			if self.mm.moduleLoaded == 0:
				try:
					mod = "modules."+args[0]
					if mod in sys.modules:
						value_holder.save_values(sys.modules[mod].variables)
						importlib.reload(sys.modules[mod])
						value_holder.set_values(sys.modules[mod].variables)
						try:
							self.modadd.init()
						except AttributeError:
							pass
						print("["+colors.bold+colors.green+"suc"+colors.end+"] Module "+ args[0] +" reloaded!"+colors.end)
					else:
						importlib.import_module(mod)
						try:
							self.modadd.init()
						except AttributeError:
							pass
						print("["+colors.bold+colors.green+"suc"+colors.end+"] Module "+ args[0] +" imported!"+colors.end)

				except IndexError:
					print (colors.red+"Please enter module's name"+colors.end)
			else:
				try:
					mod = "modules."+args[0]
					if mod in sys.modules:
						value_holder.save_values(sys.modules[mod].variables)
						importlib.reload(sys.modules[mod])
						value_holder.set_values(sys.modules[mod].variables)
						try:
							self.modadd.init()
						except AttributeError:
							pass				
						print("["+colors.bold+colors.green+"suc"+colors.end+"] Module "+ args[0] +" reloaded!"+colors.end)
					else:
						importlib.import_module(mod)
						try:
							self.modadd.init()
						except AttributeError:
							pass
						print("["+colors.bold+colors.green+"suc"+colors.end+"] Module "+ self.mm.moduleName +" reloaded!"+colors.end)
				except IndexError:
					mod = "modules."+self.mm.moduleName
					if mod in sys.modules:
						value_holder.save_values(sys.modules[mod].variables)
						importlib.reload(sys.modules[mod])
						value_holder.set_values(sys.modules[mod].variables)
						try:
							self.modadd.init()
						except AttributeError:
							pass
						print("["+colors.bold+colors.green+"suc"+colors.end+"] Module "+ self.mm.moduleName +" reloaded!"+colors.end)

					else:
						modadd = importlib.import_module(mod)
						try:
							self.modadd.init()
						except AttributeError:
							pass
						print("["+colors.bold+colors.green+"suc"+colors.end+"] Module "+ self.mm.moduleName +" reloaded!"+colors.end)
		except:
			print("["+colors.bold+colors.red+"err"+colors.end+"] Faced unexpected error during reimporting:\n")
			traceback.print_exc()
			print(colors.end)
			if api.enabled == True:
				raise

	def run(self, args):

		if self.mm.moduleLoaded == 1:
			try:
				return self.modadd.run()

			except KeyboardInterrupt:
				print("["+colors.bold+colors.red+"err"+colors.end+"] Module terminated!"+colors.end)
			except PermissionError:
				printError("Permission denied!")
				return "[err] Permission denied!"
			except:
				print("["+colors.bold+colors.red+"err"+colors.end+"] Unexpected error in module:\n")
				traceback.print_exc(file=sys.stdout)
				print(colors.end)
				if api.enabled == True:
					raise
		else:
			raise UnknownCommand("["+colors.bold+colors.red+"err"+colors.end+"] Module is not loaded!")

	def set(self, args):
		try:
			self.modadd.variables[args[0]][0] = args[1]
			print(colors.bold+args[0] +" ==> "+ str(args[1]) + colors.end)

		except (NameError, KeyError):
			print("["+colors.bold+colors.red+"err"+colors.end+"] Option is not found!")
			raise VariableError("["+colors.bold+colors.red+"err"+colors.end+"] Option is not found!")
		except IndexError:
			print("["+colors.bold+colors.red+"err"+colors.end+"] Invalid value!")
			raise VariableError("["+colors.bold+colors.red+"err"+colors.end+"] Invalid value!")
		except:
			print("["+colors.bold+colors.red+"err"+colors.end+"] Unexpected error in module:\n")
			traceback.print_exc(file=sys.stdout)
			print(colors.end)
			if api.enabled == True:
				raise

	def create(self, args):
		try:
			try:
				completeName = os.path.join(getpath.modules(), args[0]+".py")
				if os.path.exists(completeName):
					print("["+colors.bold+colors.red+"err"+colors.end+"] Module already exists!"+colors.end)

				else:
					mfile = open(completeName, 'w')
					template = os.path.join('core', 'module_template')
					f = open(template, 'r')
					template_contents = f.readlines()
					template_contents[5] = "	\"name\": \""+args[0]+"\", # Module's name (should be same as file name)\n"
					template_contents[11] = "	\"initdate\": \""+(time.strftime("%d.%m.%Y"))+"\", # Initial date\n"
					template_contents[12] = "	\"lastmod\": \""+(time.strftime("%d.%m.%Y"))+"\", # Last modification\n"
					mfile.writelines(template_contents)
					mfile.close()
					printSuccess("Saved to modules/"+ args[0] +".py!")

			except IndexError:
				printError("Please enter module name!")

			except PermissionError:
				printError("Permission denied!")

			except IOError:
				printError("Something went wrong!")

		except IndexError:
			raise UnknownCommand("["+colors.bold+colors.red+"err"+colors.end+"] Unrecognized command!")

	def matrix(self, args):
		try:
			core.matrix.main()
		except KeyboardInterrupt:
			curses.endwin()
			curses.curs_set(1)
			curses.reset_shell_mode()
			curses.echo()
			
	def sky(self, args):
		core.sky.main()

	def cowsay(self, args):
		print(core.cowsay.cowsay("Arissploit Framework"))

	def update(self, args):
		os.system("chmod +x etc/update.sh && etc/update.sh")

	def dependencies(self, args):
		if self.mm.moduleLoaded == 0:
			modules = glob.glob(getpath.modules()+"*.py")
			dependencies = []
			for module in modules:
				try:
					modadd = importlib.import_module("modules."+os.path.basename(module).replace(".py", ""))
					for dep in modadd.conf["dependencies"]:
						if dep not in dependencies:
							dependencies.append(dep)
				except ImportError:
					print("["+colors.bold+colors.red+"err"+colors.end+"] ImportError: "+os.path.basename(module).replace(".py", "")+colors.end)
					break
				except KeyError:
					pass
			for dep in dependencies:
				print(dep)
		else:
			try:
				for dep in self.modadd.conf["dependencies"]:
					print(dep)
			except KeyError:
				printInfo("This module doesn't require any dependencies")
					
	def init(self, args):
		if self.mm.moduleLoaded == 1:
			try:
				self.modadd.init()
				printSuccess("Module has been initialized!")
			except AttributeError:
				printError("This module doesn't have init function!")
		else:
			raise UnknownCommand("["+colors.bold+colors.red+"err"+colors.end+"] Unrecognized command!")

	def redb(self, args):
		if self.mm.moduleLoaded == 1:
			try:
				moduleop.addtodb(self.modadd)
			except PermissionError:
				print("["+colors.bold+colors.red+"err"+colors.end+"] Permission denied!"+colors.end)
			except KeyboardInterrupt:
				print()
			except:
				print("["+colors.bold+colors.red+"err"+colors.end+"] Faced unexpected:\n")
				traceback.print_exc(file=sys.stdout)
				print(colors.end)
				if api.enabled == True:
					raise

		else:
			if True:
				try:
					modules = glob.glob(getpath.modules()+"*.py")
					for module in modules:
						module = module.replace(getpath.modules(), '').replace('.py', '')
						if module != '__init__' and module != "test":
							modadd = importlib.import_module("modules."+module)
							moduleop.addtodb(modadd)
				except PermissionError:
					print("["+colors.bold+colors.red+"err"+colors.end+"] Permission denied!"+colors.end)
				except KeyboardInterrupt:
					print()
				except:
					print("["+colors.bold+colors.red+"err"+colors.end+"] Faced unexpected:\n")
					traceback.print_exc(file=sys.stdout)
					print(colors.end)
					if api.enabled == True:
						raise
