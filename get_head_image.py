from bs4 import BeautifulSoup


def get_head_image( soup='' ):
	"""retrieves image in header, if there is one"""

	# test for <div id='imgHead'>
	# head_img1 = soup.find("div", {"id": "imgHead"})
	# if head_img1:
	# 	output = head_img1
	# else:
	# 	output = []

	# test for <section id='hero-rmm' data-image-source='foo'>
	head_img2 = soup.find("section", {"data-image-source": True})
	if head_img2:
		output = str(head_img2)
	else:
		output = '!!!! NOT FOUND !!!!!!!'

	print output

	return output;
