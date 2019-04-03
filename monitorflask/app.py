from flask import Flask
from flask import render_template
import flask_monitoringdashboard as dashboard

app = Flask(__name__)
dashboard.bind(app)

@app.route('/')
def index():
	return 'Hello World'
if __name__ == '__main__':
    app.run(debug=True)