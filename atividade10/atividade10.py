from flask import Flask, render_template, request, make_response, redirect, session
from datetime import datetime, timedelta, timezone

app = Flask(__name__, template_folder='templates')
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(seconds=30)
app.secret_key = 'EXA844'

@app.route('/')
def counter():
        
    counter_value = request.args.get('counter',default=0, type=int) + 1;

    if 'username' in session:
        username = session['username']
        running_time = (datetime.now(timezone.utc).replace(tzinfo=None) - session.get('_creation_time'))
        remaining_time = app.permanent_session_lifetime - running_time
        tempo = f' '+ str(remaining_time)+' '
    else:
        tempo = "A sessão ainda irá iniciar"

    if 'counter_cookie' in request.cookies:
        count = int(request.cookies.get('counter_cookie'))
    else:
        count = 1

    resp = make_response(render_template('atividade10.html', counter_cookie=count, counter=counter_value, time=tempo ))
    resp.set_cookie('counter_cookie', str(count + 1).encode('utf-8'), max_age=60*60)

    return resp

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    session['username'] = username
    session['_creation_time'] = datetime.now(timezone.utc)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
    
