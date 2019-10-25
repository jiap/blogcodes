import pymysql
import matplotlib.pyplot as plt
import matplotlib as mpl
from datetime import datetime
import matplotlib.dates as mdates


mydb = pymysql.connect(
	host  = "localhost",
	user = "root",
	password = "Password",
	database = "btc_price")

mycursor = mydb.cursor()

sql  = "SELECT * FROM price ORDER BY inserted_at DESC LIMIT 50"
mycursor.execute(sql)

myresult = mycursor.fetchall()

price_array = []
time_array = []

for i in myresult:
	price_array.append(float(i[0]))
	time_array.append(i[1])

fig, ax = plt.subplots(1)

fig.autofmt_xdate()
plt.plot(time_array, price_array)

xfmt = mdates.DateFormatter('%y-%m-%d %H:%M')
ax.xaxis.set_major_formatter(xfmt)

plt.gcf().autofmt_xdate()
plt.show()





