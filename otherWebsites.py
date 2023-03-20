from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import lxml
from lxml import etree


driver = webdriver.Chrome(r"C:\Users\edste\Downloads\chromedriver_win32\chromedriver.exe")

driver.get("https://www.etsy.com/search?q=hats")
tree = etree.fromstring(driver.page_source, etree.HTMLParser())
soup = BeautifulSoup(driver.page_source, "lxml")

def getTitle(newSoup, tree):
    xpath = '/html/body/main/div/div[1]/div/div[3]/div[9]/div[2]/div[10]/div[1]/div[1]/div/ol/li[1]/div/div/a/div[2]/h3'
    element = tree.xpath(xpath)[0]
    class_name = element.get('class')
    print(class_name)
    title = newSoup.find_all("h3", attrs={'class':'cwt-text-caption.v2-listing-card__title.wt-text-truncate'})
    titles = []
    for element in title:
        titles.append(element.text)
    return titles

titles = getTitle(soup, tree)
print(titles)