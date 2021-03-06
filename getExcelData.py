import poloniex
import time
import re
import datetime
second = 1
minute = second*60
hour = minute*60
day = hour*24
month = day*30

defStart = float(time.time()) - (90*day)
defEnd = time.time()
def unixToDate(unix):
	return datetime.datetime.fromtimestamp(
			int(unix)
		).strftime('%Y-%m-%d %H:%M:%S')
def getExcelData(pair="USDT_BTC", location="", period=day, start=defStart, end=defEnd):
	polo = poloniex.Poloniex(extend=True)
	if location == "C:/":
		print("Saving file to default directory.")
	btcData = polo.marketChart(pair, day, start, end)
	print(btcData[0])
	outputList = []
	for sample in btcData:
		outStr = sample['high'], sample['low'], sample['open'], sample['close'], sample['volume']

		outputList.append(outStr)

	with open(location+pair+".csv", 'w') as f:
		f.write("high, low, open, close, volume, "
			+ str(period)+ ", Start: "+ unixToDate(start)+ ", End: "+ unixToDate(end))
		f.write("\n")
		for stringlet in outputList:
			print(str(stringlet))
			outStringlet = str(stringlet).replace("(", "")
			outStringlet = outStringlet.replace("'", "")
			outStringlet = outStringlet.replace(")", "")
			f.write(outStringlet)
			f.write("\n")
getExcelData()