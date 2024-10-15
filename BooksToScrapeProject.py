#Import Libaries

from bs4 import BeautifulSoup
import requests
import csv
import urllib.parse




#Books to Scrape Web Pages
books_to_scrape_url = "https://books.toscrape.com/"
#book_category_url = "https://books.toscrape.com/catalogue/category/books/food-and-drink_33/index.html"
#book_url = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"


def get_book_details(book_url,):
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
    #Access to Individual Book Web Page
    #print (book_url)
    books_to_scrape_book_url = book_url
    #print('book url',book_url)
    #print(books_to_scrape_book_url)
    books_to_scrape_book_url_response = requests.get(books_to_scrape_book_url)
    

    #  Book Parsed HTML
    book_soup = BeautifulSoup(books_to_scrape_book_url_response.content, 'html.parser')
    #print(soup)

    # Get the Book Details

    # Catputre the Book's Product Page URL
    product_page_url = books_to_scrape_book_url
    book_details['product_page_url'] = product_page_url
    #print(product_page_url)

    # Catputre the Book's Universal Product Code
    universal_product_code = book_soup.find('th',string='UPC')
    if universal_product_code:
        universal_product_code = universal_product_code.find_next('td').get_text()
    else:
        universal_product_code = 'N/A'  
    book_details['universal_product_code'] = universal_product_code
    #print(universal_product_code)

    # Catputre the Book's Title
    book_title = book_soup.h1.string
    book_details['book_title'] = book_title
    #print()
    #print("Book Title:  ",book_title)

    # Catputre the Book Price, including tax
    price_including_tax = book_soup.find('th', string='Price (incl. tax)')
    if price_including_tax:
        price_including_tax = price_including_tax.find_next('td').get_text()
    else:
        price_including_tax = 'N/A'
    book_details['price_including_tax'] = price_including_tax
    #print(price_including_tax)

    # Catputre the Book Price, excluding tax
    price_excluding_tax = book_soup.find('th', string='Price (excl. tax)')
    if price_excluding_tax:
        price_excluding_tax = price_excluding_tax.find_next('td').get_text()
    else:
        price_excluding_tax = 'N/A'
    book_details['price_excluding_tax'] = price_excluding_tax
    #print(price_excluding_tax)

    # Capature the Number of Books Available
    quantity_available = book_soup.find('th', string='Availability')
    if quantity_available:
        quantity_available = quantity_available.find_next('td').get_text()
    else:
        quantity_available = 'N/A'
    book_details['quantity_available'] = quantity_available
    #print(quantity_available)

    # Capture the Books Category
    #print('catpture book category:', book_url)
    category_tag= book_soup.find_all('a', href=True)
    #print ('href', category_tag )
    last_category_tag = category_tag[3]
    #print('last_category_tag',last_category_tag)
    # Extract the category from the text of the <a> tag
    category = last_category_tag.get_text()
    #if not category:
    #       category = 'N/A'
    book_details['category'] = category
    
    #print('Category:', category)
  
    # Capture the Book's Description

    product_description = book_soup.find('div', id='product_description')
    if product_description:
        product_description = product_description.find_next_sibling('p')
        if product_description:
            product_description = product_description.text
        else:
            product_description = "N/A"
    book_details['product_description'] = product_description

    # Capture the Book's Review Rating
    review_rating = book_soup.find('p', class_= 'star-rating Three')
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
    image_url = book_soup.find('img')['src']
    image_url = image_url.replace('../../',books_to_scrape_url)
    book_details['image_url'] = image_url
    
    try:
        actual_url_image = requests.get(image_url)
        no_spaces_title = book_title.strip()
        no_spaces_title = no_spaces_title.replace(':','').replace('#','').replace('/','').replace('\\','').replace('\'','').replace('\"','').replace('?','').replace('.','').replace('*','')
        #print ("jpg file name:  ", no_spaces_title)
        save_file = no_spaces_title +".jpg"
        if save_file == 'At The Existentialist Café Freedom, Being, and apricot cocktails with Jean-Paul Sartre, Simone de Beauvoir, Albert Camus, Martin Heidegger, Edmund Husserl, Karl Jaspers, Maurice Merleau-Ponty and others.jpg':
            save_file = 'AtTheExistentialistCafeFreedom.jpg'
        #print('save file:  ', save_file)

        with open(save_file, 'wb') as file:
            file.write(actual_url_image.content)
    except Exception as jpgerr:
        print()
        print("***Error-Unable to Save File***:  ", str(jpgerr))

    #print('Saved', save_file)
    
      
    #CSV File
    try:
        save_category_books_file = category +".csv"
        #print(save_category_books_file)
        with open(save_category_books_file, "a", newline='',encoding='utf-8') as book_details_file:
            writer = csv.writer(book_details_file, delimiter=',')
            if book_details_file.tell() == 0:
                writer.writerow(book_details.keys())
            writer.writerow(list(book_details.values())) 
            #print ("file saved",save_category_books_file)
    except Exception as err:
        print("CSV Error:  ", str(err))
       
    book_details_file.close()

