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

from prettytable import PrettyTable
from core import colors

def generateTable(hlist):
	t = PrettyTable([colors.bold+"Command"+colors.end, "",colors.bold+"Description"+colors.end])
	t.add_row(["-------"," ","-----------"])
	t.align = 'l'
	t.valing = 'm'
	t.border = False

	for val in hlist:
			t.add_row([val[0], "  =>  ", val[1]])

	return t

def generatemTable(hlist1, hlist2):
	t = PrettyTable([colors.bold+"Command"+colors.end, "",colors.bold+"Description"+colors.end])
	t.add_row(["-------"," ","-----------"])
	t.align = 'l'
	t.valing = 'm'
	t.border = False

	for val in hlist1:
			t.add_row([val[0], "  =>  ", val[1]])

	for key, val in hlist2.items():
			t.add_row([key, "  =>  ", val])

	return t
