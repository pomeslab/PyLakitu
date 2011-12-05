import optparse
import threading
import requests
import flask

#from collections import deque

#import logging

app = flask.Flask(__name__)

@app.before_request
def before_request():
    """
    The following code will be executed each time at the beginning of the
    establishment of the connection between server and client
    """

@app.teardown_request
def teardown_request(exception):
    """
    The following code will be executed each time at the beinning of the
    closure of the connection between the server and client
    """
    pass

@app.route("/", methods=['GET', 'POST'])
def index():
    return flask.request.form.to_dict()
#    hello()

def client_loop(hostip, port):
    num_runs = 1
    url = str(hostip) + ":" + str(port)
    while True:
        requests.post(url=url, data={'test': 'hello!'})

        if num_runs == 1:
            break


def parse_cmd():
    """parse the command line, new options could(should?) be added"""
    parser = optparse.OptionParser()
    parser.add_option('-r', '--run-mode', dest='run_mode', default='slave', help="set the running mode of the app")
    options, args = parser.parse_args()
    return options


if __name__ == "__main__":
    options = parse_cmd()


    client_loop("127.0.0.1", 5000)

