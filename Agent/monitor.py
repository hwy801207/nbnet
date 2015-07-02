#-*- coding:utf-8 -*-
from NbNetBase.daemon import Daemon
from NbNetBase.NetBase import nbNet
from NbNetBase.NetUtils import sendData
import json


class Monitor(Daemon):
    #��ȡ�����
    def __init__(self, sock_l=None, host, port):
        self.items = ['cpuused', 'memtotal', 'memused']
        self.logic = None
        self.sock_l[0] = sock_l 
        self.host = host
        self.port = port
        

    #���ռ�����ȡ�������
    def readData(self):
        data = {}
        for item in self.items:
            data[item] = self.getData(item)
        return json.dumps(data)
     
    #���ͼ�����ݵ�saver�� saver�����͸����ݿ���澯ģ��
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
    

    

        
    
