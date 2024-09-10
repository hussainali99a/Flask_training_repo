from flask import Flask , redirect , url_for

app = Flask(__name__)

@app.route("/range1/<int:num>")
def range1(num):
    return "<h1>range is </h1>"+str(num) +"<h1>btw 101 to 201</h1>"

@app.route("/range2/<int:num>")
def range2(num):
    return "<h1>range is  </h1>"+str(num)+"<h1>btw 201 to 301</h1>"

@app.route("/range3/<int:num>")
def range3(num):
    return "<h1>range is  </h1>"+str(num)+"<h1>btw 301 to 401</h1>"

@app.route("/norange/<int:num>")
def norange(num):
    return "<h1>range is  </h1>"+str(num)+"<h1>no range </h1>"
@app.route("/result/<int:no>")
def result(no):
    result = ""
    if no > 101 and no<201:
        result = "range1"
    elif no > 201 and no<301:
        result = "range2"
    elif no > 301 and no<401:
        result = "range3"
    else:
        result = "norange"
        
    return redirect(url_for(result ,  num=no))


if __name__ == "__main__":
    app.run(debug=True)