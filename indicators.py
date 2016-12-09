import numpy as np
class Indicators(object):
	def __init__(self, histData):
		self.data = histData

	def sma(self, data, window=20):
		return np.convolve(data, np.ones((window,))/window)[(window-1):]

	def ema(self, data, window):
		if len(data) < 2 * window:
			raise ValueError("data is too short")
		c = 2.0 / (window + 1)
		current_ema = self.sma(data[-window*2:-window], window)
		for value in data[-window:]:
			current_ema = (c * value) + ((1 - c) * current_ema)
		return current_ema

	def dpo(self, data, window=21):
		shifted_period = (window / 2 + 1)
		dpo = datasma(data, window)[shifted_period:]