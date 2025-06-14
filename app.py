from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return redirect('/contact')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/submit_feedback', methods=['POST'])
def submit_feedback():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    # For now, just print it — later you can store in a file or database
    print(f'Name: {name}, Email: {email}, Message: {message}')

    return "<h2 style='color:white; text-align:center;'>Thanks for your feedback!</h2>"

if __name__ == '__main__':
    app.run(debug=True)
