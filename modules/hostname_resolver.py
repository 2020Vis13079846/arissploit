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
import socket

conf = {
	"name": "hostname_resolver",
	"version": "1.0",
	"shortdesc": "Hostname IP resolver.",
	"author": "Entynetproject",
	"initdate": "9.5.2019",
	"lastmod": "3.1.2019",
	"apisupport": True
}

# List of the variables
variables = OrderedDict((
	('target', ['192.168.1.1', 'Target IP address.']),
))

#simple changelog
changelog = "Version 1.0:\nrelease"

def run():
	try:
		querly = socket.gethostbyaddr(variables['target'][0])
		printSuccess("Resolved hostname: "+ querly[0])
		return querly[0]
	except(socket.herror):
		printError("Unknown host!")
		return ModuleError("Unknown host!")
	except(socket.gaierror):
		printError("Name or service not known!")
		return ModuleError("Name or service not known!")
