from flask import Flask
from flask import render_template
import flask_monitoringdashboard as dashboard

app = Flask(__name__)
dashboard.bind(app)

@app.route('/')
def index():
	return render_template('index.html')
if __name__ == '__main__':
    app.run(host='0.0.0.0',port='9999', debug=True)