from flask import Flask  # this is use to create app object.
from flask import render_template # this is use to render any custom .html file placed in template folder.
from flask import request  # this is used to get the nature of the requirest. [GET OR POST]
from flask import redirect,url_for # these are used for redirecting to the url and sending parameters.
from flask import jsonify
# create a new application.

app = Flask(__name__)

# this home page content of application.
@app.route("/",methods=["GET"])
def welcome():
    return "<h1>This is the flask Home page.</h1>"

# this is the content shown after we route to /index.
@app.route('/index',methods=['GET'])
def index():
    return "<h2>This is the index page</h2>"

# here we can pass varible to the url and use it in function.
# if we are providing it Type along with var then it is call variable Rule.
@app.route('/success/<int:score>') # by defult GET.
def success(score):
    return "The Passed score is "+ str(score)

@app.route('/fail/<int:score>') # by defult GET.
def fail(score):
    return "The Failed score is "+ str(score)

@app.route('/form',methods=['GET','POST'])
def form():
    if request.method=='GET':
        return render_template('form.html')
    else:
        maths = float(request.form['maths_score'])
        science = float(request.form['science_score'])
        hisotry = float(request.form['history_score'])

        avg_marks = (maths+science+hisotry)/3
        
        if avg_marks>50:
            res = 'success'
        else:
            res = 'fail'
        
        return redirect(url_for(res,score=avg_marks))
        
        # return render_template('form.html',score=avg_marks)

@app.route('/api',methods=['POST'])
def sumofnumbers():
    data = request.get_json()
    a = dict(data)['a']
    b = dict(data)['b']

    return jsonify(a+b)

if __name__=="__main__":
    app.run(debug=True) # here here debug parameter help me to debug without closing flask server.
