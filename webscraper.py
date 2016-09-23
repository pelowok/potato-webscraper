import xlwt
import urllib2

from bs4 import BeautifulSoup
from get_title import get_title
from get_head_image import get_head_image

styleError = xlwt.easyxf('font: name Times New Roman, color-index red, bold on')

# with open("url_short.p", "rU") as myfile:
with open("url.p", "rU") as myfile:
	url_list = myfile.readlines()

# create Excel workbook
wb = xlwt.Workbook(encoding='utf-8', style_compression=0)

# create wb.sheet
ws = wb.add_sheet('testSheet', cell_overwrite_ok=True)

# loop through URLs in url_list
i = 0
for cor, url in enumerate(url_list):
	i += 1
	if url.startswith('http:'):
		try:
			page = urllib2.urlopen(url)
			soup = BeautifulSoup(page.read(), "html.parser")
			site_title = get_title(soup)  # returns string
			head_img = get_head_image(soup)  # returns [] or bs4.tag
			# print str(i) + " : " + str(site_title) + ", " + str(head_img)
			if url:
				ws.write(cor, 0, url)
			if site_title:
				ws.write(cor, 1, str(site_title))
			if head_img:
				ws.write(cor, 2, str(head_img))
		except urllib2.HTTPError:
			ws.write(cor, 0, url)
			ws.write(cor, 1, str(urllib2.HTTPError), styleError)
	else:
		print str(i) + " : Not a URL (skipped) : " + str(url).strip()
wb.save('testBook.xls')
