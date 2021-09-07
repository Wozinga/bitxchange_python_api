Getting Started with bitxchange REST API
========================================

.. meta::
   :description lang=en: Get started with Bitxchange REST API.


This guide will cover the use of the Spot Market API's, parameter options and their expected results, for more
information about the specific methods and behaviors can be found in the code documentation in the git repo.


Installation
------------

* Install via package name

  .. code-block:: bash

     pip install bitxchange-py-api

* Alternatively, install with git repository path

  .. code-block:: bash

    python -m pip install git+https://github.com/Wozinga/bitxchange_python_api.git


API Endpoint Connection
-----------------------
* Spot(base_url=<api_url>, key=<api_key>, secret=<api_secret>)

  To successfully authenticate with the API endpoint Spot() requires a a valid API & secret key
  to be passed in at time of instanciation.

  If no base url is provided it will revert to Bitxchnage default

  .. code-block:: python

    from bitxchange.spot import Spot

    client = Spot(
      base_url='https://exchangeapi.bit-xchange.co',
      key='12345678-1234-1234-1234-1234567890123',
      secret='asdfghj-asdfghjh-asdfghj'
    )


Spot Market Data Endpoints
==========================

Available Trading pairs
-----------------------
.. autofunction:: bitxchange.spot.market.Market.available_trading_pairs

  Request:

  .. code-block:: python

    from bitxchange.spot import Spot

    exchange = Spot()

    print(exchange.available_trading_pairs())


  Response:

  .. code-block:: bash

    {
    'status': 1,
    'message': 'Success',
    'combinations':
      [
        'ETH_BTC',
        'BTC_ETH',
        'USDX_BTC',
        'USDX_ETH',
        'XBTC2_USDX'
      ]
    } 


All Market tickers
------------------
.. autofunction:: bitxchange.spot.market.Market.all_market_tickers

  Request:

  .. code-block:: python

      from bitxchange.spot import Spot

      exchange = Spot()

      print(exchange.all_market_ticker())

  Response:

  .. code-block:: bash

    {
    'status': 1,
    'message': 'Success',
    'combinations': 
      {
      'BTC_ETH': 
        {
        'pair': 
          'BTC_ETH',
          'last': 13.66910445,
          'lowestAsk': 13.66910445,
          'highestBid': 14.53241631,
          'percentChange': 0,
          'base24hrVolume': 0,
          'quote24hrVolume': 0,
          'low24hr': '0.00',
          'high24hr': '0.00'

        },
      'XBTC2_USDX': 
        {
        'pair': 
          'XBTC2_USDX',
          'last': 0.38805,
          'lowestAsk': 0.38805,
          'highestBid': 0.38805,
          'percentChange': 0,
          'base24hrVolume': 0,
          'quote24hrVolume': 0,
          'low24hr': '0.00',
          'high24hr': '0.00'

        },
      'USDX_BTC': 
        {
        'pair': 
          'USDX_BTC',
          'last': 2.1018099999999998,
          'lowestAsk': 2.1018099999999998,
          'highestBid': 2.1018099999999998,
          'percentChange': 0,
          'base24hrVolume': 0,
          'quote24hrVolume': 0,
          'low24hr': '0.00',
          'high24hr': '0.00'

        },
      'USDX_ETH': 
        {
        'pair':
          'USDX_ETH',
          'last': 0.0003025253,
          'lowestAsk': 0.0003025253,
          'highestBid': 0.0003025253,
          'percentChange': 0,
          'base24hrVolume': 0,
          'quote24hrVolume': 0,
          'low24hr': '0.00',
          'high24hr': '0.00'

        },
      'ETH_BTC':
        {
        'pair':
          'ETH_BTC',
          'last': '0.06511605',
          'lowestAsk': 0.065959507,
          'highestBid': 0.0701253706,
          'percentChange': '100.00',
          'base24hrVolume': 0,
          'quote24hrVolume': 0,
          'low24hr': '0.00',
          'high24hr': '0.00'

        }
      }
    }

24 Hour volume
--------------
.. autofunction:: bitxchange.spot.market.Market.volume_24h

  Request:

  .. code-block:: python

    from bitxchange.spot import Spot

    exchange = Spot()

    print(exchange.volume_24h())

  Response:

  .. code-block:: python

    {
    'status': 1,
    'message': 'Success',
    'combinations':
      {
      'ETH_BTC':
        {
        'ETH': 0,
        'BTC': 0
        },
      'USDX_BTC':
        {
        'USDX': 0,
        'BTC': 0
        },
      'USDX_ETH':
        {
        'USDX': 0,
        'ETH': 0
        },
      'BTC_ETH':
        {
        'BTC': 0,
        'ETH': 0
        },
      'XBTC2_USDX':
        {
        'XBTC2': 0,
        'USDX': 0
        }
      }
    } 

