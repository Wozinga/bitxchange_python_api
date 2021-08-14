import pytest

from bitxchange.errors import TargetPairError

from bitxchange.spot import market


@pytest.fixture(scope="function")
def mocked_query_exchange(mocker):
    mocked_query_exchange = mocker.patch.object(market.Market, "query_exchange")

    yield mocked_query_exchange

    # cleanup


class TestMarket:

    market_obj = market.Market("https://test.com")

    def test_available_trading_pairs(self, mocked_query_exchange):

        self.market_obj.available_trading_pairs()

        mocked_query_exchange.assert_called_once_with("/api/available_pairs")

    def test_all_market_ticker(self, mocked_query_exchange):

        self.market_obj.all_market_ticker()

        mocked_query_exchange.assert_called_once_with("/api/tickers")

    def test_volume_24h(self, mocked_query_exchange):

        self.market_obj.volume_24h()

        mocked_query_exchange.assert_called_once_with("/api/volume24")

    def test_specific_market_ticker_success(self, mocker):

        mocked_query_exchange = mocker.patch.object(
            market.Market, "query_exchange",
            mocker.MagicMock(return_value={"status": 1})
        )

        target_pair = "XYZ"
        ret = self.market_obj.specific_market_ticker(target_pair)
        mocked_query_exchange.assert_called_once_with(f"/api/ticker/{target_pair}")

        assert ret == {"status": 1}

    def test_specific_market_ticker_failure(self, mocker):

        mocked_query_exchange = mocker.patch.object(
            market.Market, "query_exchange",
            mocker.MagicMock(return_value={"status": 0})
        )

        target_pair = "XYZ"

        with pytest.raises(
            TargetPairError,
            match=f"ERROR: '{target_pair}' is not a valid target pair or format"
        ):
            self.market_obj.specific_market_ticker(target_pair)

        mocked_query_exchange.assert_called_once_with(f"/api/ticker/{target_pair}")

    def test_order_book_passing(self, mocker):

        mocked_query_exchange = mocker.patch.object(
            market.Market, "query_exchange",
            mocker.MagicMock(return_value={"status": 1})
        )

        target_pair = "XYZ"
        ret = self.market_obj.order_book(target_pair)
        mocked_query_exchange.assert_called_once_with(f"/api/order_book/{target_pair}")

        assert ret == {"status": 1}

    def test_order_book_failure(self, mocker):

        mocked_query_exchange = mocker.patch.object(
            market.Market, "query_exchange",
            mocker.MagicMock(return_value={"status": 0})
        )

        target_pair = "XYZ"

        with pytest.raises(
            TargetPairError,
            match=f"ERROR: '{target_pair}' is not a valid target pair or format"
        ):
            self.market_obj.order_book(target_pair)

        mocked_query_exchange.assert_called_once_with(f"/api/order_book/{target_pair}")

    def test_trade_history_passing(self, mocker):

        mocked_query_exchange = mocker.patch.object(
            market.Market, "query_exchange",
            mocker.MagicMock(return_value={"status": 1})
        )

        target_pair = "XYZ"
        ret = self.market_obj.trade_history(target_pair)
        mocked_query_exchange.assert_called_once_with(f"/api/trade_history/{target_pair}")

        assert ret == {"status": 1}

    def test_trade_history_failure(self, mocker):

        mocked_query_exchange = mocker.patch.object(
            market.Market, "query_exchange",
            mocker.MagicMock(return_value={"status": 0})
        )

        target_pair = "XYZ"

        with pytest.raises(
            TargetPairError,
            match=f"ERROR: '{target_pair}' is not a valid target pair or format"
        ):
            self.market_obj.trade_history(target_pair)

        mocked_query_exchange.assert_called_once_with(f"/api/trade_history/{target_pair}")










