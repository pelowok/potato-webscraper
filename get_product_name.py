import re
from bs4 import BeautifulSoup
from get_product_logo import get_product_logo


def get_product_name(soup=''):
	"""deduces the product name from the page content"""

	prod = ""

	try:
		logo = get_product_logo(soup).split("/")[-1]
		prod = products[logo]()
	except:
		prod = "undetermined"

	return prod


def unknown():
	return "undetermined"


def rm_unknown():
	return "RM (type unknown)"


def max_focus():
	return "MAX Focus"


def backup():
	return "Backup"


def rm_msp():
	return "RM-MSP"


def mail():
	return "Mail"


def ri():
	return "RI"


def rm_itpro():
	return "RM-IT-Pros"


def backup_playbook():
	return "Backup (playbook)"


products = { 'LOGICnow_MAX_Backup_Recovery.png': backup,
             'MAX_Remote_Management.png' : rm_msp,
             '3s - maxfocus-logo.png' : max_focus,
             'footer-logo.png' : max_focus,
             'LOGICnow_MAX_Backup_Product_Logo_Fullcolour.jpg' : backup,
             'LOGICnow_MAX_Backup_Recovery.png' : backup,
             'logicnow-remote-mgmt.png': rm_unknown,
             'logicnow-xsmall.png' : unknown,
             'max_focus_remote_management_logo.png' : max_focus,
             'max_logo.png' : max_focus,
             'MAX_Remote_Management.png' : rm_unknown,
             'max_rm_logo.png' : rm_unknown,
             'max-bylogicnow-logo.png' : unknown,
             'MaxBackup-playbook-Logo.png' : backup_playbook,
             'mf_logo.png' : max_focus}
