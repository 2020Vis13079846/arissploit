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
from scapy.all import srp,Ether,ARP,conf
from datetime import datetime
import traceback
from core import colors
from core.messages import *

try:
	import netifaces
except ImportError:
	print(colors.red+'ImportError: netifaces:\n')
	traceback.print_exc()
	print(colors.end)


def scan():
	try:
		print(colors.purple+"Interfaces:"+colors.end)
		for iface in netifaces.interfaces():
			print(colors.yellow+iface+colors.end)
		interface = input("\033[1;77m[>]\033[0m Interface: ").strip(" ")
		try:
			ip = netifaces.ifaddresses(interface)[2][0]['addr']
		except(ValueError, KeyError):
			printError("Invalid interface!")
			return
		ips = ip+"/24"
		printInfo("Scanning...")

		start_time = datetime.now()

		conf.verb = 0
		try:
			ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst = ips), timeout = 2,iface=interface,inter=0.1)
		except PermissionError:
			printError('Permission denied!')
			return

		for snd,rcv in ans:
			print(rcv.sprintf(colors.yellow+"r%Ether.src% - %ARP.psrc%"+colors.end))
		stop_time = datetime.now()
		total_time = stop_time - start_time
		printSuccess("Scan completed!")
		printSuccess("Scan duration: "+str(total_time))
	except KeyboardInterrupt:
		printWarning("Network scanner terminated.")
