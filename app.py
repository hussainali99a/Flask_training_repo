from flask import Flask

app = Flask(__name__)

      
@app.route('/')
def hello():
    return "<h1>Hello AIDS/CSE/EC Students</h1>"

@app.route('/home')
def home():
    return "<h1>You are in home page , Welcome to Sistec in Bhopal</h1>"

if __name__ =="__main__":
    app.run(debug=True)