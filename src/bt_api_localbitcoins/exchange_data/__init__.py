from __future__ import annotations

from bt_api_base.containers.exchanges.exchange_data import ExchangeData


_FALLBACK_REST_PATHS = {
    "get_server_time": "GET /api/ecjson.php",
    "get_tick": "GET /bitcoinaverage/ticker-all-currencies/",
    "get_all_tickers": "GET /bitcoinaverage/ticker-all-currencies/",
    "get_exchange_info": "GET /api/currencies/",
    "get_ads": "GET /api/ad-get/{id}/",
    "get_ads_search": "GET /buy-bitcoins-online/{currency}/",
    "get_online_ads": "GET /buy-bitcoins-online/{currency}/{country_code}/",
    "get_wallet": "GET /api/wallet/",
    "get_wallet_balance": "GET /api/wallet-balance/",
    "get_account": "GET /api/myself/",
    "get_balance": "GET /api/wallet-balance/",
}


class LocalBitcoinsExchangeData(ExchangeData):
    """Base exchange data for LocalBitcoins (P2P, HMAC-SHA256)."""

    def __init__(self) -> None:
        super().__init__()
        self.exchange_name = "LOCALBITCOINS___SPOT"
        self.asset_type = "SPOT"
        self.rest_url = "https://localbitcoins.com"
        self.wss_url = ""
        self.rest_paths = dict(_FALLBACK_REST_PATHS)
        self.wss_paths = {}
        self.kline_periods = {"1d": "1d"}
        self.reverse_kline_periods = {"1d": "1d"}
        self.legal_currency = ["USD", "EUR", "GBP", "RUB", "BTC"]

    @staticmethod
    def get_symbol(symbol):
        return symbol.lower().replace("-", "_").replace("/", "_")

    @staticmethod
    def get_reverse_symbol(symbol):
        return symbol.upper().replace("_", "-")

    def get_period(self, period: str) -> str:
        return self.kline_periods.get(period, period)

    def get_reverse_period(self, period: str) -> str:
        return self.reverse_kline_periods.get(period, period)

    def get_rest_path(self, key: str, **kwargs) -> str:
        if key not in self.rest_paths or self.rest_paths[key] == "":
            raise ValueError(f"[{self.exchange_name}] REST path not found: {key}")
        path = self.rest_paths[key]
        if kwargs:
            for k, v in kwargs.items():
                path = path.replace(f"{{{k}}}", str(v).lower())
        return str(path)


class LocalBitcoinsExchangeDataSpot(LocalBitcoinsExchangeData):
    def __init__(self) -> None:
        super().__init__()
        self.asset_type = "SPOT"
