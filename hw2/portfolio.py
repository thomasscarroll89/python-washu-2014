from random import uniform

class portfolio():
	def __init__(self, cash, stocks={}, mutual_funds={}, history=""):
		self.cash = float(cash)
		self.stocks = stocks
		self.mutual_funds = mutual_funds
		self.history = history
	
	def addCash(self, amount):
		self.cash = self.cash + amount #adds new cash to old cash
		self.history = self.history + "\n$" + format(amount, ".2f") + " added to portfolio."
		return self
	
	def withdrawCash(self, amount):
		self.cash = self.cash - amount #subtracts new cash from old cash
		self.history = self.history + "\n$" + format(amount, ".2f") + " withdrawn from portfolio."
		return self
	
	def buyStock(self, amount, stock_name):
		total_cost = stock_name.price*amount
		self.cash = self.cash - total_cost
		#Next, redefine the number of shares of stock in the portfolio by adding new amount to old amount
		if stock_name.symbol not in self.stocks.keys(): #If stock does not already exist, create a new key for it
			self.stocks[stock_name.symbol] = amount
		else:
			old_amount = self.stocks[stock_name.symbol] #extracts the old number of shares of stocks
			self.stocks[stock_name.symbol] = amount + old_amount
		self.history = self.history + "\n" + str(amount) + " shares of " + stock_name.symbol + " purchased for $" + format(total_cost, ".2f") + "."
		return self
			
	def sellStock(self, amount, stock_name):
		factor = uniform(0.5, 1.5) #get selling price, first by getting random draw from uniform distribution
		sell_price = factor*stock_name.price
		total_cost = sell_price*amount
		#Redefine the number of shares of stock in the portfolio by subtracting new amount from old amount
		if stock_name.symbol not in self.stocks.keys():
			return "Error: stock not found in portfolio."
		elif self.stocks[stock_name.symbol] < amount:
			return "Error: number of stocks in portfolio is less than the number of stocks trying to be sold."
		else:
			old_amount = self.stocks[stock_name.symbol] #extracts the old number of shares of stocks
			self.stocks[stock_name.symbol] = old_amount - amount
			self.cash = self.cash + total_cost
			self.history = self.history + "\n" + str(amount) + " shares of " + stock_name.symbol + " sold for $" + format(total_cost, ".2f") + "."
			return self
			
	def buyMutualFund(self, amount, fund_name):
		self.cash = self.cash - amount #We can simply subtract the amount since each share is sold for exactly one dollar
		#Redefine the number of shares of Mutual Fund in the portfolio by adding new amount to old amount
		if fund_name.symbol not in self.mutual_funds.keys():
			self.mutual_funds[fund_name.symbol] = amount
		else:
			old_amount = self.mutual_funds[fund_name.symbol] #extracts the old number of shares of stocks
			self.mutual_funds[fund_name.symbol] = amount + old_amount
			self.history = self.history + "\n" + str(amount) + " shares of " + fund_name.symbol + " purchased for $" + format(amount, ".2f") + "."
			return self
			
	def sellMutualFund(self, amount, fund_name):
		sell_price = uniform(0.9, 1.2)
		total_cost = sell_price*amount
		#Redefine the number of shares of stock in the portfolio by subtracting new amount from old amount
		if fund_name.symbol not in self.mutual_funds.keys():
			return "Error: mutual fund not found in portfolio."
		elif self.mutual_funds[fund_name.symbol] < amount:
			return "Error: number of shares in portfolio is less than the number of shares trying to be sold."
		else:
			old_amount = self.mutual_funds[fund_name.symbol] #extracts the old number of shares of stocks
			self.mutual_funds[fund_name.symbol] = old_amount - amount
			self.cash = self.cash + total_cost
			self.history = self.history + "\n" + str(amount) + " shares of " + fund_name.symbol + " sold for $" + format(total_cost, ".2f") + "."
			return self
			
	def history(self):
		return self.history
		
class Stock():
	def __init__(self, price, symbol):
		self.price = float(price)
		self.symbol = str(symbol)

class MutualFund():
	def __init__(self, symbol):
		self.symbol = str(symbol)