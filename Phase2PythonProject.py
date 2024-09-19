#import libaries
from bs4 import BeautifulSoup
from requests import get
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
#Create Product Page Variable
product_page_url = ""

#Access Books to Scrape Category information (Poetry)
books_to_scrape_category_information_url = "https://books.toscrape.com/catalogue/category/books/poetry_23/index.html"
books_to_scrape_category_information_url_response = get(books_to_scrape_category_information_url)

#Category Informaiton Parsed HTML(Poetry)
soup=BeautifulSoup(books_to_scrape_category_information_url_response.content, 'html.parser')

#print(soup)

#Extract Books to Scrape Category Listing of Books (Poetry)
capture_categories = soup.find("ol", class_ = "row")
category_books = soup.find("li", class_= "col-xs-6 col-sm-4 col-md-3 col-lg-3")
category_books_article = soup.find("article", class_= "product_pod")
category_books = soup.find_all("a")
category_books_url = []
for category_book in category_books:
    category_books_url.append(category_book['href'])
        
print (category_books_url)

