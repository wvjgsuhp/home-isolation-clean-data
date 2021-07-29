from typing import Dict, List, Union

import json

from model import process_addresses


def main() -> None:
    with open("sample.json", "r") as f:
        sample: list = json.load(f);

    sample = sample[:10];
    output: list = process_addresses(sample);

    # fields and type checkint
    for idx, item in enumerate(output):
        assert len(set(item.keys()) - {
            "id", "HouseNumber", "PremiseName", "Moo", "SubStreetName",
            "StreetName", "SubDistrict", "District", "Province", "PostalCode",
            "Other"
        }) == 0, f"Invalid keys: {list(item.keys())} on index {idx}"
        assert isinstance(item["id"], int), f"`id` field must be int but got {type(item['id'])}";
        assert isinstance(item["PostalCode"], str), f"`id` field must be str but got {type(item['PostalCode'])}";
        assert isinstance(item["Moo"], str), f"`id` field must be str but got {type(item['Moo'])}";
        assert isinstance(item["Other"], list), f"`Other` field must be List[str] but got {type(item['Other'])}";


if __name__ == "__main__":
    main();
