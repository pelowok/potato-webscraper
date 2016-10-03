from bs4 import BeautifulSoup


def get_content_title(soup=''):
	"""retrieves title in hero section, if there is one"""

	title = []
	t = []

	if soup.find_all("div", {"id" : "introtext-rmm"}):
		t = soup.find("h2", {"class": "white"}).contents
		title = t[0]
	elif soup.find_all("div", {"id": "introtext"}):
		t = soup.find("h2", {"class": "white"}).contents
		title = t[0].strip()
	elif soup.find_all("div", {"class" : "bannerbox"}):
		if soup.find("div", {"class", "textOverImgTop"}):
			t = soup.find("div", {"class": "textOverImgTop"}).contents
		elif soup.find("div", {"class" : "bannerbox"}).p.strong:
			pset = soup.find("div", {"class": "bannerbox"})
			t = pset.find_all('p')[0].strong.contents
		else:
			t = "BANNERBOX ERROR : TRY AGAIN"

		title = t[0]

	elif soup.find_all("span", {"class" : "bannerMainTitle"}):
		# print soup.find_all("span", {"class" : "bannerMainTitle"})
		t = soup.find("span", {"class" : "bannerMainTitle"}).contents
		try:
			title = t[0]
		except:
			print "content_title not found"
	else:
		title = "Content title not found;"

	# print title

	return title