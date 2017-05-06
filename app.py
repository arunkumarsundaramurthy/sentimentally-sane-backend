from flask import Flask
from flask import jsonify
import os
import loader
import provider

app = Flask(__name__)

@app.route('/load')
def load():
	loader.load()
	return "200"

@app.route('/articles/<sentiment>')
def articles(sentiment):
	print sentiment
	return jsonify(provider.fetch(sentiment))

if __name__ == '__main__':
    app.run(debug=os.environ.get("DEBUG"),host='0.0.0.0')