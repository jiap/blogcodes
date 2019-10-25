import pymysql

import requests
import json
import time


def get_price():
	url = 'https://api.coinmarketcap.com/v1/ticker/bitcoin/'
	response = requests.get(url).json()
	price_usd = response[0]["price_usd"]
	price_2f = '%.2f' % float(price_usd)
	return price_2f

if __name__ == '__main__':
	mydb = pymysql.connect(
		host  = "localhost",
		user = "root",
		password = "Password",
		database = "btc_price")

	mycursor = mydb.cursor()

	while True:
		btc_price = get_price()
		local_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 

		sql = "INSERT INTO price (price, inserted_at) VALUES ("  + btc_price + ",'" + local_time + "')"
		# print(sql)
		mycursor.execute(sql)
		mydb.commit()
		time.sleep(60)
		print("success")
