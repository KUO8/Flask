from flask import Flask,session, render_template, request, url_for, redirect


app = Flask(__name__)
app.secret_key = 'Super_tayno'

@app.route('/index')
def index():
    return 'Пользователь: {}'.format(session.get('email','nn')) + '<p><a href="/logout">logout</a></p>'

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        email = request.form['email']
        session['email'] = email
        return redirect(url_for('index'))
    
@app.route('/logout')
def logout():
    session.pop('email', 'None')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()