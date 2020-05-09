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
from scapy.all import *

conf = {
	"name": "arp_monitor", # Module's name (should be same as file name)
	"version": "1.0", # Module version
	"shortdesc": "ARP packet monitor.", # Short description
	"author": "Entynetproject", # Author
	"initdate": "31.12.2019", # Initial date
	"lastmod": "31.12.2019", # Last modification
	"apisupport": False, # Api support
	"needroot": 1, # Alert user if root permissions not available (remove variable below if root permissions not needed)
}

# List of the variables
variables = OrderedDict((
	
))

# Additional notes to options
option_notes = "This module does not have any options."

# Simple changelog
changelog = "Version 1.0:\nrelease"

def arp_display(pkt):
	if pkt[ARP].op == 1: #who-has (request)
		return "Request: " + pkt[ARP].psrc + " is asking about " + pkt[ARP].pdst
	if pkt[ARP].op == 2: #is-at (response)
		return "*Response: " + pkt[ARP].hwsrc + " has address " + pkt[ARP].psrc

# Run function
def run():
	printInfo("Starting ARP monitor...")
	printInfo("Ctrl + C to stop.")
	print(sniff(prn=arp_display, filter="arp", store=0))
	printInfo("ARP monitor stopped.")