Specific Market ticker
----------------------
.. autofunction:: bitxchange.spot.market.Market.specific_market_ticker

  Request:

  .. code-block:: python
      
    from bitxchange.spot import Spot

    exchange = Spot()

    print(exchange.specific_market_ticker('ETH_BTC'))

  Response:

  .. code-block:: bash

    {
    'status': 1,
    'message': 'Success',
    'combinations':
      {
      'pair': 'BTC_ETH',
      'last': 13.66709995,
      'lowestAsk': 13.66709995,
      'highestBid': 14.53028521,
      'percentChange': 0,
      'base24hrVolume': 0,
      'quote24hrVolume': 0,
      'low24hr': '0.00',
      'high24hr': '0.00'

      }

    }

  Expected Error Responses:

  .. code-block:: bash

    ERROR: 'BTC_ET' is not a valid target pair or format 

Order order_book
----------------
.. autofunction:: bitxchange.spot.market.Market.order_book

  Request:

  .. code-block:: python
      
    from bitxchange.spot import Spot

    exchange = Spot()

    print(exchange.order_book('ETH_BTC'))

  Response:

  .. code-block:: bash

    {
    'status': 1,
    'message': 'Success',
    'bids': 
      [

      ], 
    'asks': 
      [
        [
          '1.00000000',
          '0.05917959'
        ]
      ]
    } 

  Expected Error Responses:

  .. code-block:: bash

    ERROR: 'BTC_EH' is not a valid target pair or format

Trade History
-------------
.. autofunction:: bitxchange.spot.market.Market.trade_history

  Request:

  .. code-block:: python
      
      from bitxchange.spot import Spot

      exchange = Spot()

      print(exchange.trade_history('ETH_BC'))

  Response:

  .. code-block:: bash

    {
    'status': 1,
    'message': 'Success',
    'trade_history': 
      [
        {
        'date': '2021-08-10T10:04:03.546Z',
        'type': 'Sell',
        'rate': '0.06511605',
        'amount': '1.00000000',
        'total': '0.06511605'
        }, 
        {
        'date': '2021-08-10T09:59:56.020Z',
        'type': 'Sell',
        'rate': '0.06511605',
        'amount': '1.00000000',
        'total': '0.06511605'
        },
        {
        'date': '2021-08-10T09:46:02.707Z',
        'type': 'Buy',
        'rate': '0.06923458',
        'amount': '1.00000000',
        'total': '0.06923458'
        },
        {
        'date': '2021-08-10T09:43:50.563Z',
        'type': 'Sell',
        'rate': '0.06509066',
        'amount': '1.00000000',
        'total': '0.06509066'
        },
        {
        'date': '2021-08-10T08:57:20.138Z',
        'type': 'Sell',
        'rate': '0.06503080',
        'amount': '1.00000000',
        'total': '0.06503080'
        },
        {
        'date': '2021-08-06T07:16:31.622Z',
        'type': 'Sell',
        'rate': '0.06459963',
        'amount': '3.00000000',
        'total': '0.19379889'
        },
        {
        'date': '2021-08-06T07:15:53.359Z',
        'type': 'Sell',
        'rate': '0.06461662',
        'amount': '1.00000000',
        'total': '0.06461662'
        }
      ]
    } 

  Expected Error Responses:

  .. code-block:: bash

    ERROR: 'BTC_EH' is not a valid target pair or format



Account Order Endpoints
=======================
All API's that interact with a users account require the API call to be
authenticated

.. code-block:: python

  exchange = Spot(
    key='12345678-1234-1234-1234-123456789012',
    secret='abcdefg-abcdefg-abcdefg'
  )

Create New Account Order
------------------------

