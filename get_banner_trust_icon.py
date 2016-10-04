import cssutils

from bs4 import BeautifulSoup

def get_banner_trust_icon(soup=''):
	"""retrieve banner trust-icon if it is present"""


	banner_trust_icon = ""

	if soup.find("div", {"id" : "lockIcon"}):
		banner_trust_icon = "lock_icon.png"

	elif soup.find("i", {"class" : "fa-lock"}):
		banner_trust_icon = "font-awesome class : fa-lock"

	return banner_trust_icon