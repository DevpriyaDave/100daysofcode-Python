from flask import Flask

app = Flask(__name__)


@app.route('/landingpage')
def landingpage():
    return 'This is landing page'

if __name__ == "__main__" :
    app.run(debug=True)













