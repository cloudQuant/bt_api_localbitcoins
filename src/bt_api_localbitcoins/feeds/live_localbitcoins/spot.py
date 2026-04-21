from __future__ import annotations

from typing import Any

from bt_api_base.containers.requestdatas.request_data import RequestData
from bt_api_localbitcoins.feeds.live_localbitcoins.request_base import LocalBitcoinsRequestData


class LocalBitcoinsRequestDataSpot(LocalBitcoinsRequestData):
    def __init__(self, data_queue: Any = None, **kwargs: Any) -> None:
        kwargs.setdefault("exchange_name", "LOCALBITCOINS___SPOT")
        kwargs.setdefault("asset_type", "SPOT")
        super().__init__(data_queue, **kwargs)

    def get_server_time(self, extra_data: Any = None, **kwargs: Any) -> RequestData:
        path, params, extra = self._get_server_time(extra_data, **kwargs)
        return self.request(path, params, extra_data=extra)

    async def async_get_server_time(self, extra_data: Any = None, **kwargs: Any) -> RequestData:
        path, params, extra = self._get_server_time(extra_data, **kwargs)
        return await self.async_request(path, params, extra_data=extra)

    def get_tick(self, symbol: Any, extra_data: Any = None, **kwargs: Any) -> RequestData:
        path, params, extra = self._get_tick(symbol, extra_data, **kwargs)
        return self.request(path, params, extra_data=extra)

    async def async_get_tick(
        self, symbol: Any, extra_data: Any = None, **kwargs: Any
    ) -> RequestData:
        path, params, extra = self._get_tick(symbol, extra_data, **kwargs)
        return await self.async_request(path, params, extra_data=extra)

    def get_ticker(self, symbol: Any, extra_data: Any = None, **kwargs: Any) -> RequestData:
        return self.get_tick(symbol, extra_data, **kwargs)

    async def async_get_ticker(
        self, symbol: Any, extra_data: Any = None, **kwargs: Any
    ) -> RequestData:
        return await self.async_get_tick(symbol, extra_data, **kwargs)

    def get_exchange_info(self, extra_data: Any = None, **kwargs: Any) -> RequestData:
        path, params, extra = self._get_exchange_info(extra_data, **kwargs)
        return self.request(path, params, extra_data=extra)

    async def async_get_exchange_info(self, extra_data: Any = None, **kwargs: Any) -> RequestData:
        path, params, extra = self._get_exchange_info(extra_data, **kwargs)
        return await self.async_request(path, params, extra_data=extra)

    def get_balance(self, symbol: Any = None, extra_data: Any = None, **kwargs: Any) -> RequestData:
        path, params, extra = self._get_balance(extra_data, **kwargs)
        return self.request(path, params, extra_data=extra)

    async def async_get_balance(
        self, symbol: Any = None, extra_data: Any = None, **kwargs: Any
    ) -> RequestData:
        path, params, extra = self._get_balance(extra_data, **kwargs)
        return await self.async_request(path, params, extra_data=extra)

    def get_account(
        self, symbol: Any = "ALL", extra_data: Any = None, **kwargs: Any
    ) -> RequestData:
        path, params, extra = self._get_account(extra_data, **kwargs)
        return self.request(path, params, extra_data=extra)

    async def async_get_account(
        self, symbol: Any = "ALL", extra_data: Any = None, **kwargs: Any
    ) -> RequestData:
        path, params, extra = self._get_account(extra_data, **kwargs)
        return await self.async_request(path, params, extra_data=extra)
