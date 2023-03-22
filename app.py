from flask import Flask, render_template, request
from ScrapeAmazon import search_product as initializeAmazon, get_titles as getAmazonTitle, get_images as getAmazonImage, get_prices as getAmazonPrice, get_links as getAmazonLinks, format_data as formatAmazon
from ScrapeEbay import search_product as initializeEbay, getTitle as getEbayTitle, getImage as getEbayImage, getPrice as getEbayPrice, get_links as getEbayLinks, format_data as formatEbay
import pandas as pd

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
    soup_amazon = initializeAmazon(input)
    soup_ebay = initializeEbay(input)
    amazon_data = formatAmazon(getAmazonTitle(soup_amazon, input), getAmazonPrice(soup_amazon), getAmazonImage(soup_amazon), getAmazonLinks(soup_amazon), int(numInput))
    ebay_data = formatEbay(getEbayTitle(soup_ebay), getEbayPrice(soup_ebay),getEbayImage(soup_ebay), getEbayLinks(soup_ebay), int(numInput))
    data = pd.concat([amazon_data, ebay_data], axis=1)
    print(data.to_string())
    print(data.info())
    return render_template('result.html', df=data)
if __name__ == '__main__':
    app.run(debug=True)