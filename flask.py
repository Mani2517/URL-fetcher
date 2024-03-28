from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    url = input("Enter URL:")
    try:
        response = requests.get(url)
        response_code = response.status_code
    except requests.RequestException as e:
        response_code = str(e)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)