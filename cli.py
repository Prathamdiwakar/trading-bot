import argparse
from bot.client import get_client
from bot.orders import place_order
from bot.validators import validate_inputs
from bot.logging_config import logger

def main():
    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")
    
    parser.add_argument("--symbol", required=True, help="Trading pair e.g. BTCUSDT")
    parser.add_argument("--side", required=True, help="BUY or SELL")
    parser.add_argument("--type", required=True, dest="order_type", help="MARKET or LIMIT")
    parser.add_argument("--quantity", required=True, help="Order quantity")
    parser.add_argument("--price", required=False, help="Price (required for LIMIT orders)")

    args = parser.parse_args()

    try:
        validate_inputs(args.symbol, args.side, args.order_type, args.quantity, args.price)
        
        print("\n========== ORDER SUMMARY ==========")
        print(f"Symbol    : {args.symbol.upper()}")
        print(f"Side      : {args.side.upper()}")
        print(f"Type      : {args.order_type.upper()}")
        print(f"Quantity  : {args.quantity}")
        if args.price:
            print(f"Price     : {args.price}")
        print("====================================\n")

        client = get_client()
        order = place_order(client, args.symbol, args.side, args.order_type, args.quantity, args.price)

        print("\n========== ORDER RESPONSE ==========")
        print(f"Order ID      : {order.get('orderId')}")
        print(f"Status        : {order.get('status')}")
        print(f"Executed Qty  : {order.get('executedQty')}")
        print(f"Avg Price     : {order.get('avgPrice', 'N/A')}")
        print("=====================================\n")
        print("✅ Order placed successfully!")

    except ValueError as ve:
        print(f"❌ Validation Error: {ve}")
        logger.error(f"Validation Error: {ve}")
    except Exception as e:
        print(f"❌ Error: {e}")
        logger.error(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()