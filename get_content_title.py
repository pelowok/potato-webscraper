from bs4 import BeautifulSoup


def get_content_title(soup=''):
	"""retrieves title in hero section, if there is one"""

	title = []
	t = []

	if soup.find_all("span", {"class" : "bannerMainTitle"}):
		t = soup.find("span", {"class" : "bannerMainTitle"}).contents
		title = t[0]
	elif soup.find_all("div", {"id" : "introtext-rmm"}):
		t = soup.find("h2", {"class": "white"}).contents
		title = t[0]
	elif soup.find_all("div", {"id": "introtext"}):
		t = soup.find("h2", {"class": "white"}).contents
		title = t[0].strip()
	elif soup.find_all("div", {"class" : "bannerbox"}):
		t = soup.find("div", {"class": "textOverImgTop"}).contents
		title = t[0]
	else:
		title = "not found"

	print title

	return title