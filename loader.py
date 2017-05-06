import requests
import sqlite3
import os

API_KEY = os.environ.get("TWINWORD_API")
TWINWORD_URL = 'https://www.twinword.com/api/v4/sentiment/analyze/'
DB_NAME = 'save_the_hacker.db'

def load():
	conn = sqlite3.connect(DB_NAME)
	c = conn.cursor()
	c.execute('''create table if not exists articles (source varchar(40), url varchar(200),
	 date varchar(40), url_to_image varchar(200), title text, description text,
	  content text, twinword_response text, sentiment varchar(15))''')

	sources = {"Times Of India": "the-times-of-india", "The Hindu": "the-hindu"}

	for source_text, source_key in sources.iteritems():
		url = "https://newsapi.org/v1/articles?source=" + source_key + "&sortBy=latest&apiKey=" + API_KEY
		r = requests.get(url)
		if r.status_code == 200:
			data = r.json()
			for article in data['articles']:
				print article['title']
				if not c.execute("select title from articles where title = (?)", (article['title'], )).fetchone():
					twinword_response = requests.post(TWINWORD_URL, data = {'text': article['title'] + " " + article['description']})
					c.execute("INSERT INTO articles (source, url, date, url_to_image, title, description, twinword_response, sentiment) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (source_text, article['url'], article['publishedAt'], article['urlToImage'], article['title'], article['description'], twinword_response.text, twinword_response.json()['type']))

	conn.commit()
	conn.close()