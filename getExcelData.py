import poloniex
import time
import re
second = 1
minute = second*60
hour = minute*60
day = hour*24
month = day*30

start = float(time.time()) - (90*day)
end = time.time()

polo = poloniex.Poloniex(extend=True)

btcData = polo.marketChart('USDT_BTC', day, start, end)
print(btcData[0])
outputList = []
for sample in btcData:
	outStr = sample['high'], sample['low'], sample['open'], sample['close'], sample['volume']

	outputList.append(outStr)

with open("C:/Users/mat97/Desktop/exampleExcel.csv", 'w') as f:
	for stringlet in outputList:
		print(str(stringlet))
		outStringlet = str(stringlet).replace("(", "")
		outStringlet = outStringlet.replace("'", "")
		outStringlet = outStringlet.replace(")", "")
		f.write(outStringlet)
		f.write("\n")