

"""
    udp server for realtime publishing
"""


import os
import socket

class UdpSetting(object):
    """
        udp channel configuration
    """
    def __init__(self):
        self.multicastIP = ''
        self.multicastPort = ''




class UdpServer(object):
    """
        udp server for realtime publishing
    """
    def __init__(self):
        super(UdpServer, self).__init__()
        self.socks = []


    def open(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 32)

        self.socks.append(sock)


    def send(self, buf):
        for sock in self.socks:
            sock.sendto(buf, ('224.4.8.11', 60400))


    def close(self):
        for sock in self.socks:
            sock.close()

