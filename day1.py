from flask import Flask , redirect , url_for

app = Flask(__name__)

@app.route("/success/<int:score>")
def success(score):
    return "<h1>My 12th Score is </h1>"+str(score) +"<h1>pass</h1>"

@app.route("/fail/<int:score>")
def fail(score):
    return "<h1>My 12th Score is </h1>"+str(score)+"<h1>fail</h1>"

@app.route("/result/<int:marks>")
def result(marks):
    result = ""
    if marks > 50:
        result = "success"
    else:
        result = "fail"
        
    return redirect(url_for(result ,  score=marks))


if __name__ == "__main__":
    app.run(debug=True)