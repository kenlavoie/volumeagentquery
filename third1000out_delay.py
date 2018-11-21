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

list2001_2100 = data[2001:1100] 
list2101_2200 = data[2101:2200] 
list2201_2300 = data[2201:2300] 
list2301_2400 = data[2301:2400] 
list2401_2500 = data[2401:2500] 
list2501_2600 = data[2501:2600] 
list2601_2700 = data[2601:2700] 
list2701_2800 = data[2701:2800]
list2801_2900 = data[2801:2900] 
list2901_3000 = data[2901:3000]
f.close() 

i = 0  

def superloop(): 
    ti = str(time.time() * 1000) 
    savepath = 'savepath = /root/third1000out'
    filename = '{}third1000out.json'.format(ti) 
    third1kfile = os.path.join(savepath, filename)

    def batch21():  

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
            while i <= len(list2001_2100): 
                agentid = list2001_2100.pop()
                filter = "agent.id = %s" % agentid
                res = client.get_data(metrics, start, end, sampling, filter = filter)  
                with open(third1kfile, 'w+') as outfile: 
                    json.dump(res, outfile)
        except: 
            pass 

    def batch22():
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
            while i <= len(list2101_2200): 
                agentid = list2101_2200.pop()
                filter = "agent.id = %s" % agentid
                res = client.get_data(metrics, start, end, sampling, filter = filter)  
                with open(third1kfile, 'a+') as outfile: 
                    json.dump(res, outfile)
        except: 
            pass 

    def batch23():
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
            while i <= len(list2201_2300): 
                agentid = list2201_2300.pop()
                filter = "agent.id = %s" % agentid
                res = client.get_data(metrics, start, end, sampling, filter = filter)  
                with open(third1kfile, 'a+') as outfile: 
                    json.dump(res, outfile)
        except: 
            pass  

    def batch24():
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
            while i <= len(list2301_2400): 
                agentid = list2301_2400.pop()
                filter = "agent.id = %s" % agentid
                res = client.get_data(metrics, start, end, sampling, filter = filter)  
                with open(third1kfile, 'a+') as outfile: 
                    json.dump(res, outfile)
        except: 
            pass 


    def batch25():
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
            while i <= len(list2401_2500): 
                agentid = list2401_2500.pop()
                filter = "agent.id = %s" % agentid
                res = client.get_data(metrics, start, end, sampling, filter = filter)  
                with open(third1kfile, 'a+') as outfile: 
                    json.dump(res, outfile)
        except: 
            pass 

    def batch26():
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
            while i <= len(list2501_2600): 
                agentid = list2501_2600.pop()
                filter = "agent.id = %s" % agentid
                res = client.get_data(metrics, start, end, sampling, filter = filter)  
                with open(third1kfile, 'a+') as outfile: 
                    json.dump(res, outfile)
        except: 
            pass  

    def batch27():
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
            while i <= len(list2601_2700): 
                agentid = list2601_2700.pop()
                filter = "agent.id = %s" % agentid
                res = client.get_data(metrics, start, end, sampling, filter = filter)  
                with open(third1kfile, 'a+') as outfile: 
                    json.dump(res, outfile)
        except: 
            pass  

    def batch28():
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
            while i <= len(list2701_2800): 
                agentid = list2701_2800.pop()
                filter = "agent.id = %s" % agentid
                res = client.get_data(metrics, start, end, sampling, filter = filter)  
                with open(third1kfile, 'a+') as outfile: 
                    json.dump(res, outfile)
        except: 
            pass 

    def batch29():
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
            while i <= len(list2801_2900): 
                agentid = list2801_2900.pop()
                filter = "agent.id = %s" % agentid
                res = client.get_data(metrics, start, end, sampling, filter = filter)  
                with open(third1kfile, 'a+') as outfile: 
                    json.dump(res, outfile)
        except: 
            pass

    def batch30():
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
            while i <= len(list2901_3000): 
                agentid = list2901_3000.pop()
                filter = "agent.id = %s" % agentid
                res = client.get_data(metrics, start, end, sampling, filter = filter)  
                with open(third1kfile, 'a+') as outfile: 
                    json.dump(res, outfile)
        except: 
            pass

    def threads(): 
        tloop21 = multiprocessing.Process(target=batch21)  
        tloop22 = multiprocessing.Process(target=batch22) 
        tloop23 = multiprocessing.Process(target=batch23)  
        tloop24 = multiprocessing.Process(target=batch24)  
        tloop25 = multiprocessing.Process(target=batch25)  
        tloop26 = multiprocessing.Process(target=batch26)  
        tloop27 = multiprocessing.Process(target=batch27) 
        tloop28 = multiprocessing.Process(target=batch28) 
        tloop29 = multiprocessing.Process(target=batch29) 
        tloop30 = multiprocessing.Process(target=batch30)
        tloop21.start() 
        tloop22.start()
        tloop23.start() 
        tloop24.start() 
        tloop25.start() 
        tloop26.start() 
        tloop27.start() 
        tloop28.start() 
        tloop29.start() 
        tloop30.start()

    
    threads()

def main():
    superloop()

if __name__ == "__main__": 
    main() 