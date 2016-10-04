import re

from bs4 import BeautifulSoup
from get_product_name import get_product_name
from get_page_language import get_page_language
from get_page_title import get_page_title


def type01(site_url='', soup='', arr=[]):
	"""scrape type 1 templates and return arr for data push to workbook"""

	# set some universally needed vars
	divs = soup.find_all('div')
	spans = soup.find_all('span')
	imgs = soup.find_all('img')

	# marketo_template
	marketo_template = "HANNEMAN"
	arr.append(marketo_template)

	# site_url
	arr.append(site_url.encode('utf-8'))

	# product_name
	logo = soup.find("div", {"class": "logo"}).find("img")['src']  # varies
	logo = logo.split("?")[0].split("/")[-1]
	product_name = get_product_name(logo)
	arr.append(product_name)

	# page_language
	page_language = get_page_language(arr[0])
	arr.append(page_language)

	# page_title
	page_title = get_page_title(soup)
	arr.append(page_title)

	# product_logo
	product_logo = logo  # see product_name, above
	arr.append(product_logo)

	# content_title
	if soup.find("h1"):
		content_title = ""  # page has no title
	else:
		content_title = "STICKY SERVICES"  # http://trials.maxfocus.com/en-max-backup uses text in image
	arr.append(content_title)

	# content_subtitle
	if soup.find("h1"):
		content_subtitle = soup.find("h1", {"class": "ppc_header_title"}).contents[0].strip()
	else:
		content_subtitle = "High-value backup and recovery to help you make more money"
	arr.append(content_subtitle)

	# body_content1
	body_content = soup.find_all("div", {"class" : "main_body"})
	body_content1 = body_content[0].encode('utf-8')
	arr.append(body_content1)

	# body_content2
	if soup.find("div", {"class": "lcWhiteBox"}):
		body_content2 = soup.find("div", {"class": "lcWhiteBox"}).contents[0].strip()
	else:
		body_content2 = ""
	arr.append(body_content2)

	# body_content3
	if soup.find("div", {"class": "pointslist"}):
		body_content3 = soup.find("div", {"class": "pointslist"}).encode('utf-8')
	else:
		body_content3 = ""
	arr.append(body_content3)

	# body_content4
	body_content4 = ""
	arr.append(body_content4)

	# awards_image
	awards_image = soup.find("div", {"class" : "awardsImg"}).find("img")["src"].encode('utf-8').split('?')[0].split("/")[-1]
	arr.append(awards_image)

	# whitepaper_url
	vboxs = soup.find_all("div", {"class" : "videoBox"})
	whitepaper_url = vboxs[0].encode('utf-8')
	arr.append(whitepaper_url)

	# video_url
	video_url = vboxs[1].encode('utf-8')
	arr.append(video_url)

	# testimonial_image1
	if soup.find("div", {"class" : "testimonialImg"}):
		testimonial_image1 = soup.find("div", {"class" : "testimonialImg"}).find("img")["src"].encode('utf-8').split('?')[0].split("/")[-1]
	else:
		testimonial_image1 = ""
	arr.append(testimonial_image1)

	# testimonial_quote1
	if soup.find("div", {"class": "testimonialQuote"}):
		testimonial_quote1 = soup.find("div", {"class": "testimonialQuote"}).text.encode('utf-8')
	else:
		testimonial_quote1 = ""
	arr.append(testimonial_quote1)

	# testimonial_nametag1
	if soup.find("div", {"class": "testimonialQuote"}):
		testimonial_nametag1 = soup.find("div", {"class": "testimonialSource"}).text.encode('utf-8')
	else:
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
	custom_body_html = '<script type="text/javascript" src="/jquery.magnific-popup.min.js"></script>'  # video player
	arr.append(custom_body_html)

	return arr
