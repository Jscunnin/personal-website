'''TEMPLATE FOR ADDING PAGES

@app.route('/x')
def x():
    return render_template('personal/x')

'''

import time
from flask import Flask, render_template
import os
from flask import url_for, request, make_response, redirect
from datetime import datetime

incompletePage="temp.html"

app = Flask(__name__)
logFile = os.getcwd() +"/.data/connections.log"

#@app.after_request
#def afterRequest(response):
#	ip = request.headers.get('CF-Connecting-IP', request.remote_addr)
#	now = datetime.now()
#	with open(logFile, 'a') as file:
#		file.write(str(now) + " - " + ip + "\n")
#	return response

@app.route("/pid")
def pid():
	return '<h1>' + str(os.getpid()) + '</h1>'

@app.route('/')
def main():
    ip = request.headers.get('CF-Connecting-IP', request.remote_addr)
    now = datetime.now()
    with open(logFile, 'a') as file:
        file.write("Someone Connected! -" + ip + "\n")
    return render_template("home.html")

@app.route('/submit', methods=["POST"])
def createUserID():
    company = request.form.get("user_input")
    resp = make_response(redirect(url_for("main")))
    resp.set_cookie("userID", company)
    return resp

#Projects****************************************************************
@app.route('/projects')
def projects():
    return render_template("projects.html")

#Experience************************************************************
@app.route('/experience')
def experience():
    return render_template(incompletePage)

#Contact*********************************************************************
@app.route('/contact')
def contact():
    with open(logFile, 'a') as file:
        file.write("\tContact page visited!\n")
    return render_template('contact.html')




if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5001, threaded=True)
