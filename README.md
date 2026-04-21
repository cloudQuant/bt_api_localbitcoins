# bt_api_localbitcoins

LocalBitcoins exchange plugin for bt_api framework.

## Installation

```bash
pip install bt_api_localbitcoins
```

## Usage

```python
from bt_api_localbitcoins import LocalBitcoinsExchangeDataSpot, LocalBitcoinsRequestDataSpot
```

## Features

- REST API support
- HMAC-SHA256 authentication
- P2P exchange (aggregated ticker data from advertisements)
- Symbol format: `BTCUSD`, `BTCGBP`, etc.
