from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/chart')
def chart():
    return render_template('charts.html')

@app.route('/us')
def us():
    return render_template('aboutUs.html')

@app.route('/rc')
def rc():
    return render_template('RemoteControl.html')

if __name__ == '__main__':
    app.debug = True
    app.run()
    #app.run(host='192.168.0.4')
    #app.run(host='0.0.0.0')