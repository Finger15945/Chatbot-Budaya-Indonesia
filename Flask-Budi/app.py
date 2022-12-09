from process import chatbot_response, Response
from flask import Flask, render_template, request, url_for, redirect

#Start Chatbot
app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template("welcome.html")

@app.route('/home', methods=['GET', 'POST'])
def cool_form():
    if request.method == 'POST':
        return redirect(url_for('welcome'))

    return render_template('home.html')

@app.route("/get")
def get_bot_response():
    user_input = str(request.args.get('msg'))
    result = chatbot_response(user_input)
    return result

if __name__ == "__main__":
    app.run(debug=True)