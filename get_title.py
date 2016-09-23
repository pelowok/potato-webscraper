from bs4 import BeautifulSoup


def get_title(soup=''):
	"""retrieves the hero image form the various divs and sections in url.p"""
	str_title = str(soup.title)
	return str_title;
