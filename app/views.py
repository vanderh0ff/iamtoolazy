from app import app
from flask import render_template,request
import json
import subprocess as sub

@app.route('/')
@app.route('/index')
def index():
    title = "test"
    switches = read_switches()
    print(switches)
    return render_template("index.html", title=title, switches=switches)

@app.route('/off')
def switch_off():
    network_id = request.args.get('netid')
    switch = request.args.get('switch')
    print("toggling {}".format(network_id))
    if network_id is None:
        return error("no netid provided")
    if switch is None:
        sub.call('hacklet off -n {} -s 0'.format(network_id), shell=True)
        sub.call('hacklet off -n {} -s 1'.format(network_id), shell=True)
    if switch == "1" or switch == "0" :
        sub.call('hacklet off -n {} -s {}'.format(network_id,switch), shell=True)
    else:
        return error("invalid switch provided")
    return index()

@app.route('/on')
def switch_on():
    network_id = request.args.get('netid')
    switch = request.args.get('switch')
    print("toggling {}".format(network_id))
    if network_id is None:
        return error("no netid provided")
    if switch is None:
        sub.call('hacklet on -n {} -s 0'.format(network_id), shell=True)
        sub.call('hacklet on -n {} -s 1'.format(network_id), shell=True)
    if switch == "1" or switch == "0" :
        sub.call('hacklet on -n {} -s {}'.format(network_id,switch), shell=True)
    else:
        return error("invalid swithch provided")
    return index()

@app.route('/error')
def error():
    title = "error"
    return render_template("error.html", title=title)

@app.route('/register')
def register():
    title = "register"
    return render_template("register.html", title=title)

def read_switches():
    switch_file = open("data/switches.json")
    switches = json.load(switch_file)
    return switches
    
