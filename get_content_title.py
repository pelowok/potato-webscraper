import re

from bs4 import BeautifulSoup


def get_content_title(soup=''):
	"""retrieves title in hero section, if there is one"""

	content_title = ""

	if soup.find("h1", {"class" : "ppc_header_content_title"}):
		content_title = soup.find("h1", {"class" : "ppc_header_content_title"}).contents[0].strip()

	elif soup.find("h1", {"class" : "ppc_header_title"}):
		# content_title = soup.find("h1", {"class" : "ppc_header_title"}).contents[0].strip()
		# This page type has no text that fits as a page title.
		# Instead, the title is very long. It is used in the content_subtitle spot
		content_title = ""

	elif soup.find("span", {"class" : "bannerMainTitle"}):
		content_title = soup.find("span", {"class" : "bannerMainTitle"}).contents[0].strip()

	elif soup.find("div", {"class" : "textOverImgBottom"}):
		content_title = soup.find("div", {"class" : "textOverImgBottom"}).contents[0].strip()

	elif soup.find("div", {"id": "introtext-rmm"}):
		content_title = soup.find("div", {"id": "introtext-rmm"}).h2.contents[0].strip()

	elif soup.find("div", {"id": "introtext"}):
		content_title = soup.find("div", {"id": "introtext"}).h2.contents[0].strip()

	elif soup.find("div", {"class" : "background-sun"}):
		content_title = soup.find("div", {"class" : "background-sun"}).h1.strong.contents[0].strip()

	elif soup.find("h1", {"id": "headlineText"}):
		content_title = soup.find("h1", {"id": "headlineText"}).span.contents[0].strip()

	elif soup.find("img", {"src" : re.compile("en-gfi-max-remote-device-management.jpg") }):
		# this page has the required text as part of an image
		content_title = "Manage and Monitor all devices remotely"

	elif soup.title.contents[0] == "Here's your free MAX Backup Playbook":
		content_title = soup.find("h1").contents[0].strip().split(".")[0]

	elif soup.find("div", {"id": "heroContent"}):
		content_title = soup.find("div", {"id": "heroContent"}).h1.contents[0].strip()

	elif soup.title.contents[0] == "The Perpetually Valuable MSP":
		content_title = soup.find("h1").contents[0].strip().split(":")[0]

	else:
		content_title = "content_title not found"

	return content_title