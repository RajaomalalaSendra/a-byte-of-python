from flask import Flask
from flask import request, render_template
#code which helps initialize our server
app = Flask(__name__)

# the root in flask
@app.route('/')
def index_all():
	return render_template('index_all.html')

#defining a /hello route for only post requests
@app.route('/hello')
def index():
    #grabs the data tagged as 'name'
    name = request.get_json()['name']
    
    #sending a hello back to the requester
    return render_template("hello.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0',port='9999', debug=True)