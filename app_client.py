import optparse
import time
import multiprocessing
import sys
import threading

import requests
import flask

#import logging
import thread

hostip = "127.0.0.1"
port = 5000
url = 'http://' + str(hostip) + ":" + str(port) + '/'

def test_client_post():
    i=0
    while i<2:
#        /update_temp?temp=300
        r = requests.post(url=url+'update_n/300', config={'verbose': sys.stderr, 'safe_mode': True})
        
        print "contents of response", r.content
        time.sleep(1)
        i+=1
        
def test_client_get():
    i=0
    while i<2:
        print "getting something"
        r = requests.get(url)
        print "contents of response", r.content
        time.sleep(1)
        i+=1


if __name__ == '__main__':
    print "starting client get tests"
#    test_client_get()
    test_client_post()