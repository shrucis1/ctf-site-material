from mail import *
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email_address = request.form['email']
        if not validate_email(email_address):
            return render_template("index.html", invalid_email=True)

        if not add_user_to_list(name, email_address, "ctfmembers"):
            return render_template("index.html", add_error=True)

        if not send_confirmation_email(name, email_address):
            return render_template("index.html", conf_email_error=True)

        return render_template("index.html", success=True)

    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(port=9020)
