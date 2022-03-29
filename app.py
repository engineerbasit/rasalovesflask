from flask import Flask, render_template, request, jsonify
import os,sys,requests, json
from random import randint
app = Flask(__name__)
@app.route('/')
def home():
  return render_template('index.html')
@app.route('/parse',methods=['POST', 'GET'] )
def extract():
  text=str(request.form.get('value1'))
  payload = json.dumps({"sender": "Rasa","message": text})
  headers = {'Content-type': 'application/json', 'Accept':     'text/plain'}
  response = requests.request("POST",   url="https://rasaflask.herokuapp.com/webhooks/rest/webhook", headers=headers, data=payload)
  response=response.json()
  resp=[]
  for i in range(len(response)):
    try:
      resp.append(response[i]['text'])
    except:
      continue
  result=resp
  return render_template('index.html', result=result,text=text)
if __name__ == "__main__":
  p = int(os.environ.get("PORT", 5000))
  app.run(debug=True, port=p, host='https://rasaflask.herokuapp.com/')
