import os
from flask import Flask, redirect

focus_url = os.environ.get('REDIRECT_URL', "http://www.example.com")
code_redirect = os.environ.get('REDIRECT_CODE', 302)
port = os.environ.get('PORT', 8080)
route = os.environ.get('ROUTE', '/')

app = Flask(__name__)


@app.route(route)
def hello():
    return redirect(focus_url, code=code_redirect)


if __name__ == '__main__':
    p = int(port)
    app.run(host='0.0.0.0', port=p)
