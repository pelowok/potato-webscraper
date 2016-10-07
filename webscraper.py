import xlwt
import requests

from bs4 import BeautifulSoup
from sorting_hat import sorting_hat
from type01 import type01
from type02 import type02
from type03 import type03
from type04 import type04

# declare vars
i = 0
j = 0
page = []
arr = []
feedback = ""
page_template = "unknown"

# create Excel workbook and wb.sheets
wb = xlwt.Workbook(encoding='utf-8', style_compression=0)
ws1 = wb.add_sheet('URLs', cell_overwrite_ok=True)
ws2 = wb.add_sheet('content', cell_overwrite_ok=True)

# declare xlwt styles for workbook
styleHeader = xlwt.easyxf('font: name Arial, color-index blue, bold on, italic on')
styleError = xlwt.easyxf('font: name Times New Roman, color-index red, bold on')

# Here we initialize the many variables, and assign them a string that reflects
# their token names in Marketo.
marketo_template = '{{my.marketo_template}}'
site_url = '{{my.site_url}}'
product_name = '{{my.product_name}}'
page_language = '{{my.page_language}}'
page_title = '{{my.site_title}}'
product_logo = '{{my.product_logo}}'
content_title = '{{my.content_title}}'
content_subtitle = '{{my.content_subtitle}}'
body_content1 = '{{my.body_content1}}'
body_content2 = '{{my.body_content2}}'
body_content3 = '{{my.body_content3}}'
body_content4 = '{{my.body_content4}}'
awards_image = '{{my.awards_image}}'
whitepaper_url = '{{my.whitepaper_url}}'
video_url = '{{my.video_url}}'
testimonial_image1 = '{{my.testimonial_image1}}'
testimonial_quote1 = '{{my.testimonial_quote1}}'
testimonial_nametag1 = '{{my.testimonial_nametag1}}'
testimonial_image2 = '{{my.testimonial_image2}}'
testimonial_quote2 = '{{my.testimonial_quote2}}'
testimonial_nametag2 = '{{my.testimonial_nametag2}}'
form_header = '{{my.form_header}}'
custom_body_html = '{{my.custom_body_html}}'

# append all the header values into the list "arr"
arr.append(marketo_template)
arr.append(site_url)
arr.append(product_name)
arr.append(page_language)
arr.append(page_title)
arr.append(product_logo)
arr.append(content_title)
arr.append(content_subtitle)
arr.append(body_content1)
arr.append(body_content2)
arr.append(body_content3)
arr.append(body_content4)
arr.append(awards_image)
arr.append(whitepaper_url)
arr.append(video_url)
arr.append(testimonial_image1)
arr.append(testimonial_quote1)
arr.append(testimonial_nametag1)
arr.append(testimonial_image2)
arr.append(testimonial_quote2)
arr.append(testimonial_nametag2)
arr.append(form_header)
arr.append(custom_body_html)

# push the column headers into worksheet
j = 0
for val in arr:
	if val:
		ws2.write(0, j, val, styleHeader)
	else:
		ws2.write(0, j, "")

	j += 1
wb.save('webscrape.xls')

# get the URLs from the external file
with open("txt/url_short.p", "rU") as myfile:
	url_list = myfile.readlines()

# loop through URLs in url_list
for cor, url in enumerate(url_list):

	arr = []
	i += 1

	feedback = str(i) + " : "

	site_url = url.rstrip()
	ws1.write(cor, 0, site_url)

	if site_url.startswith('http:'):
		try:
			page = requests.get(site_url)
			soup = BeautifulSoup(page.text, "html.parser")

			# sort by template
			page_template = sorting_hat(soup)
			if page_template == 4:
				feedback += str(page_template)


			# send soup and [arr] to scrape by type
			# if page_template == 1:
			# 	arr = type01(site_url, soup, arr)
			#
			# if page_template == 2:
			# 	arr = type02(site_url, soup, arr)
			#
			# if page_template == 3:
			# 	arr = type03(site_url, soup, arr)

			if page_template == 4:
				arr = type04(site_url, soup, arr)

			j = 0
			for val in arr:
				if val:
					ws2.write(cor, j, val)
				else:
					ws2.write(cor, j, "")

				j += 1

			wb.save('webscrape.xls')

		except requests.exceptions.RequestException as e:  # This is the correct syntax
			ws1.write(cor, 1, str(e), styleError)
			feedback += str(e)
	elif site_url.startswith("{{IMPORT HEADERS}}"):
		feedback += "skip"
	else:
		ws1.write(cor, 1, "ERROR: URL does not begin with \'http:\'", styleError)
		wb.save('webscrape.xls')
		feedback += "skip"

	print feedback
print "49 looks to be Type_1 not Type_11"