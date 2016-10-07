import re

from bs4 import BeautifulSoup
from get_product_name import get_product_name
from get_page_language import get_page_language
from get_page_title import get_page_title


def type11(site_url='', soup='', arr=[]):
	"""scrape type 1 templates and return arr for data push to workbook"""

	# marketo_template
	marketo_template = "HANNEMAN"
	arr.append(marketo_template)

	# site_url
	arr.append(site_url.encode('utf-8'))

	# product_name
	logo = soup.find("div", {"id": "logo"}).find("img")['src']
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
	content_title = ""
	if soup.find("div", {"id": "introtext-rmm"}):
		content_title = soup.find("div", {"id": "introtext-rmm"}).h2.contents[0].strip()
	if soup.find("div", {"id": "introtext"}):
		content_title = soup.find("div", {"id": "introtext"}).h2.contents[0].strip()
	arr.append(content_title)

	# content_subtitle
	content_subtitle = ""
	if soup.find("div", {"id": "introtext-rmm"}):
		ctlist = soup.find("div", {"id": "introtext-rmm"}).h4.contents
	if soup.find("div", {"id": "introtext"}):
		ctlist = soup.find("div", {"id": "introtext"}).h4.contents
	for ct in ctlist:
		content_subtitle += ct.encode('utf-8')
	arr.append(content_subtitle)

	# body_content1
	body_content = soup.find_all("section", {"id" : "icons"})
	body_content1 = body_content[0].encode('utf-8')
	arr.append(body_content1)

	# body_content2
	body_content = soup.find_all("section", {"id": "features"})
	body_content2 = body_content[0].encode('utf-8')
	arr.append(body_content2)

	# body_content3
	if soup.find("section", {"id": "testimonials"}):
		body_content3 = soup.find("section", {"id": "testimonials"}).encode('utf-8')
	else:
		body_content3 = ""
	arr.append(body_content3)

	# body_content4
	if soup.find("section", {"id": "stats"}):
		body_content4 = soup.find("section", {"id": "stats"}).encode('utf-8')
	else:
		body_content4 = ""
	arr.append(body_content4)

	# awards_image
	awards_image = ""
	if soup.find("section", {"id": "awards"}):
		awards_image = soup.find("section", {"id": "awards"}).encode('utf-8').split('?')[0].split("/")[-1]
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
	form_header = soup.find("div", {"id": "rightcolumn"}).find("h4").text.encode('utf-8')
	form_header = ' '.join(form_header.split())
	form_header = form_header.replace("TageKOSTENLOS", "Tage KOSTENLOS")
	arr.append(form_header)

	# custom_body_html
	custom_body_html = ""
	arr.append(custom_body_html)

	return arr
