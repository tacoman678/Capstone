from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep
import pandas as pd

driver = webdriver.Chrome()

def getTitles(soup):
    title = soup.find_all("div", attrs={'class': 'Truncate-sc-10p6c43-0 flAIvs'})
    titles = []
    for element in title:
        titles.append(element.text)
    return titles

def getPrices(newSoup):
    price = newSoup.find_all("div", attrs={'class': 'h-padding-r-tiny'})
    prices = []
    for element in price:
        temp = element.find("span", attrs={'data-test':'current-price'})
        prices.append(temp.text)
    return prices


def getImages(newSoup):
    img_src = newSoup.find_all(
        "div", attrs={'class':'ProductCardImage__PicturePrimary-sc-rhvnbj-0 eavXsa'})
    imgs = []
    i=0
    for i in range(0,len(img_src)-4):
        temp = img_src[i].find("img")
        imgs.append(temp['src'])
    return imgs


def getLinks(soup):
    links_src = soup.find_all("div", attrs={'class': 'Truncate-sc-10p6c43-0 flAIvs'})
    links = []
    for element in links_src:
        temp = element.find("a")
        links.append(temp['href'])
    return links

def format_data(titles, prices, imgs, links, bound):
    data = {'target_title': titles[:bound], 'target_price': prices[:bound],
            'target_image': imgs[:bound], 'target_link': links[:bound]}
    df = pd.DataFrame(data)
    return df

driver.get("https://www.target.com/s?searchTerm=socks+for+guys")
sleep(1)
driver.execute_script("window.scrollTo(0, 1000)")
sleep(3)
html = driver.page_source
driver.quit()
soup = BeautifulSoup(html, 'html.parser')
print(getTitles(soup))
print(getPrices(soup))
print(getImages(soup))
print(getLinks(soup))