from bs4 import BeautifulSoup


def get_head_image(soup=''):
	"""retrieves image in header, if there is one"""

	if soup.find("section", {"id": "hero-rmm"}):
		tag = soup.find("section", {"id": "hero-rmm"})['data-image-src']
		print tag
	elif soup.find("div", {"id": "theImage"}):
		tag = soup.find("div", {"id": "theImage"})
	else:
		tag = "potato"

	return tag
