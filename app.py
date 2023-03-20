from flask import Flask, render_template, request
from ScrapeAmazon import intialize, getTitle, getImage, getPrice, format

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/documentation')
def documentation():
    return render_template('documentation.html')
@app.route('/search')
def search():
    return render_template('search.html')
@app.route('/result', methods=['POST'])
def result():
    input = request.form['myinput']
    numInput = request.form['menu']
    soup = intialize(input)
    data = format(getTitle(soup), getPrice(soup), getImage(soup), int(numInput))
    return render_template('result.html', df=data)
if __name__ == '__main__':
    app.run(debug=True)