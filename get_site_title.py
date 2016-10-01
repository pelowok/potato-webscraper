from bs4 import BeautifulSoup


def get_site_title(soup=''):
	"""retrieves the hero image form the various divs and sections in url.p"""
	str_title = soup.title.encode('utf-8')
	return str_title;
