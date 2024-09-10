from flask import Flask,redirect , url_for  , render_template , request

app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template('index.html')

@app.route("/result/<float:marks>")
def result(marks):
    result = ""
    if marks > 50:
        result = "pass"
        
    else:
        result = "fail"
        
    
    return render_template('result.html',res = result , marks = marks)

@app.route("/submit",methods=['GET','POST'])
def submit():
    total_score = 0
    if request.method =='POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        python = float(request.form['python'])
        django = float(request.form['django'])
        
        total_score = ((science+maths+python+django)/400)*100
    return redirect(url_for('result',marks = total_score))
        
        
if __name__ =="__main__":
    app.run(debug=True)