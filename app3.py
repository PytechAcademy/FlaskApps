from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    app_name = 'My Awesome App'
    message = 'Enjoy your stay!'
    return render_template('index.html', app_name=app_name, message=message)

if __name__ == '__main__':
    app.run(debug=True)
