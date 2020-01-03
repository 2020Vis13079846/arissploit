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
	print("\t" + colors.bold + "    Version "+colors.end+"[ "+info.version+" "+info.codename+" ]" + colors.end)
	print("\t" + colors.bold + "    API"+colors.end+"     [ "+info.apiversion+"         ]"+colors.end)
	print("\t" + colors.bold + "    Date"+colors.end+"    [ "+info.update_date+"      ]"+colors.end)
	print("\t" + colors.bold + "    Modules "+colors.end+"[ "+count.mod+" modules"+"    ]"+colors.end)
	print("")
