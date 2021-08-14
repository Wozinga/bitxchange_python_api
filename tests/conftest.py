from bitxchange.spot import Spot

import pytest

_client = Spot()

@pytest.fixture(scope="session")
def client():

    yield _client
