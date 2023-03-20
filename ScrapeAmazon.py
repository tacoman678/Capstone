from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import lxml
import pandas as pd

def intialize(product):
    if ' ' in product:
        query = product.split(" ")
        x = ""
        for i in range(len(query)):
            x += query[i]
            if i < (len(query) - 1):
                x += "+"
        URL = "https://www.amazon.com/s?k=" + x
    else:
        URL = "https://www.amazon.com/s?k=" + product
    options = Options()
    options.add_argument('--headless')
    browser = webdriver.Chrome(r"C:\Users\edste\Downloads\chromedriver_win32\chromedriver.exe", options=options)
    browser.get(URL)
    html = browser.page_source
    browser.quit()
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def getPrice(newSoup):
    try:
        wholeNum = newSoup.find_all("span", attrs={'class':'a-price-whole'})
        fractNum = newSoup.find_all("span", attrs={'class':'a-price-fraction'})
        price = []
        if(len(wholeNum) == len(fractNum)):
            for i in range(0, len(wholeNum)): 
                price.append("$" + wholeNum[i].text + fractNum[i].text)
        print("Price found successfully.")
    except AttributeError:
            price = ""
            print("Price not found.")
    return price
    

def getImage(newSoup):
    try:
        img = newSoup.find_all("img", attrs={'class':'s-image'})
        img_src = []
        for element in img:
            img_src.append(element['src'])
        print("Image found successfully.")
    except AttributeError:
        img_src = []
        print("Image not found.")
    return img_src

def getTitle(newSoup):
    search = newSoup.find("span", attrs={'class':'a-color-state a-text-bold'})
    if " " in search.text:
        title = newSoup.find_all("span", attrs={'class':'a-size-medium a-color-base a-text-normal'})
        titles = []
        for element in title:
            titles.append(element.text)
        print("Title found successfully.")
        return titles
    try:
        title = newSoup.find_all("span", attrs={'class':'a-size-base-plus a-color-base a-text-normal'})
        titles = []
        for element in title:
            titles.append(element.text)
        print("Title found successfully.")
    except AttributeError:
        titles = []
        print("Title not found.")
    return titles

def format(titles, prices, imgs, bound):
    panda = pd.DataFrame({'titles': titles[:bound], 'prices': prices[:bound], 'imgs': imgs[:bound]})
    return panda