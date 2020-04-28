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
import whois

conf = {
	"name": "whois", # Module's name (should be same as file name)
	"version": "1.0", # Module version
	"shortdesc": "Whois query performer.", # Short description
	"author": "Entynetproject", # Author
	"initdate": "18.12.2019", # Initial date
	"lastmod": "29.12.2019",
	"apisupport": True
}

# List of the variables
variables = OrderedDict((
	("target", ["google.com", "Target web address."]),
))

# Simple changelog
changelog = "Version 1.0:\nrelease"

def run():
	# Run
	w = whois.whois(variables["target"][0])
	print(w)
	return w
