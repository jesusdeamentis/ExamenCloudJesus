from Credentials import Credentials

from ibm_watson import ToneAnalyzerV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

#Authenticate

authenticator = IAMAuthenticator(Credentials.apikey)
ta = ToneAnalyzerV3(version='2017-09-21', authenticator=authenticator)
ta.set_service_url(Credentials.url)

#Analyze Tone
res = ta.tone('I take care of my skin so there is something shining in here, because my hopes and dreams are not going to do it').get_result()

print (res)