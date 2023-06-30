## AI Companies Web Scraping

This Python script utilizes the BeautifulSoup library to scrape data from a website that lists Cambridge-based artificial intelligence companies. The extracted information is then stored in a Pandas DataFrame and saved as a CSV file.

### Requirements

Make sure you have the following libraries installed:

- Python (version 3.6 or above)
- pip

To install the required dependencies, run the following command:

```bash
pip install -r requirements.txt
```

This command will install the necessary libraries specified in the `requirements.txt` file.

### Usage

1. Run the script using Python:

```python
python AI_Companies.py
```

2. The script will fetch the HTML content from  the [URL](https://futurology.life/101-most-innovative-cambridge-based-artificial-intelligence-companies/), extract information about AI companies, and save the data to a CSV file named `AI_Companies.csv`.

### Output

The script generates a CSV file named `AI_Companies.csv` that contains the following columns:

- Name of the company: The name of the AI company.
- Website Link: The URL of the company's website.
- LinkedIn link: The URL of the company's LinkedIn page.
- Crunchbase Link: The URL of the company's Crunchbase profile.
- Twitter Link: The URL of the company's Twitter page.
- Brief Description: A brief description of the company.

### Note

Please note that the code assumes the website structure remains the same. If the website structure changes, the script may need to be modified accordingly to extract the data correctly.

Feel free to modify and adapt the code to suit your needs!