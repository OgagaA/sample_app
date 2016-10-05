from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    #return "Hey world!"
    return render_template('index.html')

#app.run()
app.run(debug=True)
# This allows us to see changes as we code rather than have to shut down.
# localhost:5000