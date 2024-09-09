#Import Libaries
import pandas
from bs4 import BeautifulSoup
from requests import get

#Access Books to Scrape A Light in the Attic Book Web Page
books_to_scrape_a_light_in_the_attic_url = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
books_to_scrape_a_light_in_the_attic_url_response = get(books_to_scrape_a_light_in_the_attic_url)

#A Light in the Attic Parsed HTML
page = get(books_to_scrape_a_light_in_the_attic_url)
soup = BeautifulSoup(page.content, 'html.parser')
print(soup)

# Capture the Book's Category
#<a href="../category/books/poetry_23/index.html">Poetry</a>
book_category = soup.find_all('a')
category = book_category[(len(book_category)-1)]
print(category)