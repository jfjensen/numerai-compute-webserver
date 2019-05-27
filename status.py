import json
import functools
from flask import jsonify

status_file = "status.json"

def check_status(func):
    @functools.wraps(func)
    def wrapper_check_status():
        status = get_status()['status']
        if status == 'ready':
            func()
            return jsonify({"status": "ok"})
        else:
            return jsonify({"status": "busy"})
    return wrapper_check_status


def running(func):
	@functools.wraps(func)
	def wrapper_running():
	    status = get_status()
	    status['status'] = 'busy'
	    set_status(status)

	    func()

	    status['status'] = 'ready'
	    set_status(status)
	return wrapper_running


def set_ready():
    status = get_status()
    status['status'] = 'ready'
    set_status(status)


def get_status():

    status = None
    with open(status_file, "r") as read_file:
        status = json.load(read_file)

    return status

def set_status(status):

    with open(status_file, "w") as write_file:
        json.dump(status, write_file)