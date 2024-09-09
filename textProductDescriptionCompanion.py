from bs4 import BeautifulSoup
from requests import get

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

# Access Books to Scrape A Light in the Attic Book Web Page
books_to_scrape_a_light_in_the_attic_url = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
books_to_scrape_a_light_in_the_attic_url_response = get(books_to_scrape_a_light_in_the_attic_url)

# A Light in the Attic Parsed HTML
soup = BeautifulSoup(books_to_scrape_a_light_in_the_attic_url_response.content, 'html.parser')

# Get the Book Details

# Capture the Book's Description
product_description = soup.find('div', id='product_description')
description = product_description.find_next_sibling('p').text
book_details["product_description"] = description

print(book_details["product_description"])