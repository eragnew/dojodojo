from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)
app.secret_key = 'wow, much secret, so awesome'

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
	redirect_back = False
	if len(request.form['name']) < 1:
		flash('Name cannot be empty!')
		redirect_back = True
	if len(request.form['comment']) < 1:
		flash('Comment cannot be empty!')
		redirect_back = True
	if len(request.form['comment']) > 120:
		flash('Comment cannot be more than 120 characters!')
		redirect_back = True
	if redirect_back:
		return redirect('/')
	name = request.form['name']
	location = request.form['location']
	language = request.form['language']
	comment = request.form['comment']
	return render_template('process.html', name=name, location=location, language=language, comment=comment)

app.run(debug=True)
