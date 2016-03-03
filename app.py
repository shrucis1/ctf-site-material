from mail import *
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if validate_email(request.form['email']):
            name = request.form['name']
            email_address = request.form['email']
            if not get_list('ctfmembers'):
                if not create_list('ctfmembers'):
                    print("Error Creating Mailing List")
                    return render_template('index.html', create_list_error=True)
                else:
                    print("Mailing List Created")
                if add_user_to_list(name, email_address, 'ctfmembers'):
                    if send_confirmation_email(name, email_address):
                        return render_template('index.html', success=True)
                    else:
                        return render_template('index.html', conf_email_error=True)
                else:
                    return render_template('index.html', add_error=True)
            else:
                if add_user_to_list(name, email_address, 'ctfmembers'):
                    if send_confirmation_email(name, email_address):
                        return render_template('index.html', success=True)
                    else:
                        return render_template('index.html', conf_email_error=True)
                else:
                    return render_template('index.html', add_error=True)
        else:
            return render_template('index.html', invalid_email=True)
    else:
        return render_template('index.html')

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/rules/')
def rules():
    return render_template('rules.html')

@app.route('/prep/')
def prep():
    return render_template('prep.html')

if __name__ == '__main__':
    app.run(port=9020)
