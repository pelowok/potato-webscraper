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

		if soup.find("div", {"class", "textOverImgBottom"}):
			t = soup.find("div", {"class": "textOverImgBottom"}).contents
		elif soup.find("div", {"class" : "bannerbox"}).p.strong:
			pset = soup.find("div", {"class" : "bannerbox"})
			str0 = pset.find_all('p')[0].contents
			str1 = str0[1]
			print str1

			t = [str1]

		else:
			t = "BANNERBOX ERROR : TRY AGAIN"

		title = t[0]

	else:
		title = "Content subtitle not found;"

	return title