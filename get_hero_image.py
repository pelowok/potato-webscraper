from bs4 import BeautifulSoup


def get_hero_image(soup=''):
	"""retrieves image in hero section, if there is one"""

	tag = []
	tag0 = []
	tag1 = []
	tag2 = []

	if soup.find_all("div", {"id" : "theImage"}):
		tag0 = soup.find("div", {"id" : "theImage"}).find("img")['src']
	elif soup.find("section", {"id": "hero-rmm"}):
		tag0 = soup.find("section", {"id": "hero-rmm"})['data-image-src']
	elif soup.find("section", {"id": "hero-general"}):
		tag0 = soup.find("section", {"id": "hero-general"})['data-image-src']
	elif soup.find("div", {"class": "bannerbox"}):
		tag_img = soup.find_all("div", {"class": "bannerbox"})[0].find_all("img")
		tag1 = tag_img[0]["src"]
		tag2 = tag_img[1]["src"]
	else:
		tag0 = "not found"

	tag = [tag0, tag1, tag2]

	return tag
