# Download the helper library from https://www.twilio.com/docs/python/install
import os
from flask import Flask, request, jsonify, render_template, redirect, url_for
from twilio.rest import Client


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')


# Define Verify_otp() function
@app.route('/login' , methods=['POST'])
def verify_otp():
    username = request.form['username']
    password = request.form['password']
    mobile_number = request.form['number']

    if username == 'verify' and password == '12345':   
        account_sid = 'ACdfc9800d2dac621edad0294a1475b5ae'
        auth_token = 'b9ca66a2b05c9a1e2d00026d43d25f17'
        client = Client(account_sid, auth_token)

        verification = client.verify \
            .services('VA8fb60db1b5c7c8eee3082018dc73efad') \
            .verifications \
            .create(to=mobile_number, channel='sms')

        print(verification.status)
        return render_template('otp_verify.html')
    else:
        return render_template('user_error.html')



@app.route('/otp', methods=['POST'])
def get_otp():
    print('Processing...')

    received_otp = request.form['received_otp']
    mobile_number = request.form['number']

    account_sid = 'ACdfc9800d2dac621edad0294a1475b5ae'
    auth_token = 'b9ca66a2b05c9a1e2d00026d43d25f17'
    client = Client(account_sid, auth_token)
                                            
    verification_check = client.verify \
        .services('VA8fb60db1b5c7c8eee3082018dc73efad') \
        .verification_checks \
        .create(to=mobile_number, code=received_otp)
    print(verification_check.status)

    if verification_check.status == "pending":
        return render_template('otp_error.html')    # Write code here
    else:
        return redirect("https://collaborative-document-epwj.onrender.com")


if __name__ == "__main__":
    app.run()

