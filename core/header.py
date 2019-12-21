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

	print("\t" + colors.bold + "    Arissploit Framework\n" + colors.end)
	print("\t" + colors.bold + "Author "+colors.end+"\t[ "+info.author+" ]" + colors.end)	
	print("\t" + colors.bold + "Version"+colors.end+"\t[ "+info.version+"            ]"+colors.end)
	print("\t" + colors.bold + "Modules "+colors.end+"[ "+count.mod+" modules"+"     ]"+colors.end)
	print("")
