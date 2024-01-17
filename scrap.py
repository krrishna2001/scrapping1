import requests
from bs4 import BeautifulSoup
import csv

def scrape_google_links(query, num_results=10):
    url = f'https://www.google.com/search?q={query}&num={num_results}'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        links = []

        for result in soup.select('.tF2Cxc'):
            link = result.find('a')['href']
            links.append(link)

        return links
    else:
        print(f"Failed to retrieve search results. Status code: {response.status_code}")
        return None

def save_to_csv(links, filename='search_links.csv'):
    fields = ['Links']

    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(fields)

        for link in links:
            writer.writerow([link])

if __name__ == '__main__':
    search_query = input("Enter the search query: ")
    num_results_to_scrape = int(input("Enter the number of results to scrape: "))

    search_links = scrape_google_links(search_query, num_results=num_results_to_scrape)

    if search_links:
        save_to_csv(search_links)
        print(f"Search result links saved to 'search_links.csv'")
