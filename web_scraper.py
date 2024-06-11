### Web Scraper to CSV ###
'''
DISCLAIMER: check websites' robots.txt file prior to scraping sites to ensure that it is legal to do so.

A simple web scraper to parse glossary terms and their associated definitions into a CSV file.
'''

import requests
from bs4 import BeautifulSoup
import csv

url = "https://example.com/"

def parse_glossary(url):
    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        glossary = []
        terms = soup.find_all("h3")
        for term in terms:
            definition = term.find_next_sibling("p")

            if definition and definition.text.strip():
                glossary.append([term.text.strip(), definition.text.strip()])

        return glossary
    except requests.RequestException as e:
        return str(e)

def save_csv(data, filename):
    with open(filename, "w+", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Term", "Definition"])
        writer.writerows(data)

glossary_data = parse_glossary(url)
if isinstance(glossary_data, list):
    save_csv(glossary_data, "glossary.csv")
    print("Data written to glossary.csv")
else:
    print("Failed to fetch/ parse data:", glossary_data)
