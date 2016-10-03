import re

from bs4 import BeautifulSoup


def get_content_subtitle(soup=''):
	"""retrieves subtitle in hero section, if there is one"""

	content_subtitle = ""

	if soup.find("h1", {"class" : "ppc_header_content_subtitle"}):
		content_subtitle = soup.find("h1", {"class" : "ppc_header_content_subtitle"}).contents[0].strip()

	elif soup.find("img", {"src": re.compile("en-gfi-max-remote-device-management.jpg")}):
		# this page has the required text as part of an image
		content_subtitle = "One Single Dashboard: for all technical tasks across all customer sites and devices"

	elif soup.find("img", {"src": re.compile("hubspot_ppc-banners_mobile_text.jpg")}):
		# this page has the required text as part of an image
		content_subtitle = "Management on the move - laptop, mobile and tablet"

	elif soup.find("h1", {"class" : "ppc_header_title"}):
		content_subtitle = soup.find("h1", {"class" : "ppc_header_title"}).contents[0].strip()
		# Note that this page type uses only a subtitle and no title, due to phrase length.

	elif soup.find("span", {"class" : "bannerMainTitle"}):
		content_subtitle = soup.find("span", {"class" : "bannerMainContent"}).contents[0].strip()

	elif soup.find("div", {"class" : "textOverImgTop"}):
		content_subtitle = soup.find("div", {"class" : "textOverImgTop"}).contents[0].strip()

	elif soup.find("div", {"id": "introtext-rmm"}):
		ctlist = soup.find("div", {"id": "introtext-rmm"}).h4.contents
		for ct in ctlist:
			content_subtitle += ct.encode('utf-8')

	elif soup.find("div", {"id": "introtext"}):
		ctlist = soup.find("div", {"id": "introtext"}).h4.contents
		for ct in ctlist:
			content_subtitle += ct.encode('utf-8')

	elif soup.find("div", {"class" : "background-sun"}):
		content_subtitle = soup.find("div", {"class" : "background-sun"}).h2.contents[0].strip()

	elif soup.find("h1", {"id": "headlineText"}):
		content_subtitle = soup.find("h1", {"id": "headlineText"}).small.contents[0].strip()

	elif soup.title.contents[0] == "Here's your free MAX Backup Playbook":
		content_subtitle = soup.find("h1").contents[0].strip().split(".")[1]

	elif soup.find("div", {"id": "heroContent"}):
		content_subtitle = soup.find("div", {"id": "heroContent"}).h1.span.contents[0].strip()

	elif soup.title.contents[0] == "The Perpetually Valuable MSP":
		content_subtitle = soup.find("h1").contents[0].strip().split(":")[1]

	else:
		content_subtitle = "content_subtitle not found"



	return content_subtitle