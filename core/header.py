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

from core import info
from core import colors
from core.moduleop import count

arissploit = r"""
          .----.   @   @                  
         / .-.-.`.  \v/                            
         | | '\ \ \_/ )                      
       ,-\ `-.' /.'  /           
       '---`----'----'    
"""

def print_info():
	count()

	print("    " + colors.bold + " Arissploit Framework\n" + colors.end)
	print(" " + colors.bold + " Version "+colors.end+"[ "+info.version+" "+info.codename+" ]" + colors.end)
	print(" " + colors.bold + " API"+colors.end+"     [ "+info.apiversion+"          ]"+colors.end)
	print(" " + colors.bold + " Date"+colors.end+"    [ "+info.update_date+"       ]"+colors.end)
	print(" " + colors.bold + " Modules "+colors.end+"[ "+count.mod+" modules"+"     ]"+colors.end)
	print("")
