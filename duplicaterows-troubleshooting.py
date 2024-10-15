#Import Libaries
import pandas
from bs4 import BeautifulSoup
import requests
from requests import get
import csv
import urllib.parse



#Access Books to Scrape Web Page
books_to_scrape_url = "https://books.toscrape.com/catalogue/category/books/poetry_23/index.html"
books_to_scrape_url_response = get(books_to_scrape_url)
#print(books_to_scrape_url_response.content)
#print(' ')

def get_book_details(book_url):
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
    #Access Books to Scrape Book Web Page
    #print (book_url)
    books_to_scrape_book_url = urllib.parse.urljoin(books_to_scrape_url, book_url)
    books_to_scrape_book_url_response = requests.get(books_to_scrape_book_url)
    

    #  Book Parsed HTML
    soup = BeautifulSoup(books_to_scrape_book_url_response.content, 'html.parser')
    #print(soup)

    # Get the Book Details

    # Catputre the Book's Product Page URL
    product_page_url = books_to_scrape_book_url
    book_details['product_page_url'] = product_page_url
    #print(product_page_url)

    # Catputre the Book's Universal Product Code
    universal_product_code = soup.find('th',string='UPC')
    if universal_product_code:
        universal_product_code = universal_product_code.find_next('td').get_text()
    else:
        universal_product_code = 'N/A'  
    book_details['universal_product_code'] = universal_product_code
    #print(universal_product_code)

    # Catputre the Book's Title
    book_title = soup.h1.string
    book_details['book_title'] = book_title
    #print(book_title)

    # Catputre the Book Price, including tax
    price_including_tax = soup.find('th', string='Price (incl. tax)')
    if price_including_tax:
        price_including_tax = price_including_tax.find_next('td').get_text()
    else:
        price_including_tax = 'N/A'
    book_details['price_including_tax'] = price_including_tax
    #print(price_including_tax)

    # Catputre the Book Price, excluding tax
    price_excluding_tax = soup.find('th', string='Price (excl. tax)')
    if price_excluding_tax:
        price_excluding_tax = price_excluding_tax.find_next('td').get_text()
    else:
        price_excluding_tax = 'N/A'
    book_details['price_excluding_tax'] = price_excluding_tax
    #print(price_excluding_tax)

    # Capature the Number of Books Available
    quantity_available = soup.find('th', string='Availability')
    if quantity_available:
        quantity_available = quantity_available.find_next('td').get_text()
    else:
        quantity_available = 'N/A'
    book_details['quantity_available'] = quantity_available
    #print(quantity_available)

    # Capture the Book's Description

    product_description = soup.find('div', id='product_description')
    if product_description:
        product_description = product_description.find_next_sibling('p')
        if product_description:
            product_description = product_description.text
        else:
            product_description = "N/A"
    book_details['product_description'] = product_description

    # Capture the Book's Review Rating
    review_rating = soup.find('p', class_= 'star-rating Three')
    if review_rating:
        review_rating_stars = review_rating.find_next_sibling('i')
        if review_rating_stars:
            book_details['review_rating'] = review_rating_stars.text
        else:
            # Handle the case when the sibling element is not found
            book_details['review_rating'] = 'Rating information not available'
    else:
        # Handle the case when the review rating element is not found
        book_details['review_rating'] = 'Rating information not available'

    
    
    #Capture the image URL
    image_url = soup.find('img')
    book_details['image_url'] = image_url

    """#Create CSV file
    category_name = "Poetry"
    file_path = category_name + ".csv"
    
    #CSV Header
    with open(file_path, "a", newline='') as header:
        writer = csv.writer(header, delimiter=',')
        if header.tell() == 0:
            writer.writerow(book_details.keys())
    header.close()"""
    #CSV A Light in the Attic Row
    with open("Poetry_2.csv", "a", newline='') as book_details_file:
        writer = csv.writer(book_details_file, delimiter=',')
        if book_details_file.tell() == 0:
            writer.writerow(book_details.keys())
        writer.writerow(list(book_details.values())) 
        print(book_details)
        """
        #Code to create new line for each dictionary item. 
        for value in book_details.values():
            writer.writerow([value])"""
    book_details_file.close()


