VALID_SIDES = ["BUY", "SELL"]
VALID_ORDER_TYPES = ["MARKET", "LIMIT"]

def validate_inputs(symbol, side, order_type, quantity, price=None):
    if not symbol:
        raise ValueError("Symbol cannot be empty")
    
    if side.upper() not in VALID_SIDES:
        raise ValueError(f"Invalid side: {side}. Must be BUY or SELL")
    
    if order_type.upper() not in VALID_ORDER_TYPES:
        raise ValueError(f"Invalid order type: {order_type}. Must be MARKET or LIMIT")
    
    if float(quantity) <= 0:
        raise ValueError("Quantity must be greater than 0")
    
    if order_type.upper() == "LIMIT" and (price is None or float(price) <= 0):
        raise ValueError("Price is required for LIMIT orders and must be greater than 0")
    
    return True