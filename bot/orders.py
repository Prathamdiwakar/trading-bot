from binance.enums import *
from bot.logging_config import logger

def place_order(client, symbol, side, order_type, quantity, price=None):
    try:
        symbol = symbol.upper()
        side = side.upper()
        order_type = order_type.upper()

        logger.info(f"Placing {order_type} {side} order | Symbol: {symbol} | Qty: {quantity}" + 
                   (f" | Price: {price}" if price else ""))

        if order_type == "MARKET":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type=ORDER_TYPE_MARKET,
                quantity=quantity
            )
        elif order_type == "LIMIT":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type=ORDER_TYPE_LIMIT,
                timeInForce=TIME_IN_FORCE_GTC,
                quantity=quantity,
                price=price
            )

        logger.info(f"Order placed successfully!")
        logger.info(f"Order ID: {order.get('orderId')}")
        logger.info(f"Status: {order.get('status')}")
        logger.info(f"Executed Qty: {order.get('executedQty')}")
        logger.info(f"Avg Price: {order.get('avgPrice', 'N/A')}")

        return order

    except Exception as e:
        logger.error(f"Order failed: {str(e)}")
        raise