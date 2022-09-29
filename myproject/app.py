from ssl import HAS_TLSv1_1
from flask import Flask,redirect,render_template,url_for,request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hel, World!</p>"
    # return "<p>Hello, Vikas it's Flask</p>" 
@app.route("/hello")
def hello():
    return "<p>Hel, World! its vikas kushwaha from Lucknow</p>"   


@app.route("/html")
def html():
    return render_template('index.html') 

@app.route("/form",methods=['POST','GET'])
def submit():
    return "submitted"

@app.route("/score/<int:score>")
def world(score):
    if score<=50:
        return "failed" +str(score)
    elif score>70 and score<90:
        return "good performance" + str(score)    

    
    elif score>50 and score<70:
        return "passed performance" + str(score)    
    else:
        return "passed with excellent performance"+ str(score)    
    # return "<h1> Hello, World! lorem!</h1> " + str(score)
                

if __name__=='__main__':
    app.run(debug=True)   