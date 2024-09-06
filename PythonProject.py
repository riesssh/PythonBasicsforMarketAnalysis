#Import Libaries
import pandas
from bs4 import BeautifulSoup
import requests

#Access Books to Scrape Web Page
books_to_scrape_url = "https://books.toscrape.com/"
books_to_scrape_url_response = requests.get(books_to_scrape_url)
print(books_to_scrape_url_response.content)



#Define Books to Scrape Web Site HTML to be parsed
#books_to_scrape_html_content =



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

#print Book Details
print (book_details.keys())
