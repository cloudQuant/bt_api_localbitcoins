# LOCALBITCOINS Documentation

## English

Welcome to the LOCALBITCOINS documentation for bt_api.

### Quick Start

```bash
pip install bt_api_localbitcoins
```

```python
from bt_api_py import BtApi

api = BtApi(exchange_kwargs={
    "LOCALBITCOINS___SPOT": {
        "api_key": "your_key",
        "secret": "your_secret",
    }
})

ticker = api.get_tick("LOCALBITCOINS___SPOT", "BTCUSD")
print(ticker)
```

## 中文

欢迎使用 bt_api 的 LOCALBITCOINS 文档。

### 快速开始

```bash
pip install bt_api_localbitcoins
```

```python
from bt_api_py import BtApi

api = BtApi(exchange_kwargs={
    "LOCALBITCOINS___SPOT": {
        "api_key": "your_key",
        "secret": "your_secret",
    }
})

ticker = api.get_tick("LOCALBITCOINS___SPOT", "BTCUSD")
print(ticker)
```

## API Reference

See source code in `src/bt_api_localbitcoins/` for detailed API documentation.
