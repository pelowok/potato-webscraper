import re

from bs4 import BeautifulSoup
from bs4 import Comment

def sorting_hat(soup=''):
	""" one function to rule them all. the sorting hat assigns a template type that guides the scrape"""

	template = ""
	code = "unknown"

	for comment in soup.find_all(text=lambda text: isinstance(text, Comment)):
		if 'template' in comment:
			if ' id:' in comment:
				if ' path:' in comment:
					code = comment.strip().split('id:')[1].split(' path:')[0]
			elif 'rm-msp-template-1' in comment:
				code = 'rm-msp-template-1'

	for lpe_div in soup.find_all("div", {"id" : re.compile('^lpeCDiv')}):
		if soup.find_all("span", {"mktoname" : "Hero Styling"}):
			code = 'Hero Styling'
		elif soup.find_all("div", {"class" : "sitecontainer"}):
			code = '1642402159'
		else:
			code = 'lpeCDiv'

	if soup.find("div", {"class": "background-sun"}):
		code = 'background-sun'

	template = templates[code]()
	return template


def unknown():
	return 0


def type01():
	return 1


def type02():
	return 2


def type03():
	return 3


def type04():
	return 4


def type05():
	return 5


def type06():
	return 6


def type07():
	return 7


def type08():
	return 8


def type09():
	return 9


def type10():
	return 10


def type11():
	return 11


def type12():
	return 12


def type13():
	return 13


def type14():
	return 14


def type15():
	return 15


templates = {'1642402159': type01,
			'1559063283': type02,
			'1527524596': type03,
			'2410492543': type04,
			'2400147929': type05,
			'2446545017': type06,
			'2227693720': type07,
			'3443123680': type08,
			'367303966': type09,
			'rm-msp-template-1': type10,
			'lpeCDiv': type11,
			'background-sun': type12,
			'unknown': unknown,
			 'Hero Styling': type13}