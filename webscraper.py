import xlwt
import requests

from bs4 import BeautifulSoup
from sorting_hat import sorting_hat
from get_product_name import get_product_name
from get_page_language import get_page_language
from get_page_title import get_page_title
from get_product_logo import get_product_logo
from get_content_title import get_content_title
from get_content_subtitle import get_content_subtitle
# from get_banner_trust_icon import get_banner_trust_icon
# from get_banner_trust_text import get_banner_trust_text
from get_body_header1 import get_body_header1
# from get_body_content1 import get_body_content1
# from get_body_header2 import get_body_header2
# from get_body_content2 import get_body_content2
# from get_body_header3 import get_body_header3
# from get_body_content3 import get_body_content3
# from get_body_header4 import get_body_header4
# from get_body_content4 import get_body_content4
# from get_awards_image import get_awards_image
# from get_whitepaper_url import get_whitepaper_url
# from get_column_content1 import get_column_content1
# from get_column_content2 import get_column_content2
# from get_column_content3 import get_column_content3
# from get_testimonial_video1 import get_testimonial_video1
# from get_testimonial_image1 import get_testimonial_image1
# from get_testimonial_quote1 import get_testimonial_quote1
# from get_testimonial_nametag1 import get_testimonial_nametag1
# from get_testimonial_video1 import get_testimonial_video2
# from get_testimonial_image1 import get_testimonial_image2
# from get_testimonial_quote1 import get_testimonial_quote2
# from get_testimonial_nametag1 import get_testimonial_nametag2
# from get_testimonial_nametag1 import get_testimonial_nametag2
# from get_form_header import get_form_header
# from get_custom_body_html import get_custom_body_html

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
site_url = '{{my.site_url}}'
product_name = '{{my.product_name}}'
page_language = '{{my.page_language}}'
page_title = '{{my.site_title}}'
product_logo = '{{my.product_logo}}'
content_title = '{{my.content_title}}'
content_subtitle = '{{my.content_subtitle}}'
# banner_trust_icon = '{{my.banner_trust_icon}}'
# banner_trust_text = '{{my.banner_trust_text}}'
body_header1 = '{{my.body_header1}}'
body_content1 = '{{my.body_content1}}'
body_header2 = '{{my.body_header2}}'
body_content2 = '{{my.body_content2}}'
body_header3 = '{{my.body_header3}}'
body_content3 = '{{my.body_content3}}'
body_header4 = '{{my.body_header4}}'
body_content4 = '{{my.body_content4}}'
awards_image = '{{my.awards_image}}'
whitepaper_url = '{{my.whitepaper_url}}'
column_content1 = '{{my.column_content1}}'
column_content2 = '{{my.column_content2}}'
column_content3 = '{{my.column_content3}}'
testimonial_video1 = '{{my.testimonial_video1}}'
testimonial_image1 = '{{my.testimonial_image1}}'
testimonial_quote1 = '{{my.testimonial_quote1}}'
testimonial_nametag1 = '{{my.testimonial_nametag1}}'
testimonial_video2 = '{{my.testimonial_video2}}'
testimonial_image2 = '{{my.testimonial_image2}}'
testimonial_quote2 = '{{my.testimonial_quote2}}'
testimonial_nametag2 = '{{my.testimonial_nametag2}}'
form_header = '{{my.form_header}}'
custom_body_html = '{{my.custom_body_html}}'

# append all the header values into the list "arr"
arr.append(site_url)
arr.append(product_name)
arr.append(page_language)
arr.append(page_title)
arr.append(product_logo)
arr.append(content_title)
arr.append(content_subtitle)
# arr.append(banner_trust_icon)
# arr.append(banner_trust_text)
arr.append(body_header1)
arr.append(body_content1)
arr.append(body_header2)
arr.append(body_content2)
arr.append(body_header3)
arr.append(body_content3)
arr.append(body_header4)
arr.append(body_content4)
arr.append(awards_image)
arr.append(whitepaper_url)
arr.append(column_content1)
arr.append(column_content2)
arr.append(column_content3)
arr.append(testimonial_video1)
arr.append(testimonial_image1)
arr.append(testimonial_quote1)
arr.append(testimonial_nametag1)
arr.append(testimonial_video2)
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
			feedback += str(page_template)

			# my.site_url
			arr.append(site_url.encode('utf-8'))

			# my.product_name
			product_name = get_product_name(soup)
			arr.append(product_name)

			# my.page_language
			page_language = get_page_language(site_url)
			arr.append(page_language)

			# my.site_title
			page_title = get_page_title(soup)
			arr.append(page_title)  # returns string

			# my.product_logo
			product_logo = get_product_logo(soup)
			arr.append(product_logo)

			# my.content_title
			content_title = get_content_title(soup)
			arr.append(content_title)

			# my.content_subtitle
			content_subtitle = get_content_subtitle(soup)
			arr.append(content_subtitle)

			# # my.banner_trust_icon
			# banner_trust_icon = get_banner_trust_icon(soup)
			# arr.append(banner_trust_icon)
			#
			# # my.banner_trust_text
			# arr.append(banner_trust_text)

			# my.body_header1
			# body_header1 = get_body_header1(soup)
			arr.append(body_header1)
			# feedback += body_header1

			# my.body_content1
			arr.append(body_content1)

			# my.body_header2
			arr.append(body_header2)

			# my.body_content2
			arr.append(body_content2)

			# my.body_header3
			arr.append(body_header3)

			# my.body_content3
			arr.append(body_content3)

			# my.body_header4
			arr.append(body_header4)

			# my.body_content4
			arr.append(body_content4)

			# my.awards_image
			arr.append(awards_image)

			# my.whitepaper_url
			arr.append(whitepaper_url)

			# my.column_content1
			arr.append(column_content1)

			# my.columnn_content2
			arr.append(column_content2)

			# my.columnn_content3
			arr.append(column_content3)

			# my.testimonial_video1
			arr.append(testimonial_video1)

			# my.testimonial_image1
			arr.append(testimonial_image1)

			# my.testimonial_quote1
			arr.append(testimonial_quote1)

			# my.testimonial_nametag1
			arr.append(testimonial_nametag1)

			# my.testimonial_video2
			arr.append(testimonial_video2)

			# my.testimonial_image2
			arr.append(testimonial_image2)

			# my.testimonial_quote2
			arr.append(testimonial_quote2)

			# my.testimonial_nametag2
			arr.append(testimonial_nametag2)

			# my.form_header
			arr.append(form_header)

			# my.custom_body_html  (scripts)
			arr.append(custom_body_html)

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
