import pytest

from bitxchange.spot import Spot

_client = Spot()

@pytest.fixture(scope="session")
def client():

    yield _client
