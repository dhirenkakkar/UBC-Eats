
from flask import Flask, render_template,request,redirect
import stats
import parser
import grapher
import config




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
         config.loaded = False
         stats.loadData()
         grapher.heatMap()
         grapher.pieChart("01-01-2000","01-01-2100")
         return redirect('/dashboard')

@app.route('/dashboard')
def dash():

    return render_template('index.html')
@app.route('/heatmap')
def heatmap():
    return render_template('heatmap.html')

@app.route('/piechart')
def piechart():
         # grapher.pieChart("01-01-2000", "01-01-2100")
         return render_template('piechart.html')


app.jinja_env.globals.update(stats_total=stats.total)
app.jinja_env.globals.update(stats_avg=stats.avg)
app.jinja_env.globals.update(stats_stDev=stats.stDev)
app.jinja_env.globals.update(stats_var=stats.var)

if __name__ == "__main__":
    app.run(debug=True)
