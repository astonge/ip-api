#!/usr/bin/env python3
import os
from dotenv import load_dotenv
from wsgiref.simple_server import make_server
import falcon
from ipdata import IPData
from middleware import AuthMiddleware

database = ''

class IPResource:
    def on_get(self, req, resp, ip_addr):
        if ip_addr:
            ipinfo = database.search(ip_address=ip_addr)
        resp.media = ipinfo

if __name__ == '__main__':
    # Setup
    load_dotenv()
    database = IPData()
    app = falcon.App(
        middleware=[
            AuthMiddleware(),
        ]
    )
    app.add_route('/{ip_addr}', IPResource())
    
    # Start server
    port = 8123
    with make_server('', port, app) as httpd:
        print('Serving on port:',port)
        httpd.serve_forever()