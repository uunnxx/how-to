#!/usr/bin/env python3

class Server(object):
    def __init__(self, ip, hostname):
        self.ip = ip
        self.hostname = hostname

    def set_ip(self, ip):
        self.ip = ip

    def set_hostname(self, hostname):
        self.hostname = hostname

    def ping(self, ip_addr):
        print(f"Pinging {ip_addr} from {self.ip} ({self.hostname})")


if __name__ == '__main__':
    server = Server('192.168.1.20', 'bumbly')
    server.ping('192.168.1.15')
