from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
@app.route("/home")

def hello():
    return render_template('home.html')



@app.route("/about")
def about():
    return "<h1> About Page </h1>"

@app.route('/background_process_test')
def background_process_test():
    return


if __name__ == "__main__":
    app.run(debug=True)
