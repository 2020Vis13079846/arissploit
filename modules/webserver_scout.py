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

from core import colors
import http.client
from core.arissploit import *
import socket

conf = {
	"name": "webserver_scout",
	"version": "1.0",
	"shortdesc": "Webserver information thief.",
	"author": "Entynetproject",
	"initdate": "17.5.2019",
	"lastmod": "3.1.2019",
	"apisupport": True
}

# List of the variables
variables = OrderedDict((
	('target', ['google.com', 'Target web address.']),
	('timeout', ['1', 'Timeout.']),
))

# Simple changelog
changelog = "Version 1.0:\nrelease"

def run():
	try:
		try:
			socket.setdefaulttimeout(float(variables['timeout'][0]))
		except ValueError:
			printError('Invalid timeout!')
			return ModuleError("Invalid timeout!")
		conn = http.client.HTTPConnection(variables['target'][0])
		conn.request("HEAD","/index.html")
		res = conn.getresponse()
		results = res.getheaders()
		print('')
		for item in results:
			print(colors.yellow+item[0], item[1]+colors.end)
		print('')
		return results
	except http.client.InvalidURL:
		printError('Invalid URL!')
		return ("Invalid URL!")
	except socket.gaierror:
		printError('Name or service not known!')
		return ModuleError("Name or service not known!")
	except socket.timeout:
		printError('Timeout!')
		return ModuleError("Timeout!")
