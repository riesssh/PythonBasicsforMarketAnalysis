# Create Book Details Dictionary
book_details = {
    "product_page_url":"https://books.toscrape.com/" , 
    "universal_product_code" :"a897fe39b1053632", 
    "book_title" :"A Light in the Attic", 
    "price_including_tax" : 51.77, 
    "price_excluding_tax" :51.77, 
    "quantity_available" : 22, 
    "product_description" :"It's hard to imagine a world without A Light in the Attic. This now-classic collection of poetry and drawings from Shel Silverstein celebrates its 20th anniversary with this special edition. Silverstein's humorous and creative verse can amuse the dowdiest of readers. Lemon-faced adults and fidgety kids sit still and read these rhythmic words and laugh and smile and love th It's hard to imagine a world without A Light in the Attic. This now-classic collection of poetry and drawings from Shel Silverstein celebrates its 20th anniversary with this special edition. Silverstein's humorous and creative verse can amuse the dowdiest of readers. Lemon-faced adults and fidgety kids sit still and read these rhythmic words and laugh and smile and love that Silverstein. Need proof of his genius? RockabyeRockabye baby, in the treetopDon't you know a treetopIs no safe place to rock?And who put you up there,And your cradle, too?Baby, I think someone down here'sGot it in for you. Shel, you never sounded so good. ...more", 
    "category" :"Books", 
    "review_rating" : "Not Rate", 
    "image_url" : "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
}

#Extract Information
book_details = [product_page_url, universal_product_code, book_title, price_including_tax, price_excluding_tax, quantity_available, product_description, category, review_rating, image_url]
 
#print Book Details
print (book_details.keys())