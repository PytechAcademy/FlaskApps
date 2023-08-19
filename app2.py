# Routing and views
from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    return 'Welcome to the homepage!'
@app.route('/about')
def about():
    return 'This is the About page.'
@app.route('/contact')
def contact():
    return 'You can reach us at contact@example.com.'
if __name__ == '__main__':
    app.run(debug=True)