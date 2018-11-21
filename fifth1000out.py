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

list4001_4100 = data[4001:4100] 
list4101_4200 = data[4101:4200] 
list4201_4300 = data[4201:4300] 
list4301_4400 = data[4301:4400] 
list4401_4500 = data[4401:4500] 
list4501_4600 = data[4501:4600] 
list4601_4700 = data[4601:4700] 
list4701_4800 = data[4701:4800]
list4801_4900 = data[4801:4900] 
list4901_5000 = data[4901:5000]
f.close() 

i = 0  

def superloop(): 
    ti = str(time.time() * 1000) 
    savepath = '/root/fifth1000out'
    filename = '{}fifth1000out.json'.format(ti) 
    fifth1kfile = os.path.join(savepath, filename)

    def batch41():  

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
            while i <= len(list4001_4100): 
                agentid = list4001_4100.pop()
                filter = "agent.id = %s" % agentid
                res = client.get_data(metrics, start, end, sampling, filter = filter)  
                with open(fifth1kfile, 'w+') as outfile: 
                    json.dump(res, outfile)
        except: 
            pass 

    def batch42():
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
            while i <= len(list4101_4200): 
                agentid = list4101_4200.pop()
                filter = "agent.id = %s" % agentid
                res = client.get_data(metrics, start, end, sampling, filter = filter)  
                with open(fifth1kfile, 'a+') as outfile: 
                    json.dump(res, outfile)
        except: 
            pass 

    def batch43():
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
            while i <= len(list4201_4300): 
                agentid = list4201_4300.pop()
                filter = "agent.id = %s" % agentid
                res = client.get_data(metrics, start, end, sampling, filter = filter)  
                with open(fifth1kfile, 'a+') as outfile: 
                    json.dump(res, outfile)
        except: 
            pass  

    def batch44():
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
            while i <= len(list4301_4400): 
                agentid = list4301_4400.pop()
                filter = "agent.id = %s" % agentid
                res = client.get_data(metrics, start, end, sampling, filter = filter)  
                with open(fifth1kfile, 'a+') as outfile: 
                    json.dump(res, outfile)
        except: 
            pass 


    def batch45():
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
            while i <= len(list4401_4500): 
                agentid = list4401_4500.pop()
                filter = "agent.id = %s" % agentid
                res = client.get_data(metrics, start, end, sampling, filter = filter)  
                with open(fifth1kfile, 'a+') as outfile: 
                    json.dump(res, outfile)
        except: 
            pass 

    def batch46():
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
            while i <= len(list4501_4600): 
                agentid = list4501_4600.pop()
                filter = "agent.id = %s" % agentid
                res = client.get_data(metrics, start, end, sampling, filter = filter)  
                with open(fifth1kfile, 'a+') as outfile: 
                    json.dump(res, outfile)
        except: 
            pass  

    def batch47():
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
            while i <= len(list4601_4700): 
                agentid = list4601_4700.pop()
                filter = "agent.id = %s" % agentid
                res = client.get_data(metrics, start, end, sampling, filter = filter)  
                with open(fifth1kfile, 'a+') as outfile: 
                    json.dump(res, outfile)
        except: 
            pass  

    def batch48():
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
            while i <= len(list4701_4800): 
                agentid = list4701_4800.pop()
                filter = "agent.id = %s" % agentid
                res = client.get_data(metrics, start, end, sampling, filter = filter)  
                with open(fifth1kfile, 'a+') as outfile: 
                    json.dump(res, outfile)
        except: 
            pass 

    def batch49():
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
            while i <= len(list4801_4900): 
                agentid = list4801_4900.pop()
                filter = "agent.id = %s" % agentid
                res = client.get_data(metrics, start, end, sampling, filter = filter)  
                with open(fifth1kfile, 'a+') as outfile: 
                    json.dump(res, outfile)
        except: 
            pass

    def batch50():
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
            while i <= len(list4901_5000): 
                agentid = list4901_5000.pop()
                filter = "agent.id = %s" % agentid
                res = client.get_data(metrics, start, end, sampling, filter = filter)  
                with open(fifth1kfile, 'a+') as outfile: 
                    json.dump(res, outfile)
        except: 
            pass

    def threads(): 
        tloop41 = multiprocessing.Process(target=batch41)  
        tloop42 = multiprocessing.Process(target=batch42) 
        tloop43 = multiprocessing.Process(target=batch43)  
        tloop44 = multiprocessing.Process(target=batch44)  
        tloop45 = multiprocessing.Process(target=batch45)  
        tloop46 = multiprocessing.Process(target=batch46)  
        tloop47 = multiprocessing.Process(target=batch47) 
        tloop48 = multiprocessing.Process(target=batch48) 
        tloop49 = multiprocessing.Process(target=batch49) 
        tloop50 = multiprocessing.Process(target=batch50)
        tloop41.start() 
        tloop42.start()
        tloop43.start() 
        tloop44.start() 
        tloop45.start() 
        tloop46.start() 
        tloop47.start() 
        tloop48.start() 
        tloop49.start() 
        tloop50.start()

    
    threads()

def main():
    superloop()

if __name__ == "__main__": 
    main() 
