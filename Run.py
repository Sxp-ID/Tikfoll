# Open source kan ngab wkwk!

# Creator : Sanz
# Youtube : FREE TUTORIAL

import os, sys

try:
	sanz = open('main','rb').read()
	os.system('./main')
except:
	os.system('make install')
	os.system('./main')
