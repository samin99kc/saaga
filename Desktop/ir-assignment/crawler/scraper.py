import time
import requests
from bs4 import BeautifulSoup
from urllib.robotparser import RobotFileParser

# Define the base URL
base_url = "https://pureportal.coventry.ac.uk"
publications_url = base_url + "/en/organisations/fbl-school-of-economics-finance-and-accounting/publications"

# Setup a polite user-agent
headers = {
    "User-Agent": "CovCrawlerBot/1.0 (academic use by student; contact: your-email@example.com)"
}

# Step 1: Check robots.txt
def is_allowed_to_crawl(target_url):
    rp = RobotFileParser()
    rp.set_url(base_url + "/robots.txt")
    rp.read()
    return rp.can_fetch(headers["User-Agent"], target_url)

# Step 2: Crawl and parse only if allowed
def polite_crawl():
    if not is_allowed_to_crawl(publications_url):
        print("🚫 Crawling is not allowed by robots.txt")
        return

    print("✅ Crawling allowed. Starting politely...")

    response = requests.get(publications_url, headers=headers)
    time.sleep(2)  # polite delay
    soup = BeautifulSoup(response.text, "html.parser")

    publications = soup.find_all("h3", class_="title")

    for pub in publications:
        title_tag = pub.find("a")
        if title_tag:
            title = title_tag.text.strip()
            link = title_tag["href"]
            full_link = base_url + link
            print(f"📘 {title}")
            print(f"🔗 {full_link}\n")
        time.sleep(2)  # delay before next publication

# Run the polite crawler
polite_crawl()
