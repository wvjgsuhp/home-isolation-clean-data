from typing import Any, Dict, List

import json

from model import process_addresses


def assert_list_of_str(obj: Dict[str, Any], key: str) -> None:
    simple_assert(obj, 'Other', list)
    a_list: List[Any] = obj.get(key)
    for element in a_list:
        found_type = type(element)
        error_message = f'`{key}` must be {List[str]}, but got {List[found_type]}'
        assert isinstance(element, str), error_message

def simple_assert(obj: Dict[str, Any], key: str, expected_type: type) -> None:
    value = obj.get(key)
    error_message = f'`{key}` must be {expected_type}, but got {type(value)}'
    assert isinstance(value, expected_type), error_message

def main() -> None:
    with open("sample.json", "r") as f:
        sample: List[Dict[str, Any]] = json.load(f);

    sample = sample[:10];
    output = process_addresses(sample);

    # fields and type checking
    for idx, item in enumerate(output):
        assert len(set(item.keys()) - {
            "id", "HouseNumber", "PremiseName", "Moo", "SubStreetName",
            "StreetName", "SubDistrict", "District", "Province", "PostalCode",
            "Other"
        }) == 0, f"Invalid keys: {list(item.keys())} on index {idx}"
        simple_assert(item, 'id', int)
        simple_assert(item, 'PostalCode', str)
        simple_assert(item, 'Moo', str)
        assert_list_of_str(item, 'Other')


if __name__ == "__main__":
    main();
