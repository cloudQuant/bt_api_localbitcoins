"""Tests for LocalbitcoinsExchangeData container."""

from __future__ import annotations

from bt_api_localbitcoins.exchange_data import LocalBitcoinsExchangeData


class TestLocalBitcoinsExchangeData:
    """Tests for LocalBitcoinsExchangeData."""

    def test_init(self):
        """Test initialization."""
        exchange = LocalBitcoinsExchangeData()

        assert exchange.exchange_name == "LOCALBITCOINS___SPOT"
