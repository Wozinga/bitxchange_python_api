from bitxchange.errors import ParameterRequiredError
from bitxchange.errors import ParameterValueError
from bitxchange.errors import TargetPairError

from typing import Optional, Dict, Any


def remove_none_values(input) -> dict:
    # Removes any empty values from input dict
    resp = {}
    for kw in input.keys():
        if input[kw] is not None:
            resp[kw] = input[kw]
    return resp

def check_required_parameter(mandatory_params=None, **kwargs):
    # checks that all KV attributes are not empty and validates
    # all mandatory args have been met
    
    if mandatory_params:
        missing_params = []
        for param in mandatory_params:

            if param not in kwargs:
                missing_params.append(param)

        if missing_params:
                raise ValueError(
                    f"Following fields are missing as attributes: {','.join(missing_params)}")

    for key, value in kwargs.items():
        if not value:
            raise ParameterRequiredError([key])

def validate_target_pair(target_pair: str, available_pairs: Optional[Dict[str, Any]]=None):


    if not available_pairs:
        from bitxchange.spot import Spot

        spot = Spot()

        available_pairs = spot.available_trading_pairs()

    if target_pair not in available_pairs['combinations']:
        raise ValueError(
            f"{target_pair} is not a valid trading pair"
        ) from None
    else:
        return str(target_pair)
