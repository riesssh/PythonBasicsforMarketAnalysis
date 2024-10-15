# Books to Scrape Web Scraper

This project is a Python web scraper designed to extract book details from the [Books to Scrape](https://books.toscrape.com/) website. It scrapes data such as book titles, prices, availability, and more, and saves the information in CSV files for each book category. Additionally, the script downloads book cover images and stores them locally.

## Features

- Scrapes book details such as title, price (incl. and excl. tax), availability, category, and description.
- Extracts and saves book cover images.
- Stores the book data in CSV files categorized by book genre.
- Automatically navigates through paginated categories.

## Requirements

- Python 3.x
- Libraries specified in `requirements.txt`

## Installation

1. Clone this repository to your local machine:
   
   git clone https://github.com/your-username/PythonBasicsforMarketAnalysis.git

2.  Navigate to the project directory:

    Copy code
    'cd PythonBasicsforMarketAnalysis

3.  Install the required Python libraries:
  
    Copy code
    'pip install -r requirements.txt

Usage
Run the BooksToScrapeProject.py file:

Copy code
'python BooksToScrapeProject.py

The script will start scraping the Books to Scrape website and save the details in CSV files. The CSV files will be created based on the book categories, and book cover images will be saved with corresponding book titles.

Project Structure

BooksToScrapeProject.py: The main Python file that contains the scraping logic.
requirements.txt: Lists the Python libraries required for the project.
README.md: Provides an overview and instructions for the project.

Data Extracted
For each book, the following information is extracted:
   Product page URL
   Universal product code (UPC)
   Book title
   Price (including tax)
   Price (excluding tax)
   Availability (quantity)
   Product description
   Category
   Review rating
   Image URL (book cover)
