
from daemon import Daemon
import socket
import select
import time
import pdb
from _abcoll import __all__
from NbNetBase.NetUtils import dbgPrint

__all__ = ["nbNet", "sendData_mh"]

#DEBUG = True
from NetUtils import *

class nbNetBase:
    def setFd(self, sock):
        """sock is class object of socket"""
        dbgPrint("\n -- setFd start!")
        _state = STATE()
        _state.sock_obj = sock
        self.conn_state[sock.fileno()] = _state
        self.conn_state[sock.fileno()].printState()
        dbgPrint("\n -- setFd End!")
        
    def accept(self, fd):
        dbgPrint("\n -- start Accept function")
        _sock_state = self.conn_state[fd]
        _sock = _sock_state.sock_obj
        conn, addr = _sock.accept()
        conn.setblocking(0)
        dbgPrint("\n -- End Accept function")
        return conn
    def close(self, fd):
        try:
            sock = self.conn_state[fd].sock_obj
            sock.close()
            self.epoll_sock.unregister(fd)
            self.conn_state.pop(fd)
        except:
            dbgPrint("Close fd: %s abnormal" % fd)
            pass
        
    def read(self,fd):
        try:
            sock_state = self.conn_state[fd]
            conn = sock_state.sock_obj
            if sock_state.need_read <= 0:
                pass
            
    
