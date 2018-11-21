import json
import requests 
import urllib
import os
from sdcclient import SdcClient 
from sdcclient import SdMonitorClient

api_token = os.environ["APITOKEN"] 
sysdig_url = os.environ["SYSDIGURL"]

client = SdMonitorClient(api_token, sdc_url= sysdig_url, ssl_verify=True)


apiurl = 'https://a1061eb84e93911e8ba53124f7ae6446-1604746915.us-east-1.elb.amazonaws.com/api/agents/connected?_product=SDC' 
headers = {'Authorization': 'Bearer ' + api_token, 'Content-Type': 'application/json'}


res = requests.get(apiurl, headers=headers, verify=False) 
data = res.json()
newlist = []
testout = []
for customer in data['agents']: 
        newlist.append(customer['id'])

print(newlist)