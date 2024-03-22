#!/usr/bin/env python3
import ipaddress
import csv
import sqlite3
import socket

# sqlite3 inet_aton thanks to https://github.com/brthanmathwoag/sqlite-inet

class IPData:
    connection = ''
    cursor = ''
    
    def __init__(self):
        self.connection = sqlite3.connect('ips.db')
        self.connection.enable_load_extension(True)
        self.connection.load_extension('bin/inet')
        self.cursor = self.connection.cursor()

    def search(self, ip_address):
        sql = f"SELECT * FROM ips WHERE (INET_ATON('{ip_address}') BETWEEN INET_ATON(start_ip) AND INET_ATON(end_ip));"
        resp = self.cursor.execute(sql).fetchone()
        if resp:
            return {
                'ip': ip_address,
                'country_code': resp[2],
                'country' : resp[3],
                'continent' : resp[4],
                'continent_name' : resp[5],
                'asn' : resp[6],
                'as_name' : resp[7],
                'as_domain' : resp[8]
            }
        else:
            return {'ip':'not found'}