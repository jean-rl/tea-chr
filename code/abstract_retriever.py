import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from cleantext import clean
from icecream import ic
from tqdm.auto import tqdm

URL = "https://www.jair.org/index.php/jair/issue/archive"
article_page = requests.get(URL)

archive_parser = BeautifulSoup(article_page.content, "html.parser")
archive_links = []

for link in archive_parser.select('a.title'):
    vol = link.text
    link = link.get('href')
    # split year from the volume eg Vol. 73 (2020)
    year = int(vol[vol.find("(") + 1:vol.find(")")])
    if year >= 2020:
        archive_links.append({'year': year, 'link': link})


papers = list()

for archive in tqdm(archive_links, desc="Archive", position=0, leave=True, unit="archive"):
    article_page = requests.get(archive['link'])
    archive_parser = BeautifulSoup(article_page.content, "html.parser")
    links = archive_parser.select('h3.media-heading a')


    for link in tqdm(links, desc="Papers", position=1, leave=False, unit="paper"):
        # clean the title
        title = clean(text=link.text,
                      lower=True,
                      no_line_breaks=False,
                      no_numbers=False,
                      no_punct=False,
                      lang="en")

        # Get article page
        article_page = requests.get(link.get('href'))
        parser = BeautifulSoup(article_page.content, "html.parser")

        # Get abstract
        abstract = parser.select('div.article-abstract')[0].text

        # Clean the abstract
        abstract = clean(text=abstract,
                            lower=True,
                            no_line_breaks=False,
                            no_numbers=False,
                            no_punct=False,
                            lang="en")

        # Add to found papers
        papers.append({'year': archive['year'], 'title': title, 'link': link.get('href'), 'abstract': abstract})

# Write to a csv file
df = pd.DataFrame(papers)
df.to_csv('jair.csv', index=False)

