import poloniex
import time
import re
second = 1
minute = second*60
hour = minute*60
day = hour*24
month = day*30

defStart = float(time.time()) - (90*day)
defEnd = time.time()
	polo = poloniex.Poloniex(extend=True)
	btcData = polo.marketChart(pair, day, start, end)
	print(btcData[0])
	outputList = []
	for sample in btcData:
		outStr = sample['high'], sample['low'], sample['open'], sample['close'], sample['volume']

		outputList.append(outStr)

		for stringlet in outputList:
			print(str(stringlet))
			outStringlet = str(stringlet).replace("(", "")
			outStringlet = outStringlet.replace("'", "")
			outStringlet = outStringlet.replace(")", "")
			f.write(outStringlet)
			f.write("\n")