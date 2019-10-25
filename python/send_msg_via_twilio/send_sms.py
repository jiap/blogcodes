# -*- encoding: utf-8 -*
import BTC_price
from twilio.rest import Client

url = "https://coinmarketcap.com/"
price = BTC_price.getprice(url)

account_sid = 'Please update account sid'
auth_token = 'Please update auth token'
twilionumber = 'Input twilio number'
mynumber = 'Input receive number'

body_text = "The BTC price is ￥%.2f" % price

def send():
	client = Client(account_sid, auth_token)
	message = client.messages \
	                .create(
	                     body = body_text,
	                     from_ = twilionumber,
	                     to = mynumber 
	                 )
	print "Message sent."
	
if __name__ == "__main__":
    send()