def get_book_urls(book_category_url):
    book_category_url_response = requests.get(book_category_url)
    
    #  Book Parsed HTML
    category_soup = BeautifulSoup(book_category_url_response.content, 'html.parser')

    # Get Number of Pages for A category
    try:
        total_pages = int(category_soup.find('li', class_='current').text.strip().split()[-1])
    except AttributeError: #when total pages is not found
        total_pages = 1 
    #print('total page count:  ',total_pages)

    # Declare Books URLs Array
    book_urls = []

    for page in range(1, total_pages + 1):
        if total_pages > 1:
        # Get URL for each page
            page_url = book_category_url.replace('index.html', f'page-{page}.html')
            #print ('page url:  ',page_url)
        else:
            page_url = book_category_url
        page_response = requests.get(page_url)
        #print (page_response)
        page_soup = BeautifulSoup(page_response.content, 'html.parser')

        # Get the Book URLs
        book_link_urls = page_soup.find_all('a', title=True)
        # Iterate through each book extracting the URLs
        
        for book_link in book_link_urls:
            relative_book_url = book_link['href']
            relative_book_url = relative_book_url.replace('../../../', '') 
            full_book_url = urllib.parse.urljoin(books_to_scrape_url, "catalogue/") 
            full_book_url = urllib.parse.urljoin(full_book_url, relative_book_url)
            book_urls.append(full_book_url)
            #print(book_url)
    return book_urls

def get_book_category_urls(book_to_scrape_url):
    book_to_scrape_url_response = requests.get(book_to_scrape_url)
    
    #  Book Parsed HTML
    book_to_scrape_soup = BeautifulSoup(book_to_scrape_url_response.content, 'html.parser')

    # Create Category URLs Dictionary
    book_category_urls = []

    #Get the Book Category URLs
    left_side_bar = book_to_scrape_soup.find('div', class_= 'side_categories')
    #book_category_link_urls = left_side_bar.find_all('li', class_= '::marker')
    book_category_link_urls = left_side_bar.find_all('a') 
    #print(book_category_link_urls)
    for book_category_link_url in book_category_link_urls:
        #print('')
        #print ('entered the loop')
        #category_url = book_to_scrape_url + book_category_link_url['href']
        category_url = urllib.parse.urljoin(book_to_scrape_url, book_category_link_url['href'])
        book_category_urls
        
        #print('category_url:  ', category_url)
        if 'books_1' not in category_url:
            book_category_urls.append(category_url)
            
            
            #print('category url added',category_url)
            #print('')
            #print (book_category_link_url)
    return book_category_urls


# Main Program
book_category_urls = get_book_category_urls (books_to_scrape_url)

#Listing of Categories
#categories = []

for book_category_url in book_category_urls:
    #print("Book Category Url:",book_category_url)
    category_url = urllib.parse.urlparse(book_category_url).path
    #print(category_url)
    book_urls = get_book_urls (book_category_url)
    #print('book category url',book_category_url)
    for book_url in book_urls:
        get_book_details(book_url)
        #print ("Catagory" , category)
        #print ('book url', book_url)

    #Extract the category from the book URL
    category = book_category_url