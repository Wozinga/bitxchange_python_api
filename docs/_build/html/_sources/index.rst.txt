.. Bitxchange Python API Library documentation master file, created by
   sphinx-quickstart on Thu Aug 12 00:27:56 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Bitxchange Python API Library's documentation!
=========================================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   /intro/getting-started-api
   /changelog



.. role:: raw-html-m2r(raw)
   :format: html


Bitxchange Python API Library
===================================


.. image:: https://img.shields.io/badge/python-3.6+-blue.svg
   :target: https://www.python.org/downloads/release/python-360/
   :alt: Python 3.6


.. image:: https://img.shields.io/badge/License-MIT-yellow.svg
   :target: https://opensource.org/licenses/MIT
   :alt: License: MIT

This is the offical lightweight python library to connect to the Bitxchange public API.
* Source Code: `Bitxchange API Library <https://github.com/Wozinga/bitxchange_python_api>`_

* Source Code: https://github.com/Wozinga/bitxchange_python_api
* Official API document:

  * https://<read the docs>
  * https://https://github.com/Wozinga/bitxchange_python_api

* Support channels:

  * Telegram Channel: https://t.me/bitxchange_developer_support

* API key setup: <how to setup API docs>


Quick Start
-----------

Installation
^^^^^^^^^^^^

* Install via package name

  .. code-block:: bash

     pip install bitxchange-python-api

* Alternatively, install with git repository path

  .. code-block:: bash

    python -m pip install git+https://github.com/Wozinga/bitxchange_python_api.git


Usage Example
-------------

RESTful APIs
^^^^^^^^^^^^

.. code-block:: python

    from bitxchange.spot import Spot

    exchange = Spot()

    print('All trading pairs')
    print(exchange.available_trading_pairs(), '\n')

    print('All market tickers')
    print(exchange.all_market_ticker(), '\n')



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`