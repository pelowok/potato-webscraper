

def get_page_language(url=''):
	"""deduces the page language from the url"""

	lang = "EN"

	if "/de-" in url:
		lang = "DE"

	if "/es-" in url:
		lang = "ES"
	if "-esta-" in url:
		lang = "ES"

	if "/pt-" in url:
		lang = "PT"
	if "/br-" in url:
		lang = "PT"
	if ".br" in url:
		lang = "PT"

	if "/it-" in url:
		lang = "IT"

	if "/fr-" in url:
		lang = "FR"

	if "/nl-" in url:
		lang = "NL"

	print "lang : " + lang

	return lang