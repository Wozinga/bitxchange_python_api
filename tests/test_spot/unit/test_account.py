import pytest

from bitxchange.spot import account


@pytest.fixture(scope="function")
def mocked_send_request(mocker):
    mocked_send_request = mocker.patch.object(account.Account, "send_request")

    yield mocked_send_request

    # cleanup


class TestAccount:

    account_obj = account.Account("https://test.com")

    def test_create_order_passing(self, mocked_send_request):
        """
            spot.account.create_order(<kwargs>) should send a create order
            request in the auth users account.
        """
        # GIVEN I have authenticated and supplied the required paramaters
        # WHEN I call the create order endpoint
        # THEN I recieve JSON confirming a new order has been placed

        params = {
            "amount": 1,
            "price": 0.05917959,
            "pair": "BTC/ETH",
            "order_type": 2,
            "type": "sell"
        }

        self.account_obj.create_order(**params)
        mocked_send_request.assert_called_once_with("POST", "/trade/placeOrder", params)

    def test_create_order_missing_param_failing(self, mocked_send_request):
        """
            spot.account.create_order(<kwargs>) should send a create order
            request in the auth users account.
        """
        # GIVEN I have authenticated and supplied incorrect or missing paramaters
        # WHEN I call the create order endpoint
        # THEN I recieve an error and complaint

        params = {
            "amount": 1,
            "price": 0.05917959,
            "pair": "BTC/ETH",
            "order_type": 2
        }

        with pytest.raises(ValueError):
            self.account_obj.create_order(**params)

        mocked_send_request.assert_not_called()

    def test_check_order_status_passing(self, mocked_send_request):
        """
            spot.account.check_order_status(<kwargs>) should return the current
            status of a previously placed order to the authed users account.
        """
        # GIVEN I have authenticated and supplied the required paramaters
        # WHEN I call the check order status endpoint
        # THEN I recieve JSON response with an update on the target orders status

        params = {
            "orderId": 1
        }

        self.account_obj.check_order_status(**params)
        mocked_send_request.assert_called_once_with("POST", "/trade/orderstatus", params)

    def test_check_order_status_missing_param_failing(self, mocked_send_request):
        """
            spot.account.check_order_status(<kwargs>) should return the current
            status of a previously placed order to the authed users account.
        """
        # GIVEN I have authenticated and supplied a missing parameter
        # WHEN I call the check order status endpoint
        # THEN I recieve a ValueError response and complaint message

        params = {}
        with pytest.raises(ValueError):
            self.account_obj.check_order_status(**params)

        mocked_send_request.assert_not_called()

    def test_cancel_order_passing(self, mocked_send_request):
        """
            spot.account.cancel_order(<kwargs>) should cancel a target order
            on the authed users account.
        """
        # GIVEN I have authenticated and supplied the required paramaters
        # WHEN I call the cancel order endpoint
        # THEN I recieve JSON response with a cancelation confirmation

        params = {
            "orderId": 1
        }

        self.account_obj.cancel_order(**params)
        mocked_send_request.assert_called_once_with("POST", "/trade/cancelOrder", params)

    def test_cancel_order_missing_param_failing(self, mocked_send_request):
        """
            spot.account.cancel_order(<kwargs>) should cancel a target order
            on the authed users account.
        """
        # GIVEN I have authenticated and supplied a missing parameter
        # WHEN I call the cancel order endpoint
        # THEN I recieve a ValueError response and complaint message

        params = {}
        with pytest.raises(ValueError):
            self.account_obj.cancel_order(**params)
        
        mocked_send_request.assert_not_called()

    def test_get_wallet_balance_passing(self, mocked_send_request):
        """
            spot.account.wallet_ballance(<kwargs>) should return wallet balance of
            the given target symbol
        """
        # GIVEN I have authenticated and supplied the required paramaters
        # WHEN I call the wallet balance endpoint
        # THEN I recieve JSON response containing the wallet balance of that symbol

        params = {
            "symbol": 'BTC'
        }

        self.account_obj.get_wallet_balance(**params)
        mocked_send_request.assert_called_once_with("POST", "/trade/getBalance", params)

    def test_get_wallet_balance_missing_param_failing(self, mocked_send_request):
        """
            spot.account.wallet_ballance(<kwargs>) should return wallet balance of
            the given target symbol
        """
        # GIVEN I have authenticated and supplied a missing parameter
        # WHEN I call the wallet balance endpoint
        # THEN I recieve a ValueError response and complaint message

        params = {}
        with pytest.raises(ValueError):
            self.account_obj.get_wallet_balance(**params)
        
        mocked_send_request.assert_not_called()
