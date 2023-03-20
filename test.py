from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import lxml

options = Options()
options.add_argument('--headless')

driver = webdriver.Chrome(r"C:\Users\edste\Downloads\chromedriver_win32\chromedriver.exe")

driver.get("https://www.amazon.com/s?k=headphones")
source = driver.page_source
soup = BeautifulSoup(source, "lxml")

def getPrice(newSoup):
    wholeNum = newSoup.find_all("span", attrs={'class':'a-price-whole'})
    fractNum = newSoup.find_all("span", attrs={'class':'a-price-fraction'})
    price = []
    if(len(wholeNum) == len(fractNum)):
        for i in range(0, len(wholeNum)): 
            price.append("$" + wholeNum[i].text + fractNum[i].text)
    return price

def getImage(newSoup):
    img = newSoup.find_all("img", attrs={'class':'s-image'})
    img_src = []
    for element in img:
        img_src.append(element['src'])
    return img_src

def getTitle(newSoup):
    try:
        title = newSoup.find_all("span", attrs={'class':'a-size-medium a-color-base a-text-normal'})
        titles = []
        for element in title:
            titles.append(element.text)
        print("Title found successfully.")
    except AttributeError:
        try: 
            title = newSoup.find_all("span", attrs={'class':'a-size-base-plus a-color-base a-text-normal'})
            titles = []
            for element in title:
                titles.append(element.text)
            print("Title found successfully.")
        except: 
            titles = []
            print("Title not found.")
    return titles

prices = getPrice(soup)
imgLinks = getImage(soup)
titles = getTitle(soup)
n = 1
for element in prices:
    print(element + " " + str(n))
    n+=1
n = 1
for element in imgLinks:
    print(element + " " + str(n))
    n+=1
n = 1
for element in titles:
    print(element + " " + str(n))
    n+=1