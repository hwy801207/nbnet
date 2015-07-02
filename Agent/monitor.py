#-*- coding:utf-8 -*-
from NbNetBase.daemon import Daemon
from NbNetBase.NetBase import nbNet
from NbNetBase.NetUtils import sendData
import json


class Monitor(Daemon):
    #获取监控项
    def __init__(self, sock_l=None, host, port):
        self.items = ['cpuused', 'memtotal', 'memused']
        self.logic = None
        self.sock_l[0] = sock_l 
        self.host = host
        self.port = port
        

    #按照监控项，读取监控数据
    def readData(self):
        data = {}
        for item in self.items:
            data[item] = self.getData(item)
        return json.dumps(data)
     
    #发送监控数据到saver， saver负责发送给数据库跟告警模块
    def sendMonitorData(self):
        data = self.readData()
        sendData(self.sock_l, self.host, self.port, data)
        
    def getData(self, item):
        value  = 10
        return value
    
    def run(self):
        self.sendMonitorData()
        
    
if __name__ == '__main__':
    monitor_agent = Monitor('0.0.0.0', 9076)
    monitor_agent.run()
    

    

        
    
