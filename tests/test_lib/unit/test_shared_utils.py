import pytest

from bitxchange.lib.shared_utils import remove_none_values
from bitxchange.lib.shared_utils import check_required_parameter
from bitxchange.lib.shared_utils import validate_target_pair


passing_targets = [
    "BTC_ETH",
    "ETH_BTC",
    "BTC_USDX"
]

failing_targets = [
    "TC_ETH",
    "TH_BTC",
    "TC_USDX"
]

available_pairs = {
    "combinations": [
        "BTC_ETH",
        "ETH_BTC",
        "BTC_USDX"
    ]
}

mandatory_params = {
    "example_1",
    "example_2",
    "example_3"
}

class TestSharedUtils():


    def test_passing_remove_none_values_case_1(self):
        """
            shared_utils.remove_none_values(<valid dict>)
            should return valid dict with no None values
        """
        # GIVEN I have a k, v dictionary that I would like to send to the api
        # WHEN I pass that to the remove_none_values function for validation
        # THEN I am returnd a k, v dict with no None values

        complete_passing_dict = {
        "example_1": "pass",
        "example_2": "pass",
        "example_3": "pass"
        }

        case = remove_none_values(complete_passing_dict)
        expected_results = {
            'example_1': 'pass',
            'example_2': 'pass',
            'example_3': 'pass'
        }

        assert case == expected_results

    def test_passing_remove_none_values_case_2(self):
        """
            shared_utils.remove_none_values(<valid dict>)
            should return valid dict with no None values
        """
        # GIVEN I have a k, v dictionary that I would like to send to the api
        # WHEN I pass that to the remove_none_values function for validation
        # THEN I am returnd a k, v dict with no None values

        none_value_passing_dict = {
            "example_1": "pass",
            "example_2": "pass",
            "example_3": None
        }

        case = remove_none_values(none_value_passing_dict)
        expected_results = {
            'example_1': 'pass',
            'example_2': 'pass'
        }

        assert case == expected_results

    def test_passing_check_required_parameter_kwargs_case_1(self):
        """
            shared_utils.check_required_param(<**kwargs>)
            should return validate all keys have values if successful
            None is returned,    if unsuccessful ParameterRequiredError raised
        """
        # GIVEN I have a k, v dictionary that I want to pass to the exchnage api
            # AND there are NO mandatory fields
        # WHEN I pass dict to the check_required_parameter for validation
        # THEN a None value is return when successful or a tuple of missing values

        passing_dict = {
            "example_1": "pass",
            "example_2": "pass",
            "example_3": "pass"
        }

        case = check_required_parameter(**passing_dict)
        assert case == None

    def test_passing_check_required_parameter_kwargs_case_2(self):
        """
            shared_utils.check_required_param(<**kwargs>)
            should return validate all keys have values if successful
            None is returned, if unsuccessful ParameterRequiredError raised
        """
        # GIVEN I have a k, v dictionary that I want to pass to the exchnage api
            # AND there are NO mandatory fields
        # WHEN I pass dict to the check_required_parameter for validation
        # THEN a None value is return when successful or a tuple of missing values

        passing_dict = {
            "example_1": "pass",
            "example_2": "pass",
            "example_3": "pass"
        }

        case = check_required_parameter(mandatory_params, **passing_dict)
        assert case == None

    def test_failing_check_required_parameter_kwargs_case_3(self):
        """
            shared_utils.check_required_param(<**kwargs>)
            should return validate all keys have values if successful
            None is returned, if unsuccessful ParameterRequiredError raised
        """
        # GIVEN I have a k, v dictionary that I want to pass to the exchnage api
            # AND there are NO mandatory fields
        # WHEN I pass dict to the check_required_parameter for validation
        # THEN a None value is return when successful or a tuple of missing values

        passing_dict = {
            "example_1": "pass",
            "example_2": "pass"
        }

        with pytest.raises(ValueError) as error:
            check_required_parameter(mandatory_params, **passing_dict)

        assert str(error.value) == "Following fields are missing as attributes: example_3"

    @pytest.mark.parametrize('target', passing_targets)
    def test_passing_validate_target_pair_case_1(self, target):
        """
            shared_utils.validate_target_pair(<target_pair>, <available_pairs>)
            should take target and all pairs available dict and then validate that the target
            is a valid and available trading pair.
        """
        # GIVEN I have a valid target pair
        # WHEN I pass that target to the validator to check if it is a valid and active pair
        # THEN I should have the target pair returned to me as a string without any errors

        case = validate_target_pair(target, available_pairs)
        assert case == target

    @pytest.mark.parametrize('target', failing_targets)
    def test_failing_validate_target_pair_case_1(self, target):
        """
            shared_utils.validate_target_pair(<target_pair>, <available_pairs>)
            should take target and all pairs available dict and then validate that the target
            is a valid and available trading pair.
        """
        # GIVEN I have an invalid valid target pair
        # WHEN I pass that target to the validator to check if it is a valid and active pair
        # THEN I should have tan error returned telling me the pair I chose is not a valid pair.

        with pytest.raises(ValueError, match=f"{target} is not a valid trading pair"):
            validate_target_pair(target, available_pairs)
