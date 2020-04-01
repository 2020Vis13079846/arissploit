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
from core import colors
import traceback
import sys
from prettytable import PrettyTable
from core import getpath
from core import moddbparser
from xml.etree import ElementTree
from xml.dom import minidom
from core.messages import *

def count():
	isfile = os.path.isfile
	join = os.path.join

	directory = getpath.modules()
	global module_count
	module_count = sum(1 for item in os.listdir(directory) if isfile(join(directory, item)))
	module_count = module_count - 1
	count.mod = str(module_count)

def printoptions(modadd):
	try:
		print(" ")
		t = PrettyTable([colors.red +'Option', 'Value', 'Description'+colors.end])
		t.add_row(["------","-----","-----------"])
		t.align = 'l'
		t.valing = 'm'
		t.border = False

		for key, val in modadd.variables.items():
				t.add_row([key, val[0], val[1]])

		print (t,'\n')
		try:
			print(modadd.option_notes,'\n')
		except(AttributeError):
			pass

	except Exception as error:
		print("["+colors.bold+colors.red+"err"+colors.end+"] error: module is corrupted\n")
		traceback.print_exc(file=sys.stdout)
		print(colors.end)

def writedb(root):
	rough_string = ElementTree.tostring(root, 'utf-8').decode("utf-8").replace("\n", "").replace("\t", "").replace("  ", "").replace("    ", "").encode("utf-8")
	reparsed = minidom.parseString(rough_string)
	clean = reparsed.toprettyxml(indent="\t")
	f = open(getpath.core()+"module_database.xml", "w")
	f.write(clean)
	f.close()

def addtodb(modadd):
	xml = moddbparser.parsemoddb()
	root = xml[0]
	tree = xml[1]

	new = True
	newcat = True

	for category in root:
		if category.tag == "category":
			for item in category:
				if item.tag == "module" and item.attrib["name"] == modadd.conf["name"]:
					for info in item:
						if info.tag == "shortdesc":
							info.text = modadd.conf["shortdesc"]
							new = False
							tree.write(getpath.core()+"module_database.xml")
							printSuccess("database updated")
							return
	if new == True:
		printInfo("Module "+modadd.conf["name"]+" doesn't exist in modules database!")
		printInfo("Going to add this module to modules database...")
		dome = input(colors.purple+"Add module to [old/new] "+colors.end).strip(" ").lower()
		if dome == "old":
			pass
		if dome == "new":
			printInfo("Going to add new category...")
			catname = input(colors.purple+"Category: "+colors.end)
			newcat = ElementTree.Element("category")
			newcat.set("name", catname)
			newcat.set("key", catname)
			module = ElementTree.Element("module")
			shortdesc = ElementTree.Element("shortdesc")
			shortdesc.text = modadd.conf["shortdesc"]
			module.set("name", modadd.conf["name"])
			module.append(shortdesc)
			newcat.append(module)
			root.append(newcat)
			writedb(root)
			printSuccess("New category created!")
			printSuccess("Module added to "+newcat.attrib["name"])
			return
		print(colors.purple+"Categories:"+colors.yellow)
		for category in root:
			if category.tag == "category":
				print(category.attrib["key"])
		print(colors.end, end="")
		catkey = input(colors.purple+"Category: "+colors.end)

		for category in root:
			if category.tag == "category" and category.attrib["key"] == catkey:
				module = ElementTree.Element("module")
				shortdesc = ElementTree.Element("shortdesc")
				shortdesc.text = modadd.conf["shortdesc"]
				module.set("name", modadd.conf["name"])
				module.append(shortdesc)
				category.append(module)
				writedb(root)
				newcat = False
				printSuccess("Module added to "+category.attrib["name"])
				break

		if newcat == True:
			printInfo("Category not found!")
			printInfo("Going to add new category...")
			catname = input(colors.purple+"Category: "+colors.end)
			newcat = ElementTree.Element("category")
			newcat.set("name", catname)
			newcat.set("key", catkey)
			module = ElementTree.Element("module")
			shortdesc = ElementTree.Element("shortdesc")
			shortdesc.text = modadd.conf["shortdesc"]
			module.set("name", modadd.conf["name"])
			module.append(shortdesc)
			newcat.append(module)
			root.append(newcat)
			writedb(root)
			printSuccess("New category created!")
			printSuccess("Module added to "+newcat.attrib["name"])
