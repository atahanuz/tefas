from flask import Flask, render_template
import main


app = Flask(__name__)
text= main.main("MAC","AFT","IPJ","TCD","TKF","AEH")

@app.route('/')
def home():
    return render_template('index.html', text=text)

if __name__ == '__main__':

    app.run(debug=True)
