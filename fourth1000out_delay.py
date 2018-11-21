import json
import asyncio 
import datetime 
import time
import os
from sdcclient import SdMonitorClient 
import requests  
import multiprocessing 
from multiprocessing import Pool

api_token = os.environ["APITOKEN"] 
sysdig_url = os.environ["SYSDIGURL"]

client = SdMonitorClient(api_token, sdc_url= sysdig_url, ssl_verify=True)

f = open('totalagents.json') 

data = json.loads(f.read())  

list3001_3100 = data[3001:3100] 
list3101_3200 = data[3101:3200] 
list3201_3300 = data[3201:3300] 
list3301_3400 = data[3301:3400] 
list3401_3500 = data[3401:3500] 
list3501_3600 = data[3501:3600] 
list3601_3700 = data[3601:3700] 
list3701_3800 = data[3701:3800]
list3801_3900 = data[3801:3900] 
list3901_4000 = data[3901:4000]
f.close() 

i = 0  

def superloop(): 
    ti = str(time.time() * 1000) 
    savepath = '/root/fourth1000out/'
    filename = '{}fourth1000outdelay.json'.format(ti) 
    fourth1kfile = os.path.join(savepath, filename)

    def batch31():  

        metrics =   [
                { "id": "host.hostName" },
                { "id": "net.local.endpoint" }, 
                { "id": "net.remote.endpoint" }, 
                { "id": "net.connection.direction"}, 
                { "id": "proc.name"}, 
                { "id": "proc.commandLine"}
            ]

        start =     -600
        end =       0
        sampling =  10
        try:
            while i <= len(list3001_3100): 
                agentid = list3001_3100.pop()
                filter = "agent.id = %s" % agentid
                res = client.get_data(metrics, start, end, sampling, filter = filter)  
                with open(fourth1kfile, 'w+') as outfile: 
                    json.dump(res, outfile)
        except: 
            pass 

    def batch32():
        metrics =   [
                { "id": "host.hostName" },
                { "id": "net.local.endpoint" }, 
                { "id": "net.remote.endpoint" }, 
                { "id": "net.connection.direction"}, 
                { "id": "proc.name"}, 
                { "id": "proc.commandLine"}
            ]

        start =    -600
        end =       0
        sampling =  10


        try:
            while i <= len(list3101_3200): 
                agentid = list3101_3200.pop()
                filter = "agent.id = %s" % agentid
                res = client.get_data(metrics, start, end, sampling, filter = filter)  
                with open(fourth1kfile, 'a+') as outfile: 
                    json.dump(res, outfile)
        except: 
            pass 

    def batch33():
        metrics =   [
                { "id": "host.hostName" },
                { "id": "net.local.endpoint" }, 
                { "id": "net.remote.endpoint" }, 
                { "id": "net.connection.direction"}, 
                { "id": "proc.name"}, 
                { "id": "proc.commandLine"}
            ]

        start =     -600
        end =       0
        sampling =  10


        try:
            while i <= len(list3201_3300): 
                agentid = list3201_3300.pop()
                filter = "agent.id = %s" % agentid
                res = client.get_data(metrics, start, end, sampling, filter = filter)  
                with open(fourth1kfile, 'a+') as outfile: 
                    json.dump(res, outfile)
        except: 
            pass  

    def batch34():
        metrics =   [
                { "id": "host.hostName" },
                { "id": "net.local.endpoint" }, 
                { "id": "net.remote.endpoint" }, 
                { "id": "net.connection.direction"}, 
                { "id": "proc.name"}, 
                { "id": "proc.commandLine"}
            ]

        start =     -600
        end =       0
        sampling =  10


        try:
            while i <= len(list3301_3400): 
                agentid = list3301_3400.pop()
                filter = "agent.id = %s" % agentid
                res = client.get_data(metrics, start, end, sampling, filter = filter)  
                with open(fourth1kfile, 'a+') as outfile: 
                    json.dump(res, outfile)
        except: 
            pass 


    def batch35():
        metrics =   [
                { "id": "host.hostName" },
                { "id": "net.local.endpoint" }, 
                { "id": "net.remote.endpoint" }, 
                { "id": "net.connection.direction"}, 
                { "id": "proc.name"}, 
                { "id": "proc.commandLine"}
            ]

        start =     -600
        end =       0
        sampling =  10


        try:
            while i <= len(list3401_3500): 
                agentid = list3401_3500.pop()
                filter = "agent.id = %s" % agentid
                res = client.get_data(metrics, start, end, sampling, filter = filter)  
                with open(fourth1kfile, 'a+') as outfile: 
                    json.dump(res, outfile)
        except: 
            pass 

    def batch36():
        metrics =   [
                { "id": "host.hostName" },
                { "id": "net.local.endpoint" }, 
                { "id": "net.remote.endpoint" }, 
                { "id": "net.connection.direction"}, 
                { "id": "proc.name"}, 
                { "id": "proc.commandLine"}
            ]

        start =     -600
        end =       0
        sampling =  10


        try:
            while i <= len(list3501_3600): 
                agentid = list3501_3600.pop()
                filter = "agent.id = %s" % agentid
                res = client.get_data(metrics, start, end, sampling, filter = filter)  
                with open(fourth1kfile, 'a+') as outfile: 
                    json.dump(res, outfile)
        except: 
            pass  

    def batch37():
        metrics =   [
                { "id": "host.hostName" },
                { "id": "net.local.endpoint" }, 
                { "id": "net.remote.endpoint" }, 
                { "id": "net.connection.direction"}, 
                { "id": "proc.name"}, 
                { "id": "proc.commandLine"}
            ]

        start =     -600
        end =       0
        sampling =  10


        try:
            while i <= len(list3601_3700): 
                agentid = list3601_3700.pop()
                filter = "agent.id = %s" % agentid
                res = client.get_data(metrics, start, end, sampling, filter = filter)  
                with open(fourth1kfile, 'a+') as outfile: 
                    json.dump(res, outfile)
        except: 
            pass  

    def batch38():
        metrics =   [
                { "id": "host.hostName" },
                { "id": "net.local.endpoint" }, 
                { "id": "net.remote.endpoint" }, 
                { "id": "net.connection.direction"}, 
                { "id": "proc.name"}, 
                { "id": "proc.commandLine"}
            ]

        start =     -600
        end =       0
        sampling =  10


        try:
            while i <= len(list3701_3800): 
                agentid = list3701_3800.pop()
                filter = "agent.id = %s" % agentid
                res = client.get_data(metrics, start, end, sampling, filter = filter)  
                with open(fourth1kfile, 'a+') as outfile: 
                    json.dump(res, outfile)
        except: 
            pass 

    def batch39():
        metrics =   [
                { "id": "host.hostName" },
                { "id": "net.local.endpoint" }, 
                { "id": "net.remote.endpoint" }, 
                { "id": "net.connection.direction"}, 
                { "id": "proc.name"}, 
                { "id": "proc.commandLine"}
            ]

        start =     -600
        end =       0
        sampling =  10


        try:
            while i <= len(list3801_3900): 
                agentid = list3801_3900.pop()
                filter = "agent.id = %s" % agentid
                res = client.get_data(metrics, start, end, sampling, filter = filter)  
                with open(fourth1kfile, 'a+') as outfile: 
                    json.dump(res, outfile)
        except: 
            pass

    def batch40():
        metrics =   [
                { "id": "host.hostName" },
                { "id": "net.local.endpoint" }, 
                { "id": "net.remote.endpoint" }, 
                { "id": "net.connection.direction"}, 
                { "id": "proc.name"}, 
                { "id": "proc.commandLine"}
            ]

        start =     -600
        end =       0
        sampling =  10


        try:
            while i <= len(list3901_4000): 
                agentid = list3901_4000.pop()
                filter = "agent.id = %s" % agentid
                res = client.get_data(metrics, start, end, sampling, filter = filter)  
                with open(fourth1kfile, 'a+') as outfile: 
                    json.dump(res, outfile)
        except: 
            pass

    def threads(): 
        tloop31 = multiprocessing.Process(target=batch31)  
        tloop32 = multiprocessing.Process(target=batch32) 
        tloop33 = multiprocessing.Process(target=batch33)  
        tloop34 = multiprocessing.Process(target=batch34)  
        tloop35 = multiprocessing.Process(target=batch35)  
        tloop36 = multiprocessing.Process(target=batch36)  
        tloop37 = multiprocessing.Process(target=batch37) 
        tloop38 = multiprocessing.Process(target=batch38) 
        tloop39 = multiprocessing.Process(target=batch39) 
        tloop40 = multiprocessing.Process(target=batch40)
        tloop31.start() 
        tloop32.start()
        tloop33.start() 
        tloop34.start() 
        tloop35.start() 
        tloop36.start() 
        tloop37.start() 
        tloop38.start() 
        tloop39.start() 
        tloop40.start()

    
    threads()

def main():
    superloop()

if __name__ == "__main__": 
    main() 
