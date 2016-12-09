import poloniex
import numpy as np

def getMarketDepth(pair="USDT_BTC", printB=False):
	polo = poloniex.Poloniex(extend=True)
	orderData = polo.marketOrders(pair, depth=70)
	# print(orderData)
	bidArray = np.ndarray([])
	for bidOrder in orderData['bids']:
		price = float(bidOrder[0])
		amount = float(bidOrder[1])
		print(price, amount)
		order = np.ndarray([price, amount], shape=(2,1))
		# print(order)
		assert False
		np.append(bidArray, order)
	print(bidArray)
# from getMarketDepth import getMarketDepth

getMarketDepth()