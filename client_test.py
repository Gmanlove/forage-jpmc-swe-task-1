import unittest
from unittest.mock import Mock, patch
from datafeed_script import getDataPoint, getRatio

class TestDatafeedFunctions(unittest.TestCase):
    
    def test_getDataPoint(self):
        quote = {
            "symbol": "AAPL",
            "top_bid": {"price": "150.00"},
            "top_ask": {"price": "151.00"}
        }
        stock, bid_price, ask_price, price = getDataPoint(quote)
        
        self.assertEqual(stock, "AAPL")
        self.assertEqual(bid_price, 150.00)
        self.assertEqual(ask_price, 151.00)
        self.assertEqual(price, 150.50)
    
    def test_getRatio(self):
        ratio = getRatio(10, 5)
        self.assertEqual(ratio, 2)
        
        ratio = getRatio(10, 0)
        self.assertIsNone(ratio)

if __name__ == '__main__':
    unittest.main()
