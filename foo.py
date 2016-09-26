from bs4 import BeautifulSoup
import requests

url = "http://www.mynameiskendra.com"
r = []

try:
	r = requests.get(url)
except requests.exceptions.RequestException as e:  # This is the correct syntax
	print e

if r:
	soup = BeautifulSoup(r.text, "html.parser")

	messages = []

	gridunit = soup.select("div.grid-unit") # selects all .grid-unit's
	for l in gridunit:
		message = {}

	link = l.find("a")
	if link:
		message['link'] = link['href']


	image = l.find('img')
	if image:
		message['image'] = image['src']

	messages.append(message)

	print messages