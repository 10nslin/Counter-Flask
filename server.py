'''
Scott Enslin

Create a simple web application that holds a counter that increments every time the page is visited.
 Complete this using session.

'''


from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'very secret'


@app.route('/')
def counter():
    try:
        session['counter'] += 1
    except:
        session['counter'] = 1
    return render_template('index.html')

@app.route('/ninjas', methods=['POST'])
def increment():
   session['counter'] += 1 
   return redirect('/')

@app.route('/hackers', methods=['POST'])
def reset():
    session['counter'] = 0
    return redirect('/')

app.run(debug=True)