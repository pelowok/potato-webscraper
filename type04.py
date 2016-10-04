import re

from bs4 import BeautifulSoup
from get_product_name import get_product_name
from get_page_language import get_page_language
from get_page_title import get_page_title


def type04(site_url='', soup='', arr=[]):
	"""scrape type 4 templates and return arr for data push to workbook"""

	# marketo_template
	marketo_template = "GILFOYLE"
	arr.append(marketo_template)

	# site_url
	arr.append(site_url.encode('utf-8'))

	# product_name
	logo = soup.find("div", {"class": "logo"}).find("img")['src']  # varies
	logo = logo.split("?")[0].split("/")[-1]
	product_name = get_product_name(logo)
	arr.append(product_name)

	# page_language
	page_language = get_page_language(arr[1])
	arr.append(page_language)

	# page_title
	page_title = get_page_title(soup)
	arr.append(page_title)

	# product_logo
	product_logo = logo  # see product_name, above
	arr.append(product_logo)


	return arr
