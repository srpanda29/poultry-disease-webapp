from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', temperature=28, humidity=65, ammonia=15, status="Healthy")

if __name__ == '__main__':
    app.run(debug=True)
