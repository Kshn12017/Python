import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

# Load the input file
input_file = 'Input.xlsx'
df = pd.read_excel(input_file)

# Create a directory to save the articles
if not os.path.exists('articles'):
    os.makedirs('articles')

# Function to extract text from a URL
def extract_text_from_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract the article title
    title_tag = soup.find('h1', class_='entry-title')
    title = title_tag.get_text(strip=True) if title_tag else 'No Title Found'

    # Extract the article text
    article_div = soup.find('div', class_='td-post-content tagdiv-type')
    
    if article_div:
        # Extract text content from the specified tags
        elements = article_div.find_all(['h1', 'p', 'h3', 'ol', 'li', 'ul', 'br'])
        article_text = ''
        for element in elements:
            if element.name == 'br':
                article_text += '\n'
            else:
                article_text += element.get_text(strip=True) + '\n'
    else:
        article_text = 'No Article Text Found'

    return title + '\n' + article_text.strip()

# Extract text for each URL and save to a text file
for index, row in df.iterrows():
    url_id = row['URL_ID']
    url = row['URL']

    try:
        article_text = extract_text_from_url(url)
        with open(f'articles/{url_id}.txt', 'w', encoding='utf-8') as file:
            file.write(article_text)
    except Exception as e:
        print(f"Failed to extract {url}: {e}")

print("Article extraction completed.")