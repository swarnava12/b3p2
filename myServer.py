from flask import request, url_for
from flask_api import FlaskAPI, status, exceptions
from flask import Flask, render_template
import os
import time
from input import call

app = FlaskAPI(__name__)

@app.route("/p", methods=['GET'])
def notes_detail():
    smileCode = request.args.get('smileCodes').split(",")
   # print(smileCode)
    #os.system("python /home/pankaz-lab-pc3/Desktop/python_flask/input.py " + "'" + smileCode + "'")
    #time.sleep(5)
    #return open('/home/pankaz-lab-pc3/Desktop/python_flask/filename1.html','r').read()
    result = call(smileCode)
    return render_template("json.html", data = result)

@app.route("/p1", methods=['GET'])
def predict():
    smileCode = request.args.get('smileCodes').split(",")
    result = call(smileCode)
    return render_template("json.html", data = result)
    #return result

@app.route('/')
def test():
    return render_template("BBB/main/index.html")

  
if __name__ == "__main__":
    app.run(debug=True)
