from flask import Flask, render_template,request
import stats
import parser




app = Flask(__name__)

@app.route("/")
@app.route("/home")

def hello():
    return render_template('home.html')



@app.route("/about")
def about():
    return "<h1> About Page </h1>"

@app.route('/', methods=['GET','POST'])
def send():
     if request.method == 'POST':
         stats.loadData()



if __name__ == "__main__":
    app.run(debug=True)
