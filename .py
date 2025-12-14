# Extract News Headlines

import requests
from bs4 import BeautifulSoup

def scrape_news(url):
    try:
        # Send HTTP GET request
        response = requests.get(url)
        response.raise_for_status()  # Check for request errors

        # Parse HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Example: Extract all headlines inside <h2> tags (depends on website)
        headlines = soup.find_all('h2')

        if headlines:
            print("\n--- News Headlines ---")
            for idx, headline in enumerate(headlines, start=1):
                print(f"{idx}. {headline.get_text().strip()}")
        else:
            print("No headlines found. The website structure may have changed.")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching the website: {e}")

# --- Main Program ---
url = input("Enter the website URL to scrape: ")
scrape_news(url)
