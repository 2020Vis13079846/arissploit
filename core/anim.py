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
from core import colors

errorstr = "["+colors.bold+colors.red+"err"+colors.end+"] "
infostr = "["+colors.bold+colors.blue+"inf"+colors.end+"] "
warningstr = "["+colors.bold+colors.yellow+"war"+colors.end+"] "
successstr = "["+colors.bold+colors.green+"suc"+colors.end+"] "

def animline(message, last=False):
	sys.stdout.write("\033[K")
	if last == False:
		sys.stdout.write(message+"\r")
	else:
		sys.stdout.write(message+"\n")

def animError(message, last=False):
	sys.stdout.write("\033[K")
	if last == False:
		sys.stdout.write(errorstr+message+"\r")
	else:
		sys.stdout.write(errorstr+message+"\n")

def animWarning(message, last=False):
	sys.stdout.write("\033[K")
	if last == False:
		sys.stdout.write(warningstr+message+"\r")
	else:
		sys.stdout.write(warningstr+message+"\n")

def animInfo(message, last=False):
	sys.stdout.write("\033[K")
	if last == False:
		sys.stdout.write(infostr+message+"\r")
	else:
		sys.stdout.write(infostr+message+"\n")

def animSuccess(message, last=False):
	sys.stdout.write("\033[K")
	if last == False:
		sys.stdout.write(successstr+text+"\r")
	else:
		sys.stdout.write(successstr+text+"\n")
