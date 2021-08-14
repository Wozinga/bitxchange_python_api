from bitxchange.api import API


class Account(API):
    def create_order(self, **kwargs):
        """
            Description: Creates a new order under the authed account, user
            has the ability to create a market price buy/sell order OR can post
            a fixed price buy/sell order.

            POST /trade/placeOrder

            Guide:

            args: None

            kwargs:
                amount (int) - amount of token to buy or sell
                price (int) - price to pay or be paid for amount
                pair (str) - trading target pair
                order_type (int) - 1=market_price, 2=fixed_price
                type (str) - 'buy' or 'sell'
        """

        mandatory_params = {
            "amount",
            "price",
            "pair",
            "order_type",
            "type"
        }

        # retrun error if Kwargs is missing a mandatory field
        self._check_required_parameter(mandatory_params, **kwargs)
        # self._validate_target_pairs(kwargs['pair'])

        url_path = "/trade/placeOrder"
        return self.send_request("POST", url_path, kwargs)

    def check_order_status(self, **kwargs):
        """
            Description: check status of active order

            POST /trade/orderstatus

            Guide:

            args: None

            kwargs:
                orderId (str) - trade order ID
        """

        mandatory_params = {
            "orderId"
        }

        # retrun error if Kwargs is missing a mandatory field
        self._check_required_parameter(mandatory_params, **kwargs)
        # self._validate_target_pairs(kwargs['pair'])

        url_path = "/trade/orderstatus"
        return self.send_request("POST", url_path, kwargs)

    def cancel_order(self, **kwargs):
        """
            Description: Cancel active order

            POST /trade/cancelOrder

            Guide:

            args: None

            kwargs:
                orderId (str) - trade order ID
        """

        mandatory_params = {
            "orderId"
        }

        # retrun error if Kwargs is missing a mandatory field
        self._check_required_parameter(mandatory_params, **kwargs)

        url_path = "/trade/cancelOrder"
        return self.send_request("POST", url_path, kwargs)

    def get_wallet_balance(self, **kwargs):
        """
            Description: Returns current wallet balance of the
            target token.

            POST /trade/getBalance

            Guide:

            args: None

            kwargs:
                symbol (str) - token symbol
        """

        mandatory_params = {
            "symbol"
        }

        # retrun error if Kwargs is missing a mandatory field
        self._check_required_parameter(mandatory_params, **kwargs)

        url_path = "/trade/getBalance"
        return self.send_request("POST", url_path, kwargs)

    def _check_required_parameter(self, *args, **kwargs):
        from bitxchange.lib.shared_utils import check_required_parameter

        check_required_parameter(*args, **kwargs)

    def _validate_target_pairs(self, target_pairs):
        from bitxchange.lib.shared_utils import validate_target_pair

        validate_target_pair(target_pairs)
