from flask import Flask, request, make_response, render_template_string, redirect, url_for

app = Flask(__name__)

FLAG = "flag{cookie_tampering_success}"

index_page = '''
<!doctype html>
<title>Cookie Monster</title>
<h2>Welcome to Cookie Monster!</h2>
<p><a href="/login">Login</a> | <a href="/admin">Admin Panel</a></p>
'''

login_page = '''
<!doctype html>
<title>Login</title>
<h2>Login</h2>
<form method="POST">
  Username: <input type="text" name="username"><br>
  <input type="submit" value="Login">
</form>
'''

admin_page = '''
<!doctype html>
<title>Admin Panel</title>
<h2>Welcome, Admin!</h2>
<p>Here is your flag: <code>{{ flag }}</code></p>
'''

@app.route('/')
def index():
    return render_template_string(index_page)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username', '')
        resp = make_response(redirect(url_for('index')))
        # Insecure: sets role in cookie without validation
        resp.set_cookie('role', 'admin' if username == 'admin' else 'user')
        return resp
    return render_template_string(login_page)

@app.route('/admin')
def admin():
    role = request.cookies.get('role', 'user')
    if role == 'admin':
        return render_template_string(admin_page, flag=FLAG)
    return "<h2>Access Denied</h2><p>You must be an admin to view this page.</p>", 403

# No app.run() here — Gunicorn will handle it
