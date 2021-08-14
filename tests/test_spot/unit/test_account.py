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

        params = {
            "orderId": 1
        }

        self.account_obj.check_order_status(**params)
        mocked_send_request.assert_called_once_with("POST", "/trade/orderstatus", params)

    def test_check_order_status_missing_param_failing(self, mocked_send_request):

        params = {}

        with pytest.raises(ValueError):
            self.account_obj.check_order_status(**params)
        
        mocked_send_request.assert_not_called()

    def test_cancel_order_passing(self, mocked_send_request):

        params = {
            "orderId": 1
        }

        self.account_obj.cancel_order(**params)
        mocked_send_request.assert_called_once_with("POST", "/trade/cancelOrder", params)

    def test_cancel_order_missing_param_failing(self, mocked_send_request):

        params = {}

        with pytest.raises(ValueError):
            self.account_obj.cancel_order(**params)
        
        mocked_send_request.assert_not_called()

    def test_get_wallet_balance_passing(self, mocked_send_request):

        params = {
            "symbol": 'BTC'
        }

        self.account_obj.get_wallet_balance(**params)
        mocked_send_request.assert_called_once_with("POST", "/trade/getBalance", params)

    def test_get_wallet_balance_missing_param_failing(self, mocked_send_request):

        params = {}

        with pytest.raises(ValueError):
            self.account_obj.get_wallet_balance(**params)
        
        mocked_send_request.assert_not_called()
