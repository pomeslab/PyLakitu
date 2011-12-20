import optparse
import time
import multiprocessing
import sys
import threading

import requests

from PyLakitu import app

#import logging
import thread

@app.before_request
def before_request():
    print "before request"

@app.teardown_request
def teardown_request(exception):
    print "teardown_request"

@app.route('/')
def index():
    print "This is the index()"
    return "This is the index method"

@app.route("/update", methods=['POST'])
def update():
    print "update()"
    return "This is the update method"

@app.route("/update_n/<int:temp>", methods=['POST'])
def update_n(temp):
    print "data sent", temp
    return str(temp)

@app.route("/admin/list_jobs")
def all_jobs():
    print "all jobs"
    return list_jobs("all")

@app.route("/admin/list_jobs/<status>")
def list_jobs(status):
    print "sent status", status
    return "status of all jobs"

#@app.route("/admin/stop")
#def stop():
#    pass
#
#@app.route("/admin/start")
#def start():
#    pass

def parse_cmd():
    parser = optparse.OptionParser()
    parser.add_option('-r', '--run-mode', dest='run_mode', default='slave', help="set the running mode of the app")
    options, args = parser.parse_args()
    return options

'''
if __name__ == "__main__":
    options = parse_cmd()

    hostip = "127.0.0.1"
    port = 5000

    print "start dev server"
    app.run(debug=True)


    client.run()
'''
