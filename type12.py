import re

from bs4 import BeautifulSoup
from get_product_name import get_product_name
from get_page_language import get_page_language
from get_page_title import get_page_title


def type12(site_url='', soup='', arr=[]):
	"""scrape type 1 templates and return arr for data push to workbook"""

	# marketo_template
	marketo_template = "HANNEMAN"
	arr.append(marketo_template)

	# site_url
	arr.append(site_url.encode('utf-8'))

	# product_name
	logo = soup.find("div", {"id": "identity"}).find("img")['src']
	if soup.find("div", {"id" : "rmm-title"}):
		logo = soup.find("div", {"id": "rmm-title"}).find("img")['src']
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

	# content_title
	titlediv = soup.find("div", {"class": "background-sun"})
	children = titlediv.findChildren()
	content_title = children[0].text
	arr.append(content_title)

	# content_subtitle
	content_subtitle = children[2].text
	arr.append(content_subtitle)
	#
	# body_content1
	body_content = soup.find_all("div", {"class" : "background-midnight"})
	body_content1 = body_content[0].encode('utf-8')
	arr.append(body_content1)

	# body_content2
	body_content = soup.find_all("div", {"class": "background-white"})
	body_content2 = body_content[0].encode('utf-8')
	arr.append(body_content2)

	# body_content3
	body_content3 = ""
	arr.append(body_content3)

	# body_content4
	body_content4 = ""
	arr.append(body_content4)

	# awards_image
	awards_image = ""
	arr.append(awards_image)

	# whitepaper_url
	whitepaper_url = ""
	arr.append(whitepaper_url)

	# video_url
	video_url = ""
	arr.append(video_url)

	# testimonial_image1
	testimonial_image1 = ""
	arr.append(testimonial_image1)

	# testimonial_quote1
	testimonial_quote1 = ""
	arr.append(testimonial_quote1)

	# testimonial_nametag1
	testimonial_nametag1 = ""
	arr.append(testimonial_nametag1)

	# testimonial_image2
	testimonial_image2 = ""
	arr.append(testimonial_image2)

	# testimonial_quote2
	testimonial_quote2 = ""
	arr.append(testimonial_quote2)

	# testimonial_nametag2
	testimonial_nametag2 = ""
	arr.append(testimonial_nametag2)

	# form_header
	form_header = soup.find("a", {"id": "button-secondary"}).text
	arr.append(form_header)

	# custom_body_html
	custom_body_html = ""
	arr.append(custom_body_html)

	return arr
