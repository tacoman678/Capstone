from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd

def search_product(product):
    if isinstance(product, str):
        query = "+".join(product.split())
        URL = f"https://www.amazon.com/s?k={query}"
    else:
        raise TypeError("product must be a string")
        
    options = Options()
    options.add_argument('--headless')
    browser = webdriver.Chrome(r"C:\Users\edste\Downloads\chromedriver_win32\chromedriver.exe", options=options)
    browser.get(URL)
    html = browser.page_source
    browser.quit()
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def get_prices(soup):
    whole_nums = soup.find_all("span", attrs={'class':'a-price-whole'})
    fract_nums = soup.find_all("span", attrs={'class':'a-price-fraction'})
    prices = []
    if len(whole_nums) == len(fract_nums):
        for i in range(len(whole_nums)): 
            price = f"${whole_nums[i].text}{fract_nums[i].text}"
            prices.append(price)
    return prices

def get_images(soup):
    imgs = soup.find_all("img", attrs={'class':'s-image'})
    img_srcs = []
    for img in imgs:
        if "SS" not in img['src']:
            img_srcs.append(img['src'])
    return img_srcs

def get_titles(soup, product):
    if " " in product:
        titles = soup.find_all("span", attrs={'class':'a-size-medium a-color-base a-text-normal'})
    else:
        titles = soup.find_all("span", attrs={'class':'a-size-base-plus a-color-base a-text-normal'})

    return [title.text for title in titles]

def get_links(soup):
    links = soup.find_all("a", attrs={'class':'a-link-normal s-no-outline'})
    links_list = []
    for link in links:
        links_list.append("https://www.amazon.com" + link.get('href'))
    return links_list

def format_data(titles, prices, imgs, links, bound):
    data = {'amazon_title': titles[:bound], 'amazon_price': prices[:bound], 'amazon_image': imgs[:bound], 'amazon_link': links[:bound]}
    df = pd.DataFrame(data)
    return df