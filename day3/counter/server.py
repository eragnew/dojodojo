from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'Wow, such secret, much wow.'

@app.route('/')
def index():
  if session.get('count'):
	session['count'] += 1
  else:
	session['count'] = 1
  return render_template('index.html')

@app.route('/plus_two', methods=['POST'])
def plus_two():
  session['count'] += 1
  return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
	session['count'] = 0
	return redirect('/')

app.run(debug=True)
