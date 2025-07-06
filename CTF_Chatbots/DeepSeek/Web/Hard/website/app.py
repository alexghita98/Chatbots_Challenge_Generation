from flask import Flask, request, render_template_string

app = Flask(__name__)

FLAG = "FLAG{ssti_2_rce_1337}"

@app.route('/')
def home():
    name = request.args.get('name', 'Guest')
    template = f"<h1>Hello {name}!</h1>"
    return render_template_string(template)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)