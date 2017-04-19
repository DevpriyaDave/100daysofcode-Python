from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('welcome.html')


@app.route('/login', methods=['GET'])
def login(username, password):
    if request.method == 'POST':
        return render_template('login.html')
    


@app.route('/profile/<username>', methods=['GET', 'POST'])
def profile(username, password):
    # database connection to get data for that user and display
    return render_template('profile.html', username, password)


if __name__ == "__main__":
    app.run(debug=True)

