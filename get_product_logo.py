from bs4 import BeautifulSoup


def get_product_logo(soup=''):
	"""retrieves product logo from html - helps to determine product name"""

	logo = []

	if soup.find("div", {"class" : "logo"}):
		logo = soup.find("div", {"class" : "logo"}).find("img")['src']
	elif soup.find("div", {"id" : "logo"}):
		logo = soup.find("div", {"id": "logo"}).find("img")['src']
	elif soup.find("div", {"id": "identity"}):
		logo = soup.find("div", {"id": "identity"}).find("img")['src']
	elif soup.find("a", {"title": "MAXfocus"}):
		logo = soup.find("a", {"title": "MAXfocus"}).find("img")['src']
	elif soup.find("img", {"title": "MaxBackup-Logo.png"}):
		logo = soup.find("img", {"title": "MaxBackup-Logo.png"})['src']
	elif soup.find("img", {"title": "GFI MAX"}):
		logo = soup.find("img", {"title": "GFI MAX"})['src']
	else:
		print "product_logo not found"

	# remove the cache-busting from end of URLs
	logo = logo.split("?")[0]

	return logo