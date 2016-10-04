import re

from bs4 import BeautifulSoup


def get_body_header1(soup=''):
	"""retrieves header for first main-column content section, if there is one"""

	header = ""

	if soup.find("span", {"class" : "bannerMainTitle"}):

		type1 = soup.find

		ss = soup.find_all("span", {"class": "bannerMainTitle"})

		for sp in ss:
			print len(sp)

			if len(sp) == 0:
				header = "TYPE 1 : " + soup.find("span", {"class": "bannerMainContent"}).contents[0].strip()

			else:
				header = "TYPE 2 : " + soup.find("div", {"class": "main_body"}).h3.contents[0].strip()

	elif soup.find_all("div", {"class" : "bannerbox"}):

		paragraphs = soup.find("div", {"class" : "bannerbox"}).find_all("p")

		strong = soup.find("div", {"class" : "bannerbox"}).find_all("strong")
		if len(strong) > 0:
			header = "TYPE 3 : " + strong[0].contents[0].strip()

		else:
			header = "TYPE 4 : " + paragraphs[0].contents[0].strip()

	elif soup.find("div", {"id": "introtext-rmm"}):
		# header = soup.find("div", {"id": "introtext-rmm"}).h2.contents[0].strip()
		header = "TYPE 5"

	elif soup.find("div", {"id": "introtext"}):
		# header = soup.find("div", {"id": "introtext"}).h2.contents[0].strip()
		header = "TYPE 6"

	elif soup.find("div", {"class" : "background-sun"}):
		# header = soup.find("div", {"class" : "background-sun"}).h1.strong.contents[0].strip()
		header = "TYPE 7"

	elif soup.find("h1", {"id": "headlineText"}):
		# header = soup.find("h1", {"id": "headlineText"}).span.contents[0].strip()
		header = "TYPE 8"

	elif soup.find("img", {"src" : re.compile("en-gfi-max-remote-device-management.jpg") }):
		# this page has the required text as part of an image
		# header = "Manage and Monitor all devices remotely"
		header = "TYPE 9"

	elif soup.title.contents[0] == "Here's your free MAX Backup Playbook":
		# header = soup.find("h1").contents[0].strip().split(".")[0]
		header = "TYPE 10"

	elif soup.find("div", {"id": "heroContent"}):
		# header = soup.find("div", {"id": "heroContent"}).h1.contents[0].strip()
		header = "TYPE 11"

	elif soup.title.contents[0] == "The Perpetually Valuable MSP":
		# header = soup.find("h1").contents[0].strip().split(":")[0]
		header = "TYPE 12"

	else:
		header = "header not found"

	return header
