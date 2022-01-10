from livereload import Server
from flask import Flask, render_template, redirect, url_for, request, session
import json,pdb,os
import requests
import pdb #Python debugger
import collections #dictionaries
import urllib.parse



app = Flask(__name__)
#server = Server(app.wsgi_app)
app.debug = True

@app.template_filter('not_list_or_dict')
def typecheck(value):
    return type(value) not in [type({}), type([])]

@app.template_filter('list_only')
def typecheck(value):
    return type(value) in [type([])]

@app.template_filter('dict_only')
def typecheck(value):
    return type(value) in [type({})]

@app.route('/search', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if len(request.form['tag']) > 11 or len(request.form['tag']) < 9: #8Y8PPP2V0
            error = 'Tag is incorrect'
        else:
            tag = request.form['tag']
            tag = '#' + tag if '#' not in tag else tag
            #Part of the secret key stuff
            #messages = session['messages']
            #-------------------------------

            root_url = 'https://api.clashroyale.com/v1/players/'
            response = requests.get(
                root_url + urllib.parse.quote(tag),
                headers = {
                    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjFmMGMxNzJmLTY3ZTItNDc2NC1iMjI0LTg0MGU1NzY3ZWNiZiIsImlhdCI6MTY0MTIzMzcyNiwic3ViIjoiZGV2ZWxvcGVyLzRlOTg5N2RmLWQxMjItNTNiOC1iODRiLWQ0ZjlkZWQ3ZjVhYSIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyIyNC4xOTIuNDguMTc5Il0sInR5cGUiOiJjbGllbnQifV19.2BqLPfT7P3fw1uB2IqglmlsiM-zSXIsg7iuiuuvbJveZzBVZsMRDfwry2EIfgwJUNTxDyxyEE4PyqfQzWRuOkA',
                    'Accept': 'application/json'}
            )
            if response.ok:
                clanData = response.json()

        #    pdb.set_trace()
            try:
                return render_template("test.html", clanData = clanData)
            except:
                print(response.reason)

            

    return render_template('test.html', error=error)


if __name__ == '__main__':
    #server.serve(port=8080, host='localhost')
    #Server(app).serve()
    # I don't know what this is
    app.secret_key = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.config['FLASK_ENV'] = 'development'
    #--------------------------------------
    app.run(host='0.0.0.0',port=int(os.environ.get("PORT","5000")), debug=True)


