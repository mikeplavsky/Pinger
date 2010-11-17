def ping(url):

	import logging

	try:

		import System
		
		from System.Net import CredentialCache
		from System.Net import WebClient

		client = WebClient()
		client.Credentials = CredentialCache.DefaultCredentials
    
		res = client.DownloadString( url )
		logging.info( url )

	except SystemError, ex:
    
		logging.error( ex ) 
	