.. autofunction:: bitxchange.spot.account.Account.create_order

  Request:

  .. code-block:: python

    from bitxchange.spot import Spot

    exchange = Spot(
      key='12345678-1234-1234-1234-123456789012',
      secret='abcdefg-abcdefg-abcdefg'
    )

    params = {
      "amount": 1,
      "price": 0.05917959,
      "pair": "BTC/ETH",
      "order_type": 2,
      "type": "sell"
    }

    x = client.create_order(**params)
    print(x)


  Response:

  .. code-block:: bash

    {
    'status': 200,
    'message': 'Successfully placed your order',
    'data': 
      {
      'userId': 'F3Ry+a4de+vJsydbGpB5rpC+llY/+8tqQZCmCVqO+Q0=',
      'firstCurrency': '5df20c3fb6e5c35860023dd3',
      'secondCurrency': '5df20c3fb6e5c35860023dd4',
      'Amount': 1,
      'Price': 0.05917959,
      'Type': 'Sell',
      'Process': 'Pending',
      'Fee': 0.0005918,
      'Total': 0.05917959,
      'wallet': '',
      'ordertype': '2',
      'pair': '60a6c1719f97153d6d65ead0',
      'status': 'active',
      'fee_per': 1,
      'stopprice': 0,
      'partial': False,
      'trade_his': '',
      'tradetime': '',
      'order_no': '',
      'incre_order': '',
      'user_type': 'user',
      'filledAmount': 0,
      'orderDate': '2021-08-13T18:31:22.266Z',
      'orderTime': '2021-08-13T18:31:22.266Z',
      'datetime': '2021-08-13T18:31:22.266Z',
      'updated_at': '2021-08-13T18:31:22.266Z',
      '__v': 0,
      'orderId': 'sYqFgOK1Q9TV5LAJvxtmiSajirIWPphSWWeXcfGuBQ4='
      }
    }

  Expected Error Responses

  .. code-block:: bash

    {
    'status': 412, 'message': 'Amount and Price decimal should not be greater than eight digits.'
    }

    {
    'status': 412, 'message': 'Insufficient Balance'
    }

Check Statis of Active Order
----------------------------
.. autofunction:: bitxchange.spot.account.Account.check_order_status

  Request:

  .. code-block:: python

    from bitxchange.spot import Spot

    exchange = Spot(
      key='12345678-1234-1234-1234-123456789012',
      secret='abcdefg-abcdefg-abcdefg'
    )

    params = {
      "orderId": 'sYqFgOK1Q9TV5LAJvxtmiSajirIWPphSWWeXcfGuBQ4='
    }

    x = client.check_order_status(**params)
    print(x)


  Response:

  .. code-block:: bash

    {
    'status': 200,
    'message': 'success',
    'data': 
      {
      'userId': 'F3345gfdfdfgfhjklB5rpC+llY/+4567890+Q0=',
      'firstCurrency': '5df20c3fb6e5c35860023dd3',
      'secondCurrency': '5df20c3fb6e5c35860023dd4',
      'Amount': 1,
      'Price': 0.05917959,
      'Type': 'Sell',
      'Process': 'Pending',
      'Fee': 0.0005918,
      'Total': 0.05917959,
      'wallet': '',
      'ordertype': '2',
      'pair': '60a6c1719f97153d6d65ead0',
      'status': 'active',
      'fee_per': 1,
      'stopprice': 0,
      'partial': False,
      'trade_his': '',
      'tradetime': '',
      'order_no': '',
      'incre_order': '',
      'user_type': 'user',
      'filledAmount': 0,
      'orderDate': '2021-08-13T18:31:22.266Z',
      'orderTime': '2021-08-13T18:31:22.266Z',
      'datetime': '2021-08-13T18:31:22.266Z',
      'updated_at': '2021-08-13T18:31:22.266Z',
      '__v': 0,
      'orderId': 'sYqFgOK1Q9TV5LAJvxtmiSajirIWPphSWWeXcfGuBQ4='
      }
    }

  Expected Error Responses

  .. code-block:: bash

    '>>'

Cancel Active Order
-------------------
.. autofunction:: bitxchange.spot.account.Account.cancel_order

  Request:

  .. code-block:: python

    from bitxchange.spot import Spot

    exchange = Spot(
      key='12345678-1234-1234-1234-123456789012',
      secret='abcdefg-abcdefg-abcdefg'
    )

    params = {
      'orderId': 'sYqFgOK1Q9TV5LAJvxtmiSajirIWPphSWWeXcfGuBQ4='
    }
    x = client.cancel_order(**params)
    print(x)


  Response:

  .. code-block:: bash

    {
    'status': 200,
    'message': 'Order cancelled successfully',
    'currency': 'firstCurrency',
    'balance': 10
    }
  
  Expected Error Responses

  .. code-block:: bash

    {
    'status': 412, 'message': "Order doesn't exists"
    }
