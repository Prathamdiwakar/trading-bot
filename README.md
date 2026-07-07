# Binance Futures Testnet Trading Bot

A Python CLI application to place **MARKET** and **LIMIT** orders on Binance Futures Testnet. Built with clean layered architecture, structured logging, and proper error handling.

---

## Features

- Place MARKET and LIMIT orders on Binance Futures Testnet
- Supports BUY and SELL on any futures pair (e.g. BTCUSDT, ETHUSDT)
- CLI-based input with full validation
- Structured logging to file and console
- Clean separation of concerns — client, orders, validators, CLI layers
- API keys managed securely via environment variables

---

## Project Structure

```
trading_bot/
├── bot/
│   ├── __init__.py
│   ├── client.py          # Binance Futures client setup
│   ├── orders.py          # Order placement logic
│   ├── validators.py      # Input validation
│   └── logging_config.py  # Logging configuration
├── logs/                  # Auto-generated log files
├── cli.py                 # CLI entry point
├── requirements.txt
├── .env                   # API keys (not committed)
└── README.md
```

---

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/Prathamdiwakar/trading-bot.git
cd trading-bot
```

### 2. Install dependencies

```bash
pip3 install -r requirements.txt
```

### 3. Create a Binance Futures Testnet account

- Go to [testnet.binancefuture.com](https://testnet.binancefuture.com)
- Register and log in
- Navigate to **API Key** section and generate your API credentials

### 4. Configure environment variables

Create a `.env` file in the project root:

```
BINANCE_API_KEY=your_api_key_here
BINANCE_API_SECRET=your_api_secret_here
```

---

## Usage

### MARKET Order

```bash
python3 cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### LIMIT Order

```bash
python3 cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 95000
```

---

## CLI Arguments

| Argument | Required | Description |
|----------|----------|-------------|
| `--symbol` | Yes | Trading pair e.g. `BTCUSDT` |
| `--side` | Yes | `BUY` or `SELL` |
| `--type` | Yes | `MARKET` or `LIMIT` |
| `--quantity` | Yes | Order quantity |
| `--price` | LIMIT only | Limit price (required for LIMIT orders) |

---

## Sample Output

```
========== ORDER SUMMARY ==========
Symbol    : BTCUSDT
Side      : BUY
Type      : MARKET
Quantity  : 0.001
====================================

[INFO] Binance Futures Testnet client initialized
[INFO] Placing MARKET BUY order | Symbol: BTCUSDT | Qty: 0.001
[INFO] Order placed successfully!
[INFO] Order ID: 19755828908
[INFO] Status: NEW
[INFO] Executed Qty: 0.0000

========== ORDER RESPONSE ==========
Order ID      : 19755828908
Status        : NEW
Executed Qty  : 0.0000
Avg Price     : N/A
=====================================

✅ Order placed successfully!
```

---

## Logging

Logs are automatically saved to the `logs/` directory with timestamps:

```
logs/trading_20260707_105848.log
```

Each log file captures:
- API requests and responses
- Order details
- Validation errors
- Unexpected exceptions

---

## Error Handling

The bot gracefully handles:
- Invalid symbol, side, or order type
- Missing price for LIMIT orders
- Binance API errors (e.g. price out of range)
- Network failures
- Unexpected exceptions

The program never crashes — all errors are caught, logged, and displayed to the user.

---

## Assumptions

- Uses Binance Futures Testnet only — no real funds involved
- API keys are loaded from `.env` file via `python-dotenv`
- Logs are stored locally and not committed to version control
- Price validation is handled by Binance API (e.g. LIMIT price must be within allowed range)

---

## Tech Stack

- Python 3.x
- [python-binance](https://github.com/sammchardy/python-binance)
- python-dotenv
- logging (standard library)
- argparse (standard library)

---

## Author

**Pratham Diwakar**  
GitHub: [@Prathamdiwakar](https://github.com/Prathamdiwakar)
