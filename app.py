from flask import Flask, render_template
from flask_mail import Mail, Message
from flask import request,flash


app = Flask(__name__)

app.config.from_object('config.Config')

mail = Mail(app)

@app.route('/' , methods =["GET", "POST"] )
def hello():
    if request.method == "POST":
       # getting input with name = fname in HTML form
       print(request.form.get("email"))
       flash(f'Thanks for submiit created', 'success')
    return render_template('index.html')

@app.route('/form' , methods =["POST"] )
def form_data():
    if request.method == "POST":
       # getting input with name = fname in HTML form
       name = request.form.get("name")
       email = request.form.get("email")
       phone_no = message = request.form.get("phone")
       message = request.form.get("message")
       subject = "New Client Query"
       msg = Message(subject, sender = 'support@qubitnets.com', recipients = ['support@qubitnets.com'])
       msg.body = f"Hey qubitnets, {name} is trying to contact us. Email : {email} , Phone_no {phone_no},message {message}, "
       mail.send(msg)
       return "Success",200

if __name__ == '__main__':
    context = ('certificate.crt', 'private.key')
    app.run(host='0.0.0.0', port=80, ssl_context=context)
    # app.run(host='0.0.0.0', port=80)

# @app.route("/send")
# def index():
#     msg = Message('Hello from the other side!', sender = 'support@qubitnets.com', recipients = ['viveksood92@gmail.com'])
#     msg.body = "Hey Paul, sending you this email from my Flask app, lmk if it works"
#     mail.send(msg)
#     return "Message sent!"