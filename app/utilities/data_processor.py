# app/utilities/data_processor.py
class PortfolioAnalyzer:
    """Handles portfolio calculations and analytics"""
    
    def __init__(self, transactions):
        self.transactions = transactions
        
    def calculate_cost_basis(self):
        """Calculate total invested amount"""
        return sum(
            t.quantity * t.price 
            for t in self.transactions 
            if t.transaction_type == 'BUY'
        )
    
    def calculate_current_value(self, current_prices):
        """Calculate current market value"""
        # current_prices = {symbol: price} from API
        return sum(
            t.quantity * current_prices.get(t.symbol, 0)
            for t in self.transactions
        )