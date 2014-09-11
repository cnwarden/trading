#!/usr/bin/python

"""
    tcp server for realtime publishing
"""


import os
import socket

class TcpSetting(object):
    """
        udp channel configuration
    """
    def __init__(self):
        pass

class TcpServer(object):
    """
        tcp server for realtime publishing
    """
    def __init__(self, event_callback=None):
        super(TcpServer, self).__init__()
        self.socks = []


    def open(self):
        pass


    def send(self, buf):
        pass


    def close(self):
        pass

