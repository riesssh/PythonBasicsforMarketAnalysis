#import libaries
from bs4 import BeautifulSoup
from requests import get
import requests
import csv

# Create Book Details Dictionary
book_details = {
    "product_page_url":"" , 
    "universal_product_code" :"", 
    "book_title" :"", 
    "price_including_tax" : "", 
    "price_excluding_tax" :"", 
    "quantity_available" : "", 
    "product_description" :"", 
    "category" :"", 
    "review_rating" : "", 
    "image_url" : ""
} 
#Parsed HTML Function
def parsed_HTML_function(url):
    parsed_HTML_page_response = requests.get(url)
    parsed_HTML_page_soup = BeautifulSoup(parsed_HTML_page_response.text, "html.parser")
    return parsed_HTML_page_soup


#Access Books to Scrape Informaiton 
books_to_scrape_url = "https://books.toscrape.com"
books_to_scrape_url_response = parsed_HTML_function(books_to_scrape_url)
print (books_to_scrape_url_response)

#Capture Book Categories
book_category_listing = books_to_scrape_url_response.find("div", class_="side_categories")
book_categories = books_to_scrape_url_response.find_all("a")
book_category_url_listing = []
for book_category_url in book_categories:
    book_category_url_listing.append(book_category_url["href"])
print (book_category_url_listing)


"""
#Books to Scrape Informaiton Parsed HTML
soup=BeautifulSoup(books_to_scrape_url_response.content, 'html.parser')

print(soup)

#Extract Books to Scrape Category Listing of Books (Poetry)
# """