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

def printError(message, start="", end="\n"):
	sys.stdout.write(errorstr+message+end)

def printWarning(message, start="", end="\n"):
	sys.stdout.write(start+warningstr+message+end)

def printInfo(message, start="", end="\n"):
	sys.stdout.write(start+infostr+message+end)

def printSuccess(message, start="", end="\n"):
	sys.stdout.write(start+successstr+message+end)
