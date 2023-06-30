from bs4 import BeautifulSoup
import requests
import lxml
import pandas as pd

url = 'https://futurology.life/101-most-innovative-cambridge-based-artificial-intelligence-companies/'
html = requests.get(url).content

soup = BeautifulSoup(html, "lxml")

companies = soup.find_all('div', {'class':'wp-block-cover alignwide has-black-background-color has-background-dim is-position-center-center'})

names = []
websites = []
linkedin= []
crunchbase = []
twitter = []
description = []
facebook = []
for company in companies:
    names.append(company.find('h3').text)
    websites.append(company.find_all('a')[1]['href'])
    linkedin.append(company.find_all('a')[-1]['href'])
    crunchbase.append(company.find_all('a')[0]['href'])
    twitter.append(company.find_all('a')[2]['href'])
    description.append(company.find_all('p')[1].text)

df = pd.DataFrame(
    {
        'Name of the company': names,
        'Website Link': websites,
        'LinkedIn link': linkedin,
        'Crunchbase Link': crunchbase,
        'Twitter Link': twitter,
        'Brief Description': description
    }
    
)

df.to_csv('AI_Companies.csv', index=False)

# https://docs.google.com/spreadsheets/d/1qp-QwGS1y7oXX316ZrdeH20f53ytJq45q-4_zpnlrrI/edit?usp=sharing