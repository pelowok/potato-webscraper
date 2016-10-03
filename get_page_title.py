from bs4 import BeautifulSoup


def get_page_title(soup=''):
	"""retrieves the page title, if there is one"""
	str_title = soup.title

	if str_title:
		str_title = str_title.encode('utf-8')
	else:
		str_title = []
		print "No page title found."

	return str_title;
