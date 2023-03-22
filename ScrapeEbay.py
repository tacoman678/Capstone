from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import lxml
import pandas as pd

def search_product(product):
    URL = f"https://www.ebay.com/sch/i.html?_nkw={product}"
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(r"C:\Users\edste\Downloads\chromedriver_win32\chromedriver.exe", options=options)
    driver.get(URL)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()
    return soup

def getTitle(newSoup):
    title = newSoup.find_all("span", attrs = {'role':'heading'})
    titles = []
    for element in title:
        titles.append(element.text)
    print("Title found successfully.")
    return titles

def getPrice(newSoup):
    price = newSoup.find_all("span", attrs = {'class':'s-item__price'})
    prices = []
    for element in price:
        prices.append(element.text)
    print("Price found successfully.")
    return prices

def getImage(newSoup):
    img_src = newSoup.find_all("div", attrs = {'class':'s-item__image-wrapper image-treatment'})
    imgs = []
    for element in img_src:
        temp = element.find("img")
        imgs.append(temp['src'])
    print("Image found successfully.")
    return imgs

def get_links(soup):
    links_src = soup.find_all("div", attrs = {'class':'s-item__title-section'})
    links = []
    for element in links_src:
        temp = element.find("a")
        links.append(temp['href'])
    print("Links found successfully.")
    return links

def format_data(titles, prices, imgs, links, bound):
    data = {'ebay_title': titles[1:bound+1], 'ebay_price': prices[1:bound+1], 'ebay_image': imgs[1:bound+1], 'ebay_link': links[1:bound+1]}
    df = pd.DataFrame(data)
    return df
