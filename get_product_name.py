import re
from bs4 import BeautifulSoup


def get_product_name(soup=''):
	"""deduces the product name from the page content"""

	prod = ""

	backup = soup(text=re.compile('Backup'))
	rm_msp = soup(text=re.compile('MSP'))
	mail = soup(text=re.compile('Mail'))
	ri = soup(text=re.compile('Risk'))
	rm_itpro = soup(text=re.compile('Remote Management IT'))

	if backup:
		prod += "backup "

	if rm_msp:
		prod += "rm_msp "

	if mail:
		prod += "mail "

	if ri:
		prod += "ri "

	if rm_itpro:
		prod += "rm_itpro "

	if len(prod) < 1 :
		prod = "UNKNOWN"
		print "prod : " + prod

	return prod