# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 12:41:28 2021

@author: Rex DENG
"""

import random

### Define Portfolio
class Portfolio:
    def __init__(self, cash = 0, stock = {}, mutualfund = {}):
        self.cash = cash
        self.stock = stock
        self.mutualfund = mutualfund
        self.transactionlist = []
        
    def addCash(self, addedcash):
        if addedcash > 0:
            self.cash += addedcash
            transaction = "Add %f cash" % addedcash
            self.transactionlist.append(transaction)
            return self.transactionlist[-1]
        else:
            return "You have to add a positive amount of cash."   
    
    def withdrawCash(self, removedcash):
        if removedcash <= self.cash:
            self.cash -= removedcash
            transaction = "Withdraw %f cash." % removedcash
            self.transactionlist.append(transaction)
            return self.transactionlist[-1]
        else:
            return "You only have %f, and do not have sufficient cash to withdraw." % self.cash
    
    def buyStock(self, share, stock):
        if isinstance(share, int) == True:
            newcash = self.cash - share * stock.price
            if newcash < 0:
                return "You do not have sufficient cash to purchase the stock."
            else:
                self.cash -= share * stock.price
                transaction = "Buy %f share of %s (stock)." % (share, stock.symbol)
                self.transactionlist.append(transaction)
                if stock.symbol not in self.stock.keys():
                    self.stock.update({stock.symbol: share})
                    return self.transactionlist[-1]
                else:
                    self.stock[stock.symbol] += share
                    return self.transactionlist[-1]
        else:
            return "You must purchase stock as whole units."
    
    def sellStock(self, share, stock):
        if isinstance(share, int) == True:
            sellingprice = random.uniform(0.5*stock.price, 1.5*stock.price)
            if stock.symbol in self.stock.keys() and self.stock.get(stock.symbol) >= share:
                self.cash += share * sellingprice
                self.stock[stock.symbol] -= share
                transaction = "Sell %f share of %s (stock)." % (share, stock.symbol)
                self.transactionlist.append(transaction)
                return self.transactionlist[-1]
            else:
                return "You do not have sufficient %s (stock) to sell." % stock.symbol
        else:
            return "You must sell stock as whole units."
        
    def buyMutualFund(self, share, mutualfund):
        if isinstance(share, int) == False:
            newcash = self.cash - share * mutualfund.price
            if newcash < 0:
                return "You do not have sufficient cash to purchase the mutual fund."
            else:
                self.cash -= share * mutualfund.price
                transaction = "Buy %f share of %s (mutual fund)." % (share, mutualfund.symbol)
                self.transactionlist.append(transaction)
                if mutualfund.symbol not in self.mutualfund.keys():
                    self.mutualfund.update({mutualfund.symbol: share})
                    return self.transactionlist[-1]
                else:
                    self.mutualfund[mutualfund.symbol] += share
                    return self.transactionlist[-1]
        else:
            return "You must purchase the mutual fund as fractional shares."
    
    def sellMutualFund(self, share, mutualfund):
        sellingprice = random.uniform(0.9*mutualfund.price, 1.2*mutualfund.price)
        self.cash += share * sellingprice
        if mutualfund.symbol in self.mutualfund.keys() and self.mutualfund.get(mutualfund.symbol) >= share:
            self.cash += share * sellingprice
            self.mutualfund[mutualfund.symbol] -= share
            transaction = "Sell %f share of %s (mutual fund)." % (share, mutualfund.symbol)
            self.transactionlist.append(transaction)
            return self.transactionlist[-1]
        else:
            return "You do not have sufficient %s (mutualfund) to sell." % mutualfund.symbol
        
    def __str__(self):
        nl = "\n"
        return f"cash: {self.cash} {nl}stock: {self.stock} {nl}mutual fund: {self.mutualfund}"
    
    def history(self):
        return self.transactionlist
    
class Stock():
    def __init__(self, price, symbol):
        self.price = price
        self.symbol = symbol    
 
class MutualFund():
    def __init__(self, symbol):
        price = 1
        self.price = price
        self.symbol = symbol    

        
### Test
portfolio = Portfolio()
portfolio.addCash(300)
portfolio.withdrawCash(100)
s = Stock(20, "HFH")
portfolio.buyStock(3, s)
portfolio.buyStock(2, s)
portfolio.sellStock(4, s)
portfolio.sellStock(4, s)
portfolio.buyStock(2.5, s)

mf1 = MutualFund("BRT")
mf2 = MutualFund("GHT")
portfolio.buyMutualFund(10.3, mf1)
portfolio.buyMutualFund(100.3, mf2)
portfolio.buyMutualFund(50.2, mf1)
portfolio.buyMutualFund(25.3, mf1)
portfolio.sellMutualFund(100.3, mf2)
portfolio.sellMutualFund(25, mf2)

portfolio.cash
portfolio.mutualfund
    


print(portfolio)
portfolio.history()
