import json
import asyncio 
import datetime 
import os 
import time
from sdcclient import SdMonitorClient 
import requests  
import multiprocessing  
from multiprocessing import Pool

api_token = os.environ["APITOKEN"] 
sysdig_url = os.environ["SYSDIGURL"]

client = SdMonitorClient(api_token, sdc_url= sysdig_url, ssl_verify=True)

f = open('totalagents.json') 

data = json.loads(f.read())  

list1001_1100 = data[1001:1100] 
list1101_1200 = data[1101:1200] 
list1201_1300 = data[1201:1300] 
list1301_1400 = data[1301:1400] 
list1401_1500 = data[1401:1500] 
list1501_1600 = data[1501:1600] 
list1601_1700 = data[1601:1700] 
list1701_1800 = data[1701:1800]
list1801_1900 = data[1801:1900] 
list1901_2000 = data[1901:2000]
f.close() 

i = 0  

def superloop(): 
    ti = str(time.time() * 1000) 
    savepath = '/root/second1000out/'
    filename = '{}second1000out.json'.format(ti) 
    second1kfile = os.path.join(savepath, filename)

    def batch11():  

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
            while i <= len(list1001_1100): 
                agentid = list1001_1100.pop()
                filter = "agent.id = %s" % agentid
                res = client.get_data(metrics, start, end, sampling, filter = filter)  
                with open(second1kfile, 'w+') as outfile: 
                    json.dump(res, outfile)
        except: 
            pass 

    def batch12():
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
            while i <= len(list1101_1200): 
                agentid = list1101_1200.pop()
                filter = "agent.id = %s" % agentid
                res = client.get_data(metrics, start, end, sampling, filter = filter)  
                with open(second1kfile, 'a+') as outfile: 
                    json.dump(res, outfile)
        except: 
            pass 

    def batch13():
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
            while i <= len(list1201_1300): 
                agentid = list1201_1300.pop()
                filter = "agent.id = %s" % agentid
                res = client.get_data(metrics, start, end, sampling, filter = filter)  
                with open(second1kfile, 'a+') as outfile: 
                    json.dump(res, outfile)
        except: 
            pass  

    def batch14():
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
            while i <= len(list1301_1400): 
                agentid = list1301_1400.pop()
                filter = "agent.id = %s" % agentid
                res = client.get_data(metrics, start, end, sampling, filter = filter)  
                with open(second1kfile, 'a+') as outfile: 
                    json.dump(res, outfile)
        except: 
            pass 


    def batch15():
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
            while i <= len(list1401_1500): 
                agentid = list1401_1500.pop()
                filter = "agent.id = %s" % agentid
                res = client.get_data(metrics, start, end, sampling, filter = filter)  
                with open(second1kfile, 'a+') as outfile: 
                    json.dump(res, outfile)
        except: 
            pass 

    def batch16():
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
            while i <= len(list1501_1600): 
                agentid = list1501_1600.pop()
                filter = "agent.id = %s" % agentid
                res = client.get_data(metrics, start, end, sampling, filter = filter)  
                with open(second1kfile, 'a+') as outfile: 
                    json.dump(res, outfile)
        except: 
            pass  

    def batch17():
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
            while i <= len(list1601_1700): 
                agentid = list1601_1700.pop()
                filter = "agent.id = %s" % agentid
                res = client.get_data(metrics, start, end, sampling, filter = filter)  
                with open(second1kfile, 'a+') as outfile: 
                    json.dump(res, outfile)
        except: 
            pass  

    def batch18():
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
            while i <= len(list1701_1800): 
                agentid = list1701_1800.pop()
                filter = "agent.id = %s" % agentid
                res = client.get_data(metrics, start, end, sampling, filter = filter)  
                with open(second1kfile, 'a+') as outfile: 
                    json.dump(res, outfile)
        except: 
            pass 

    def batch19():
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
            while i <= len(list1801_1900): 
                agentid = list1801_1900.pop()
                filter = "agent.id = %s" % agentid
                res = client.get_data(metrics, start, end, sampling, filter = filter)  
                with open(second1kfile, 'a+') as outfile: 
                    json.dump(res, outfile)
        except: 
            pass

    def batch20():
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
            while i <= len(list1901_2000): 
                agentid = list1901_2000.pop()
                filter = "agent.id = %s" % agentid
                res = client.get_data(metrics, start, end, sampling, filter = filter)  
                with open(second1kfile, 'a+') as outfile: 
                    json.dump(res, outfile)
        except: 
            pass

    def threads(): 
        tloop11 = multiprocessing.Process(target=batch11)  
        tloop12 = multiprocessing.Process(target=batch12) 
        tloop13 = multiprocessing.Process(target=batch13)  
        tloop14 = multiprocessing.Process(target=batch14)  
        tloop15 = multiprocessing.Process(target=batch15)  
        tloop16 = multiprocessing.Process(target=batch16)  
        tloop17 = multiprocessing.Process(target=batch17) 
        tloop18 = multiprocessing.Process(target=batch18) 
        tloop19 = multiprocessing.Process(target=batch19) 
        tloop20 = multiprocessing.Process(target=batch20)
        tloop11.start() 
        tloop12.start()
        tloop13.start() 
        tloop14.start() 
        tloop15.start() 
        tloop16.start() 
        tloop17.start() 
        tloop18.start() 
        tloop19.start() 
        tloop20.start()

    
    threads()

def main():
    superloop()

if __name__ == "__main__": 
    main() 
