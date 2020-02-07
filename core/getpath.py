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

import os
import sys

def rchop(thestring, ending):
	if thestring.endswith(ending):
		return thestring[:-len(ending)]
	return thestring

def main():
	path = rchop(os.path.dirname(os.path.abspath(__file__)), "core")
	return path

def main_module():
	path = os.path.dirname(os.path.abspath(sys.modules['__main__'].__file__)) + "/"
	return path

def modules():
	path = rchop(os.path.dirname(os.path.abspath(__file__)), "core") + "modules/"
	return path

def core():
	path = os.path.dirname(os.path.abspath(__file__)) + "/"
	return path

def lib():
	path = os.path.dirname(os.path.abspath(__file__)) + "/lib/"
	return path

def tools():
	path = os.path.dirname(os.path.abspath(__file__)) + "/tools/"
	return path

def conf():
	path = os.path.dirname(os.path.abspath(__file__)) + "/conf/"
	return path

def tmp():
	path = os.path.dirname(os.path.abspath(__file__)) + "/tmp/"
	return path

def scripts():
	path = os.path.dirname(os.path.abspath(__file__)) + "/scripts/"
	return path

def db():
	path = os.path.dirname(os.path.abspath(__file__)) + "/db/"
	return path
