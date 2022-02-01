#!/usr/bin/python


import Quartz
import flask


app = flask.Flask(__name__)
app.config["DEBUG"] = False


@app.route("/screenlocked/status", methods=["GET"])
def status():
    display = Quartz.CGSessionCopyCurrentDictionary()
    screen_lock_status = display.get("CGSSessionScreenIsLocked", 0) == 1
    if screen_lock_status:
        print("Screen is locked, Status: 1")
        return "0"
    if not screen_lock_status:
        print("Screen is unlocked, Status: 0")
        return "1"


app.run(host="0.0.0.0", port=55888)
