from __future__ import annotations

from bt_api_base.balance_utils import simple_balance_handler as _localbitcoins_balance_handler
from bt_api_base.registry import ExchangeRegistry

from bt_api_localbitcoins.exchange_data import LocalBitcoinsExchangeDataSpot
from bt_api_localbitcoins.feeds.live_localbitcoins.spot import LocalBitcoinsRequestDataSpot


def register_localbitcoins(registry: type[ExchangeRegistry]) -> None:
    registry.register_feed("LOCALBITCOINS___SPOT", LocalBitcoinsRequestDataSpot)
    registry.register_exchange_data("LOCALBITCOINS___SPOT", LocalBitcoinsExchangeDataSpot)
    registry.register_balance_handler("LOCALBITCOINS___SPOT", _localbitcoins_balance_handler)
