from flask import Flask, request, render_template_string, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'supersecretkey'

FLAG = "flag{logic_flaw_auth_bypass}"

login_page = '''
<!doctype html>
<title>Login</title>
<h2>Login</h2>
<form method="POST">
  Username: <input type="text" name="username"><br>
  Password: <input type="text" name="password"><br>
  <input type="submit" value="Login">
</form>
{% if error %}
<p style="color:red;">{{ error }}</p>
{% endif %}
'''

flag_page = '''
<!doctype html>
<title>Admin Panel</title>
<h2>Welcome, Admin!</h2>
<p>Here is your flag: <code>{{ flag }}</code></p>
'''

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form.get('username', '')
        password = request.form.get('password', '')
        # Flawed logic: allows login if username == password
        if username == password:
            session['user'] = username
            return redirect(url_for('flag'))
        else:
            error = "Invalid credentials."
    return render_template_string(login_page, error=error)

@app.route('/flag')
def flag():
    if session.get('user') == 'admin':
        return render_template_string(flag_page, flag=FLAG)
    return redirect(url_for('login'))