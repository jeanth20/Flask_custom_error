# server.py file
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("home.html")

def genericErrorHandler(error):
    return render_template("message.html", title=error.name, message=error.description), error.code

for errCode in [400, 401, 403, 404]:
    app.register_error_handler(errCode, genericErrorHandler)


@app.errorhandler(500)
@app.errorhandler(501)
def serverError(error):
    return render_template("message.html", title="Internal Server Error", message="Some Internal Error occured..."), error.code


app.run(host="0.0.0.0", port=50100, debug=True)