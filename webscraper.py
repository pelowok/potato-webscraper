import xlwt
import requests

from bs4 import BeautifulSoup
from get_title import get_title
from get_hero_image import get_hero_image
from get_content_title import get_content_title

styleError = xlwt.easyxf('font: name Times New Roman, color-index red, bold on')

with open("url_short.p", "rU") as myfile:
	url_list = myfile.readlines()

# create Excel workbook
wb = xlwt.Workbook(encoding='utf-8', style_compression=0)

# create wb.sheet
ws = wb.add_sheet('testSheet', cell_overwrite_ok=True)

# loop through URLs in url_list
i = 0
page = []
for cor, url in enumerate(url_list):
	i += 1
	url = url.rstrip()
	if url.startswith('http:'):
		try:
			page = requests.get(url)
			soup = BeautifulSoup(page.text, "html.parser")
			site_title = get_title(soup)  # returns string
			hero_img = get_hero_image(soup)  # returns [] or bs4.tag
			content_title = get_content_title(soup)
			if url:
				ws.write(cor, 0, url)
			if site_title:
				ws.write(cor, 1, str(site_title))
			if hero_img:
				ws.write(cor, 2, str(hero_img[0]))
				ws.write(cor, 3, str(hero_img[1]))
				ws.write(cor, 4, str(hero_img[2]))
			if content_title:
				ws.write(cor, 5, content_title)
		except requests.exceptions.RequestException as e:  # This is the correct syntax
			ws.write(cor, 0, url)
			ws.write(cor, 1, str(e), styleError)
			print str(i) + " : " + e
	else:
		print str(i) + " : n/a"
		# print str(i) + " : Not a URL (skipped) : " + str(url).strip()
wb.save('testBook.xls')
