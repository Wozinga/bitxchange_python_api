# Bitxchange Python API Library
[![Python 3.6](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/release/python-360/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This is a lightweight library that works as a connector to [Bitxchange public API](read_the_docs_url)


## Installation

```bash
pip install bitxchange-python-api
```

## Documentation

[https://readthedocs.org](https://readthedocs.org)

## RESTful APIs

Usage examples:
```python
from bitxchange.spot import Spot

exchange = Spot(key='<api_key ', secret='api_secret')

params = {
    "amount": 1,
    "price": 0.05917959,
    "pair": "BTC/ETH",
    "order_type": 2,
    "type": "sell"
}

order = client.create_order(**params)

print(order)
```
Please find `examples` folder to check for more endpoints.

### Base URL

If `base_url` is not provided, it defaults to `https://exchangeapi.bit-xchange.co`.<br/>
It's recommended to pass in the `base_url` parameter.

## Test Case

```python
# In case packages are not installed yet
pip install pytest

cd tests pytest
```
