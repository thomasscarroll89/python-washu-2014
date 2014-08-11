import unittest
from random import *
from portfolio import *

class portfolioTest(unittest.TestCase):

	def setUp(self):
		self.myPortfolio = portfolio(cash=967, stocks={}, mutual_funds={}, history="")
		self.s = Stock(20, "HFH")
		self.s2 = Stock(25, "STL")
		self.mf = MutualFund("JGB")
		self.stock_portfolio = portfolio(cash=967, stocks={"HFH": 10}, mutual_funds={"JGB": 50}, history="")
		
	def test_deposit(self):
		self.assertEqual(1067, self.myPortfolio.addCash(100).cash)

	def test_withdrawal(self):
		self.assertEqual(867, self.myPortfolio.withdrawCash(100).cash)

	def test_buy_stock(self):
		#First test for an empty portfolio that has no stocks in it already
		self.myPortfolio.buyStock(5, self.s) #buy 5 shares at $20 a share
		self.assertEqual(867, self.myPortfolio.cash)
		self.assertEqual({"HFH": 5}, self.myPortfolio.stocks)
		#Next test for a portfolio that already has stocks in it
		self.stock_portfolio.buyStock(5, self.s) # buy 5 shares at $20 a share
		self.stock_portfolio.buyStock(4, self.s2) #buy 4 shares at $25 a share
		self.assertEqual(767, self.stock_portfolio.cash) #check cash in portfolio
		self.assertEqual({"HFH": 15, "STL": 4}, self.stock_portfolio.stocks) 
	
	def test_sell_stock(self):
		#First test for an empty portfolio; should receive an error message
		self.assertEqual("Error: stock not found in portfolio.", self.myPortfolio.sellStock(1, self.s))
		#Second test what happens when we try to sell more stocks than we have in the portfolio
		self.assertEqual("Error: number of stocks in portfolio is less than the number of stocks trying to be sold.", self.stock_portfolio.sellStock(15, self.s))
	
	def test_sell_stock_2(self):
		#Third, test to see if the function runs correctly when it has enough stock to sell
		stock_portfolio = self.stock_portfolio.sellStock(1, self.s)
		self.assertEqual({"HFH": 9}, self.stock_portfolio.stocks)
		self.assertTrue(self.stock_portfolio.cash >= 977)
		self.assertTrue(self.stock_portfolio.cash <= 997)
				
	def test_buy_mutual(self):
		#First, test for an empty portfolio
		self.myPortfolio.buyMutualFund(100, self.mf)
		self.assertEqual(867, self.myPortfolio.cash)
		self.assertEqual({"JGB": 100}, self.myPortfolio.mutual_funds)
		#Second, test for a portfolio that already has mutual funds in it
		self.stock_portfolio.buyMutualFund(100, self.mf)
		self.assertEqual(867, self.stock_portfolio.cash)
		self.assertEqual({"JGB": 150}, self.stock_portfolio.mutual_funds)
	
	def test_sell_mutual(self):
		#First, test for an empty portfolio
		self.assertEqual("Error: mutual fund not found in portfolio.", self.myPortfolio.sellMutualFund(1, self.mf))
		#Second test what happens when we try to sell more shares than we have 
		self.assertEqual("Error: number of shares in portfolio is less than the number of shares trying to be sold.", self.stock_portfolio.sellMutualFund(51, self.mf))
	
	def test_sell_mutual_2(self):
		#Third, test for when we have enough of a stock to sell
		stock_portfolio = self.stock_portfolio.sellMutualFund(25, self.mf)
		self.assertEqual({"JGB": 25}, self.stock_portfolio.mutual_funds)
		self.assertTrue(self.stock_portfolio.cash >= 989.5)
		self.assertTrue(self.stock_portfolio.cash <= 997)
		
	def test_history(self):
		stock_portfolio = self.stock_portfolio.addCash(156)
		stock_portfolio = self.stock_portfolio.withdrawCash(39)
		stock_portfolio = self.stock_portfolio.buyStock(5, self.s)
		stock_portfolio = self.stock_portfolio.buyMutualFund(50, self.mf)
		self.assertEqual("\n$156.00 added to portfolio.\n$39.00 withdrawn from portfolio.\n5 shares of HFH purchased for $100.00.\n50 shares of JGB purchased for $50.00.", self.stock_portfolio.history)
		
if __name__ == '__main__':
	unittest.main() 