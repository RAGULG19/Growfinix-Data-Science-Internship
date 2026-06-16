import pandas as pd
from bs4 import BeautifulSoup

# 1. Simulated Public Real Estate Webpage HTML (Target Data)
html_content = """
<html>
    <body>
        <div class="property-card">
            <h2 class="title">3 BHK Luxury Apartment</h2>
            <span class="location">Adyar, Chennai</span>
            <div class="price">1.80 Crores</div>
        </div>
        <div class="property-card">
            <h2 class="title">2 BHK Semi-Furnished Flat</h2>
            <span class="location">Velachery, Chennai</span>
            <div class="price">85 Lakhs</div>
        </div>
        <div class="property-card">
            <h2 class="title">1 BHK Studio Apartment</h2>
            <span class="location">OMR, Chennai</span>
            <div class="price">45 Lakhs</div>
        </div>
        <div class="property-card">
            <h2 class="title">4 BHK Independent Villa</h2>
            <span class="location">Tambaram, Chennai</span>
            <div class="price">2.50 Crores</div>
        </div>
    </body>
</html>
"""

# 2. Initialize BeautifulSoup to Parse HTML
soup = BeautifulSoup(html_content, 'html.parser')
properties_list = []

# 3. Target the HTML/CSS Selectors to extract details
cards = soup.find_all('div', class_='property-card')

for card in cards:
    title = card.find('h2', class_='title').text
    location = card.find('span', class_='location').text
    price = card.find('div', class_='price').text
    
    properties_list.append({
        'Property_Title': title,
        'Location': location,
        'Price_Listed': price
    })

# 4. Clean and Export as a Structured CSV
df = pd.DataFrame(properties_list)
df.to_csv('scraped_properties.csv', index=False)

print("--- SCRAPED DATA FROM HTML ---")
print(df)
print("\nSuccess! Data exported to 'scraped_properties.csv'")