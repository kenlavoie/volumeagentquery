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

list0_100 = data[0:100] 
list101_200 = data[101:200] 
list201_300 = data[201:300] 
list301_400 = data[301:400] 
list401_500 = data[401:500] 
list501_600 = data[501:600] 
list601_700 = data[601:700] 
list701_800 = data[701:800]
list801_900 = data[801:900] 
list901_1000 = data[901:1000]
f.close() 

i = 0  

def superloop(): 
    ti = str(time.time() * 1000) 
    savepath = 'savepath = /root/first1000out'
    filename = '{}first1000out.json'.format(ti) 
    first1kfile = os.path.join(savepath, filename)

    def batch1():  

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
            while i <= len(list0_100): 
                agentid = list0_100.pop()
                filter = "agent.id = %s" % agentid
                res = client.get_data(metrics, start, end, sampling, filter = filter)  
                with open(filename, 'w+') as outfile: 
                    json.dump(res, outfile)
        except: 
            pass 

    def batch2():
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
            while i <= len(list101_200): 
                agentid = list101_200.pop()
                filter = "agent.id = %s" % agentid
                res = client.get_data(metrics, start, end, sampling, filter = filter)  
                with open(first1kfile, 'a+') as outfile: 
                    json.dump(res, outfile)
        except: 
            pass 

    def batch3():
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
            while i <= len(list201_300): 
                agentid = list201_300.pop()
                filter = "agent.id = %s" % agentid
                res = client.get_data(metrics, start, end, sampling, filter = filter)  
                with open(first1kfile, 'a+') as outfile: 
                    json.dump(res, outfile)
        except: 
            pass  

    def batch4():
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
            while i <= len(list301_400): 
                agentid = list301_400.pop()
                filter = "agent.id = %s" % agentid
                res = client.get_data(metrics, start, end, sampling, filter = filter)  
                with open(first1kfile, 'a+') as outfile: 
                    json.dump(res, outfile)
        except: 
            pass 


    def batch5():
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
            while i <= len(list401_500): 
                agentid = list401_500.pop()
                filter = "agent.id = %s" % agentid
                res = client.get_data(metrics, start, end, sampling, filter = filter)  
                with open(first1kfile, 'a+') as outfile: 
                    json.dump(res, outfile)
        except: 
            pass 

    def batch6():
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
            while i <= len(list501_600): 
                agentid = list501_600.pop()
                filter = "agent.id = %s" % agentid
                res = client.get_data(metrics, start, end, sampling, filter = filter)  
                with open(first1kfile, 'a+') as outfile: 
                    json.dump(res, outfile)
        except: 
            pass  

    def batch7():
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
            while i <= len(list601_700): 
                agentid = list601_700.pop()
                filter = "agent.id = %s" % agentid
                res = client.get_data(metrics, start, end, sampling, filter = filter)  
                with open(first1kfile, 'a+') as outfile: 
                    json.dump(res, outfile)
        except: 
            pass  

    def batch8():
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
            while i <= len(list701_800): 
                agentid = list701_800.pop()
                filter = "agent.id = %s" % agentid
                res = client.get_data(metrics, start, end, sampling, filter = filter)  
                with open(first1kfile, 'a+') as outfile: 
                    json.dump(res, outfile)
        except: 
            pass 

    def batch9():
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
            while i <= len(list801_900): 
                agentid = list801_900.pop()
                filter = "agent.id = %s" % agentid
                res = client.get_data(metrics, start, end, sampling, filter = filter)  
                with open(first1kfile, 'a+') as outfile: 
                    json.dump(res, outfile)
        except: 
            pass

    def batch10():
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
            while i <= len(list901_1000): 
                agentid = list901_1000.pop()
                filter = "agent.id = %s" % agentid
                res = client.get_data(metrics, start, end, sampling, filter = filter)  
                with open(first1kfile, 'a+') as outfile: 
                    json.dump(res, outfile)
        except: 
            pass

    def threads(): 
        tloop1 = multiprocessing.Process(target=batch1)  
        tloop2 = multiprocessing.Process(target=batch2) 
        tloop3 = multiprocessing.Process(target=batch3)  
        tloop4 = multiprocessing.Process(target=batch4)  
        tloop5 = multiprocessing.Process(target=batch5)  
        tloop6 = multiprocessing.Process(target=batch6)  
        tloop7 = multiprocessing.Process(target=batch7) 
        tloop8 = multiprocessing.Process(target=batch8) 
        tloop9 = multiprocessing.Process(target=batch9) 
        tloop10 = multiprocessing.Process(target=batch10)
        tloop1.start() 
        tloop2.start()
        tloop3.start() 
        tloop4.start() 
        tloop5.start() 
        tloop6.start() 
        tloop7.start() 
        tloop8.start() 
        tloop9.start() 
        tloop10.start()

    
    threads()

def main():
    superloop()

if __name__ == "__main__": 
    main() 
