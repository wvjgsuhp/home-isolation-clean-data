from custom_types import Input, Output

def process_addresses(addresses: Input) -> Output:
    """
    # TODO:
    For contributor, please edit this function as you wish. Just
    to make sure that the output is in the correct format as stated in README
    or in this docstring

    Format input address from requested JSON

    Argument
    --------
    addressses: List[Dict[str, Union[int, str]]]
        input `addresses` variable is in the following format:

        [
            { "id": <address-id: int>, "address": <input-address: str> },
            ...
        ]


    Return
    ------
    formatted_addresses: List[Dict[str, Union[str, List[str]]]]
        Formatted address where the return JSON must be in the following format

        [
            {
                "id": 1,
                "HouseNumber": "174/243",
                "PremiseName": "คอนโดบ้านสวนอยู่นิรันดร์ ตึกB",
                "Moo": "",
                "SubStreetName": "ศรีพรสวรรค์",
                "StreetName": "",
                "SubDistrict": "สวนใหญ่",
                "District": "เมืองนนทบุรี",
                "Province": "นนทบุรี",
                "PostalCode": "",
                "Other": [
                    ...
                ]
            },
            {
                ...
            }
        ]
    """
    ##################################
    # Implement your code here       #
    ##################################
    tmp: Output = [
        {
            "id": 1,
            "HouseNumber": "174/243",
            "PremiseName": "คอนโดบ้านสวนอยู่นิรันดร์ ตึกB",
            "Moo": "",
            "SubStreetName": "ศรีพรสวรรค์",
            "StreetName": "",
            "SubDistrict": "สวนใหญ่",
            "District": "เมืองนนทบุรี",
            "Province": "นนทบุรี",
            "PostalCode": "",
            "Other": []
        }
    ]
    return tmp
