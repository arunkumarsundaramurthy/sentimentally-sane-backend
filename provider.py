import sqlite3
import os

DB_NAME = 'save_the_hacker.db'

def fetch(sentiment):
	conn = sqlite3.connect(DB_NAME)
	c = conn.cursor()
	data = c.execute("select title, url, description, url_to_image from articles where sentiment = (?)", (sentiment, )).fetchall()
	output = []
	for row in data:
		output.append({'title': row[0], 'url': row[1], 'description': row[2], 'image_url': row[3]})
	return output