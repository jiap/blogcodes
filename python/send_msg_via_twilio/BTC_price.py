# -*- coding: utf-8 -*-

import requests
from lxml import etree
import re

def gethtmlurl(url):
	try:
		html = requests.get(url)
		return html.text
	except:
		return ""

def getprice(url):
	text = gethtmlurl(url)
	selector = etree.HTML(text)
	currency_exchange_rates = selector.xpath("//div[@id='currency-exchange-rates']/@data-cny")
	currency_rate = float(currency_exchange_rates[0])
	price_btc_usd = selector.xpath('//tr[@id="id-bitcoin"]//td[4]//a/text()')
	price_btc = float(price_btc_usd[0].split("$")[1])
	price_btc_cny = round(price_btc / currency_rate, 2)
	return price_btc_cny

if __name__ == '__main__':
  	main()