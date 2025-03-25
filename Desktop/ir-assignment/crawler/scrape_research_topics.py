import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# URL of the research publications page
URL = "https://pureportal.coventry.ac.uk/en/organisations/fbl-school-of-economics-finance-and-accounting/publications/"

# Setup Selenium WebDriver
def init_driver():
    options = Options()
    # options.add_argument("--headless")  # Disable headless mode for debugging
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver

# Function to extract research publications with pagination
def scrape_publications():
    driver = init_driver()
    driver.get(URL)
    
    # Take a screenshot for debugging
    time.sleep(5)  # Allow time for page load
    driver.save_screenshot("page_debug.png")

    publications = []
    
    while True:
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".list-result-item"))
            )
        except:
            print("❌ Failed to load publications. The page structure may have changed.")
            break

        # Find all research publications on the current page
        pub_elements = driver.find_elements(By.CSS_SELECTOR, ".list-result-item")

        for pub in pub_elements:
            try:
                title = pub.find_element(By.CSS_SELECTOR, ".title a").text.strip()
                
                # Handle multiple authors
                authors = [a.text.strip() for a in pub.find_elements(By.CSS_SELECTOR, ".relations.person a")]
                authors_text = ", ".join(authors) if authors else "Unknown"
                
                year = pub.find_element(By.CSS_SELECTOR, ".date").text.strip()
                publication_url = pub.find_element(By.CSS_SELECTOR, ".title a").get_attribute("href")

                # Extract author profile URLs
                author_profiles = [a.get_attribute("href") for a in pub.find_elements(By.CSS_SELECTOR, ".relations.person a")]
                author_profiles_text = ", ".join(author_profiles) if author_profiles else "N/A"
                
                publications.append(f"{title} | {authors_text} | {year} | {publication_url} | {author_profiles_text}")
            except Exception as e:
                print(f"⚠️ Skipping a publication due to error: {e}")
                continue
        
        # Check if a next page exists
        try:
            next_button = driver.find_element(By.LINK_TEXT, "Next")
            next_button.click()
            time.sleep(5)  # Allow time for next page to load
        except:
            print("✅ No more pages to load. Finished scraping.")
            break

    driver.quit()

    # Save results
    with open("publications_data.txt", "w", encoding="utf-8") as file:
        for pub in publications:
            file.write(pub + "\n")

    print(f"✅ Successfully saved {len(publications)} publications to publications_data.txt")

# Run the scraper
scrape_publications()
