from flask import Flask, request, make_response
app = Flask(__name__)

@app.route("/")
def home():
    role = request.cookies.get("role", "guest")
    if role == "admin":
        return "Welcome admin! Flag: flag{cookie_privilege_escalation}"
    return "Hello guest! You need admin rights."

@app.route("/set")
def set_cookie():
    resp = make_response("Cookie set")
    resp.set_cookie("role", "guest")
    return resp

app.run(host='0.0.0.0', port=5000)