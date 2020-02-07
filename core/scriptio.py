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

import readline
import sys

# Import core modules
from core.module_manager import ModuleManager
from core import colors
from core import command_handler

mm = ModuleManager

def run(scf):
	global mm

	scriptline = 0
	ch = command_handler.Commandhandler(mm, False)

	while True:
		try:
			if scriptline == len(scf):
				sys.exit(0)

			command = scf[scriptline][0]
			scriptline += 1

			ch.handle(command)
		except KeyboardInterrupt:
			print()
			sys.exit(0)
