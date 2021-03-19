from Credentials import Credentials

from ibm_watson import ToneAnalyzerV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

#Authenticate

authenticator = IAMAuthenticator(Credentials.apikey)
ta = ToneAnalyzerV3(version='2017-09-21', authenticator=authenticator)
ta.set_service_url(Credentials.url)

#Analyze Tone
res = ta.tone('shame on your cow, your life and your ancestors').get_result()

print (res)