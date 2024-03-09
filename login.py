from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory user data (replace with database in a production environment)
users = {'user1': 'password1', 'user2': 'password2'}

@app.route('/')
def login_page():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username in users and users[username] == password:
        # Successful login, redirect to a dashboard or home page
        return f'Welcome, {username}! (Redirect to dashboard/home here)'
    else:
        # Failed login, redirect back to the login page with an error message
        return redirect(url_for('login_page', error='Invalid username or password'))

if __name__ == '__main__':
    app.run(debug=True)
