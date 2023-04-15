import requests
from bs4 import BeautifulSoup

def scrape_data(url):
    # Send a GET request to the URL and get the HTML response
    response = requests.get(url)

    # Parse the HTML response using Beautiful Soup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract the data you want to scrape
    title = soup.title.string
    description = soup.find('meta', attrs={'name': 'description'})['content']

    # Return the scraped data as a dictionary
    return {
        'title': title,
        'description': description
    }