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
        """
            spot.market.available_trading_pairs() should return a
            list of all available trading pairs
        """
        # GIVEN I can succesfully connect to the API endpoint
        # WHEN I call the the url endpoint
        # THEN I am returned a JSON list of all available trading pairs
        
        self.market_obj.available_trading_pairs()
        mocked_query_exchange.assert_called_once_with("/api/available_pairs")

    def test_all_market_ticker(self, mocked_query_exchange):
        """
            spot.market.all_market_ticker() should return the latest ticker
            for all active pairs on the exchange
        """
        # GIVEN I can succesfully connect to the API endpoint
        # WHEN I call the the url endpoint
        # THEN I am returned a JSON list of all latest tickers

        self.market_obj.all_market_ticker()
        mocked_query_exchange.assert_called_once_with("/api/tickers")

    def test_volume_24h(self, mocked_query_exchange):
        """
            spot.market.volume_24h() should return a
            list of all available trading pairs 24 hour volume
        """
        # GIVEN I can succesfully connect to the API endpoint
        # WHEN I call the the url endpoint
        # THEN I am returned a JSON list of all available trading pairs

        self.market_obj.volume_24h()
        mocked_query_exchange.assert_called_once_with("/api/volume24")

    def test_specific_market_ticker_success(self, mocker):
        """
            spot.market.specific_market_ticker(<target_pair>) should 
            return the latest ticker for the target pair
        """
        # GIVEN I can succesfully connect to the api endpoint
        # WHEN I call the url endpoint and provide a valid target pair
        # THEN I am returned a JSON list containing the latest ticker for target pair

        mocked_query_exchange = mocker.patch.object(
            market.Market, "query_exchange",
            mocker.MagicMock(return_value={"status": 1})
        )

        target_pair = "XYZ"  # Target pair can be anything as backend is mocked
        resp = self.market_obj.specific_market_ticker(target_pair)
        mocked_query_exchange.assert_called_once_with(f"/api/ticker/{target_pair}")

        assert resp == {"status": 1}

    def test_specific_market_ticker_failure(self, mocker):
        """
            spot.market.specific_market_ticker(<target_pair>) should return a
            list of all available trading pairs
        """
        # GIVEN I can succesfully connect to the API endpoint
        # WHEN I call the the url endpoint with an invalid target pair
        # THEN I am returned an error with a complaint message

        mocked_query_exchange = mocker.patch.object(
            market.Market, "query_exchange",
            mocker.MagicMock(return_value={"status": 0})
        )

        target_pair = "XYZ"  # Target pair can be anything as backend is mocked
        with pytest.raises(
            TargetPairError,
            match=f"ERROR: '{target_pair}' is not a valid target pair or format"
        ):
            self.market_obj.specific_market_ticker(target_pair)

        mocked_query_exchange.assert_called_once_with(f"/api/ticker/{target_pair}")

    def test_order_book_passing(self, mocker):
        """
            spot.market.order_book(<target_pair>) should return a
            list of all available trading pairs
        """
        # GIVEN I can succesfully connect to the API endpoint
        # WHEN I call the the url endpoint and provide a valid target pair
        # THEN I am returned a JSON list with all current orders

        mocked_query_exchange = mocker.patch.object(
            market.Market, "query_exchange",
            mocker.MagicMock(return_value={"status": 1})
        )

        target_pair = "XYZ"  # Target pair can be anything as backend is mocked
        resp = self.market_obj.order_book(target_pair)
        mocked_query_exchange.assert_called_once_with(f"/api/order_book/{target_pair}")

        assert resp == {"status": 1}

    def test_order_book_failure(self, mocker):
        """
            spot.market.order_book(<target_pair>) should return a
            list of all available trading pairs
        """
        # GIVEN I can succesfully connect to the API endpoint
        # WHEN I call the the url endpoint and provide an invalid target pair
        # THEN I am returned an error with a complaint message

        mocked_query_exchange = mocker.patch.object(
            market.Market, "query_exchange",
            mocker.MagicMock(return_value={"status": 0})
        )

        target_pair = "XYZ"  # Target pair can be anything as backend is mocked
        with pytest.raises(
            TargetPairError,
            match=f"ERROR: '{target_pair}' is not a valid target pair or format"
        ):
            self.market_obj.order_book(target_pair)

        mocked_query_exchange.assert_called_once_with(f"/api/order_book/{target_pair}")

    def test_trade_history_passing(self, mocker):
        """
            spot.market.trade_history(<target_pair>) should return a
            list containing the trade history of the target pair
        """
        # GIVEN I can succesfully connect to the API endpoint
        # WHEN I call the the endpoint and provide a valid target pair
        # THEN I am returned a JSON list with targets pairs trade history

        mocked_query_exchange = mocker.patch.object(
            market.Market, "query_exchange",
            mocker.MagicMock(return_value={"status": 1})
        )

        target_pair = "XYZ"  # Target pair can be anything as backend is mocked
        resp = self.market_obj.trade_history(target_pair)
        mocked_query_exchange.assert_called_once_with(f"/api/trade_history/{target_pair}")

        assert resp == {"status": 1}

    def test_trade_history_failure(self, mocker):
        """
            spot.market.trade_history(<target_pair>) should return a
            list containing the trade history of the target pair
        """
        # GIVEN I can succesfully connect to the API endpoint
        # WHEN I call the the endpoint and provide an invalid target pair
        # THEN I am returned an error with a complaint message

        mocked_query_exchange = mocker.patch.object(
            market.Market, "query_exchange",
            mocker.MagicMock(return_value={"status": 0})
        )

        target_pair = "XYZ"  # Target pair can be anything as backend is mocked
        with pytest.raises(
            TargetPairError,
            match=f"ERROR: '{target_pair}' is not a valid target pair or format"
        ):
            self.market_obj.trade_history(target_pair)

        mocked_query_exchange.assert_called_once_with(f"/api/trade_history/{target_pair}")
