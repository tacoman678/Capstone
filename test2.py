from time import sleep
from selenium import webdriver
from bs4 import BeautifulSoup
import lxml
from selenium.webdriver.chrome.options import Options

def getLink(product):
    x = ""
    for i in range (len(product)):
        x += product[i]
        if i < (len(product) - 1):
            x+= "+"
    return "https://www.amazon.com/s?k=" + x

query = input("Please enter a product you would like to find:\n")
URL = getLink(query.split(" "))

#Create options object for headless mode
options = Options()
options.add_argument('--headless')

#create a new Chrome browser instance
browser = webdriver.Chrome(r"C:\Users\edste\Downloads\chromedriver_win32\chromedriver.exe", options=options)

browser.get(URL)

#save the HTML content of the webpage to a string
html = browser.page_source

browser.quit()
soup = BeautifulSoup(html, 'html.parser')

#finds all the links to each product in the search results on amazon and adds them to an array
links = soup.find_all("a", attrs={'class':'a-link-normal s-no-outline'})
links_list = []
for element in links:
    links_list.append(element.get('href')) #adds each link to the array
    
    
#given an html parse tree this method finds the product title
def get_title(soup):
    try:
        title = soup.find("span", attrs={"id":'productTitle'}).string.strip() #finds the product title HTML tags and converts the text into strings
        print("Title found successfully.")
    except AttributeError: #if there is no title found assign it a blank title
        title = ""
        print("Title not found.")
    return title

#given an html parse tree this method finds the price title
def get_price(soup):
    try:
        price = soup.find("span", attrs={'id':'priceblock_ourprice'}).string.strip() #finds the product price HTML tags and converts the text into strings
        print("Price found successfully.")
    except AttributeError:#if there is no price found check if there is a deal price or assign it a blank title
        try:
            # If there is some deal price
            price = soup.find("span", attrs={'id':'priceblock_dealprice'}).string.strip()
            print("Deal Price found successfully.")
        except:
            price = ""
            print("Price not found.")
    return price

# Function to extract Product Rating
def get_rating(soup):
	try:
		rating = soup.find("i", attrs={'class':'a-icon a-icon-star a-star-4-5'}).string.strip()
		print("Rating found successfully.")
	except AttributeError:
		try:
			rating = soup.find("span", attrs={'class':'a-icon-alt'}).string.strip()
			print("Rating found successfully.")
		except:
			rating = ""	
			print("Rating not found.")
	return rating

# Function to extract Number of User Reviews
def get_review_count(soup):
	try:
		review_count = soup.find("span", attrs={'id':'acrCustomerReviewText'}).string.strip()
		print("Review count found successfully.")
	except AttributeError:
		review_count = ""	
		print("Review count not found.")
	return review_count

# Function to extract Availability Status
def get_availability(soup):
	try:
		available = soup.find("div", attrs={'id':'availability'})
		available = available.find("span").string.strip()
		print("Availability found successfully.")
	except AttributeError:
		available = "Not Available"	
		print("Availability not found.")
	return available

for i in range(0,1):
    new_browser = webdriver.Chrome(r"C:\Users\edste\Downloads\chromedriver_win32\chromedriver.exe", options=options)
    new_browser.get("https://www.amazon.com" + links_list[i])
    new_html = new_browser.page_source
    new_browser.quit()
    new_soup = BeautifulSoup(new_html, "lxml") #creates a HTML parse tree for each link
    print("Product Title =", get_title(new_soup)) #passes HTML parse tree to get_title() method and prints out the title of the product
    print("Product Price =", get_price(new_soup)) #passes HTML parse tree to get_price() method and prints out the price of the product
    print("Product Rating =", get_rating(new_soup))
    print("Number of Product Reviews =", get_review_count(new_soup))
    print("Availability =", get_availability(new_soup))