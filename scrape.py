import json
import os
import subprocess
import requests
from bs4 import BeautifulSoup
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import time

def strip_html(data):
    return BeautifulSoup(data, "html.parser").get_text()

def scrape_data(browser, url):
    browser.visit(url)
    time.sleep(1)
    soup = BeautifulSoup(browser.html, "html.parser")
    return soup

def process_entries(entries, base_url=""):
    data = []
    for entry in entries:
        title_element = entry.find("span", class_="articleTitle")
        pub_date_element = entry.find("span", class_="pubYear")
        pub_info_element = entry.find("span", class_="pubInfo")
        link_element = entry.find("a", href=True)
        
        title = strip_html(title_element.text) if title_element else ""
        pub_date = strip_html(pub_date_element.text) if pub_date_element else ""
        pub_info = strip_html(pub_info_element.text) if pub_info_element else ""
        link = base_url + link_element["href"] if link_element else ""

        authors = [strip_html(name.text) for name in entry.find_all("span", class_="name")]

        data.append({
            "Authors": authors,
            "Title": title,
            "Date": pub_date,
            "Publication": pub_info,
            "Link": link
        })
    return data

def scrape():
    # Use ChromeDriverManager to install the correct ChromeDriver
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)

    # Scrape first site
    url1 = "https://philpapers.org/browse/top-level-ontologies?limit=50&..."
    soup1 = scrape_data(browser, url1)
    philpapers_entries = process_entries(soup1.find_all("span", class_="citation"), base_url="https://philpapers.org")

    # Scrape second site
    url2 = "https://www.scilit.net/articles/search?..."
    soup2 = scrape_data(browser, url2)
    scilit_entries = process_entries(soup2.find_all("div", class_="result"), base_url="https://www.scilit.net")

    # Combine and return the data
    articles = philpapers_entries + scilit_entries
    browser.quit()
    return articles

def save_data_to_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def git_commit_and_push(filename, commit_message):
    try:
        # Add the file, commit, and push to the repository
        subprocess.run(["git", "add", filename], check=True)
        subprocess.run(["git", "commit", "-m", commit_message], check=True)
        subprocess.run(["git", "push"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Failed to push data to repository: {e}")

if __name__ == "__main__":
    scraped_articles = scrape()

    # Define the path to the JSON file
    filename = 'docs/data/data.json'
    save_data_to_json(scraped_articles, filename)

    # Commit and push the updated file to GitHub
    git_commit_and_push(filename, "Update scraped data")

    # Print the results (optional)
    for article in scraped_articles:
        print(article)
