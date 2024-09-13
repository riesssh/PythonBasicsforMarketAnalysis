#Import Libaries
import pandas
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

"""#Access Books to Scrape Web Page
books_to_scrape_url = "https://books.toscrape.com/"
books_to_scrape_url_response = get(books_to_scrape_url)
#print(books_to_scrape_url_response.content)"""

#Access Books to Scrape A Light in the Attic Book Web Page
books_to_scrape_a_light_in_the_attic_url = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
books_to_scrape_a_light_in_the_attic_url_response = get(books_to_scrape_a_light_in_the_attic_url)

# A Light in the Attic Parsed HTML
soup = BeautifulSoup(books_to_scrape_a_light_in_the_attic_url_response.content, 'html.parser')
#print(soup)

# Get the Book Details

# Catputre the Book's Product Page URL
product_page_url = books_to_scrape_a_light_in_the_attic_url
book_details['product_page_url'] = product_page_url
#print(product_page_url)

# Catputre the Book's Universal Product Code
universal_product_code = soup.find('th',string='UPC').find_next('td').get_text()  
book_details['universal_product_code'] = universal_product_code
#print(universal_product_code)

# Catputre the Book's Title
book_title = soup.h1.string
book_details['book_title'] = book_title
#print(book_title)

# Catputre the Book Price, including tax
price_including_tax = soup.find('th', string='Price (incl. tax)').find_next('td').get_text()
book_details['price_including_tax'] = price_including_tax
#print(price_including_tax)

# Catputre the Book Price, excluding tax
price_excluding_tax = soup.find('th', string='Price (excl. tax)').find_next('td').get_text()
book_details['price_excluding_tax'] = price_excluding_tax
#print(price_excluding_tax)

# Capature the Number of Books Available
quantity_available = soup.find('th', string='Availability').find_next('td').get_text()
book_details['quantity_available'] = quantity_available
#print(quantity_available)

# Capture the Book's Description

product_description = soup.find('div', id='product_description')
product_description_contents = product_description.find_next_sibling('p').text
book_details['product_description'] = product_description_contents

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

#Create CSV file
#CSV Header
header = book_details.keys()
#CSV A Light in the Attic Row
with open("ALightInTheAticBookDetails", "w", newline='') as book_details_file:
    writer = csv.writer(book_details_file, delimiter=',')
    writer.writerow(book_details)
#Create CSV file
#CSV Header
header = book_details.keys()
#CSV A Light in the Attic Row
with open("ALightInTheAticBookDetails.csv", "w", newline='') as book_details_file:
    writer = csv.writer(book_details_file, delimiter=',')
    writer.writerow(book_details)
    writer.writerow(list(book_details.values()))
    """
    #Code to create new line for each dictionary item. 
    for value in book_details.values():
        writer.writerow([value])"""
book_details_file.close()






"""#HTML Locations
h2_text = soup.h2.string
h1 = soup.h1.string
#print(h2_text)
print(h1)
"""
"""





#page = get(books_to_scrape_url)
#print(page.content)

#soup = BeautifulSoup(page.content, 'html.parser')
#print(soup)

#Initial variables for A Light in the Attic Page
#book_title = soup.title.string
#print(book_title)



universal_product_code = get(soup.UPC.string)
print(universal_product_code)
    
price_including_tax 
    price_excluding_tax
    quantity_available
    product_description 
    category 
    review_rating 
    image_url"""



#Find all elements with a <a> tag
#books_to_scrape_elements = soup.find_all('a')
#print(books_to_scrape_elements)

#Find all elements with a <th> tag
#book_title_elements = soup.find_all('th')
#print(book_title_elements)




#Authocation Token - Do we need have this for BooktoScrape





#print Book Details
#print (book_details.keys())
#test git hub
