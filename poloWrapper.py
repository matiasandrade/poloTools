import poloniex
import json
import numpy
# change log to actual logging function

class CurrencyData(object):# rename perhaps
	def __init__(self, rawTicker, timeStamp):
		for keyPair in rawTicker:
			pairData = rawTicker[keyPair]
			# implement in numpy arrays: timestamp, last, bid, ask
			pair_str = keyPair.lower()# use lowercases for object keys
			last = pairData["last"]
			bid = pairData["highestBid"]
			ask = pairData["lowestAsk"]
			self.pair_str = np.array([timeStamp, last, bid, ask])


class Polo(object):
	def __init__(
		self, Key=False, Secret=False, coach=True,
		timeout=5):
		
		self.poloniex = poloniex.Poloniex(
			Key, Secret, coach, 
			timeout, logging.WARNING, True)
			# sets extend as true for this script's function choice to work
		self.MINUTE, self.HOUR, self.DAY, self.WEEK, self.MONTH, self.YEAR = \
					60, 60*60, 60*60*24, 60*60*24*7, 60*60*24*30, 60*60*24*365
		if not Key and not Secret:
			# log
			print("Key and secret not defined, public commands only.")
		
	def ticker(self, pairObj=False):
		tickerData = self.poloniex.marketTicker()
		timeStamp = time.time()
		if pairObj == False:
			# log
			print("No pair object passed, returning complete market list.")
			
		else:
			print("Returning ticker data for currency pairs in list.")

	def historical(self, lookbackPeriod=self.MONTH*3, density=300):
		timeNow = time.time()
		timeBefore = timeNow-lookbackPeriod
		historical = []
		historicalManip = []
		if len(currList) == 1:
			historicalManip.append(self.poloniex.marketChart(currList[0], density, timeNow, timeBefore))
		elif len(currlist) > 1:
			for elem in currList:
				historicalManip.append(self.poloniex.marketChart(elem, density, timeNow, timeBefore))
				
"""	
# Public
self.api = self.__call__
self.marketTicker = self.returnTicker
self.marketVolume = self.return24hVolume
self.marketStatus = self.returnCurrencies
self.marketLoans = self.returnLoanOrders
self.marketOrders = self.returnOrderBook
self.marketChart = self.returnChartData
# Private
self.myTradeHist = self.returnTradeHistory
self.myBalances = self.returnBalances
self.myAvailBalances = self.returnAvailableAccountBalances
self.myMarginAccountSummary = self.returnMarginAccountSummary
self.myMarginPosition = self.getMarginPosition
self.myCompleteBalances = self.returnCompleteBalances
self.myAddresses = self.returnDepositAddresses
self.myOrders = self.returnOpenOrders
self.myDepositsWithdraws = self.returnDepositsWithdrawals
self.myTradeableBalances = self.returnTradableBalances
self.myActiveLoans = self.returnActiveLoans
self.myOpenLoanOrders = self.returnOpenLoanOffers
self.myFeeInfo = self.returnFeeInfo
self.myLendingHistory = self.returnLendingHistory
self.orderTrades = self.returnOrderTrades
self.createLoanOrder = self.createLoanOffer
self.cancelLoanOrder = self.cancelLoanOffer
"""