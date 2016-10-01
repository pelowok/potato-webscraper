from bs4 import BeautifulSoup


def get_content_subtitle(soup=''):
	"""retrieves title in hero section, if there is one"""

	title = []
	t = []

	if soup.find_all("span", {"class" : "bannerMainContent"}):
		t = soup.find("span", {"class" : "bannerMainContent"}).contents
		title = t[0]
	elif soup.find_all("div", {"id" : "introtext-rmm"}):
		t = soup.find("h4", {"class": "white"}).contents
		title = t[0]
	elif soup.find_all("div", {"id": "introtext"}):
		t = soup.find("h4", {"class": "white"}).contents
		title = t[0].strip()
	elif soup.find_all("div", {"class" : "bannerbox"}):
		t = soup.find("div", {"class": "textOverImgBottom"}).contents
		title = t[0]
		main_title = soup.find("div", {"class": "textOverImgBottom"}).p
	else:
		title = "Content subtitle not found;"

	return title