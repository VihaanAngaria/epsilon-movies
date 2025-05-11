from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/watch')
def watch():
    return redirect('/sponsor')

@app.route('/sponsor')
def sponsor():
    # Redirect to sponsor (Shotify) link
#    return redirect("https://shrtlk.click/81jy8")

@app.route('/afterSponsor')
def after_sponsor():
    # Redirect to NetMirror after sponsor
    return redirect("https://netfree2.cc/login")

if __name__ == '__main__':
    app.run(debug=True)
