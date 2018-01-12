from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/workout')
def workout():
    return render_template('workout.html')

if __name__ == '__main__':
    app.run(port='80')
