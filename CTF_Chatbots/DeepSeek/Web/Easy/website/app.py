from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Homepage. Find the /admin panel!"

@app.route('/admin')
def admin():
    return "FLAG{w3b_p4th_tr4v3rs4l}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)