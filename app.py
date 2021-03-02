from flask import Flask, render_template, request
app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/', methods=['POST'])
def getvalue():
    user_input_number = request.form['inputNumber']
    return render_template('pass.html', num=user_input_number)

if __name__ == '__main__':
    app.run(debug=True)
