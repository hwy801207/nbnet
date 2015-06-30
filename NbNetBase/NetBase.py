
from daemon import Daemon
import socket
import select
import time
import pdb
from _abcoll import __all__

__all__ = ["nbNet", "sendData_mh"]

#DEBUG = True
from NetUtils import *

class nbNetBase:
    def setFd(self, sock):
        """sock is class object of socket"""
        
