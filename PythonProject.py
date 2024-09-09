#Import Libaries
import pandas
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

#Access Books to Scrape Web Page
books_to_scrape_url = "https://books.toscrape.com/"
books_to_scrape_url_response = get(books_to_scrape_url)
#print(books_to_scrape_url_response.content)

#Access Books to Scrape A Light in the Attic Book Web Page
books_to_scrape_a_light_in_the_attic_url = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
books_to_scrape_a_light_in_the_attic_url_response = get(books_to_scrape_a_light_in_the_attic_url)

#A Light in the Attic Parsed HTML
page = get(books_to_scrape_a_light_in_the_attic_url)
soup = BeautifulSoup(page.content, 'html.parser')
#print(soup)

# Get the Book Details

# Catputre the Book's Product Page URL
product_page_url = books_to_scrape_a_light_in_the_attic_url
print(product_page_url)

# Catputre the Book's Universal Product Code
universal_product_code = soup.find('th',string='UPC').find_next('td').get_text()  
print(universal_product_code)

# Catputre the Book's Title
book_title = soup.h1.string
print(book_title)

# Catputre the Book Price, including tax
price_including_tax = soup.find('th', string='Price (incl. tax)').find_next('td').get_text()
print(price_including_tax)

# Catputre the Book Price, excluding tax
price_excluding_tax = soup.find('th', string='Price (excl. tax)').find_next('td').get_text()
print(price_excluding_tax)

# Capature the Number of Books Available
quantity_available = soup.find('th', string='Availability').find_next('td').get_text()
#print(quantity_available)

# Capture the Book's Description

product_descriptions = soup.find_all('p', id='product_description')
for product_description in product_descriptions:
    print(product_description)

"""# Capture the Book's Category
book_categories = soup.find_all('a')
if book_categories:
    category = book_categories[-1].text
    #print(book_categories[-1].text)
    print(category)



    




"""
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
