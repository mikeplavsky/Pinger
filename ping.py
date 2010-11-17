from optparse import OptionParser
parser = OptionParser()

parser.add_option("-u", "--url", dest="url", help="url to ping" )
parser.add_option("-l", "--log", dest="log", help="log file for pinging this URL" )

options, args = parser.parse_args()

from ping_core import ping

import logging
logging.basicConfig(filename=options.log,level=logging.DEBUG, format = "%(asctime)s - %(levelname)s - %(message)s" )

while True:
	
	ping( options.url )
	
	import time
	import random
	
	next = 60 * 30 * random.random()
	logging.info( "Next run in %s minutes" % int( next / 60 ) )
	
	time.sleep( next )