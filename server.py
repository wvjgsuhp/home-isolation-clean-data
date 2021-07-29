from typing import Dict, List, Union

from flask import Flask, request, abort, jsonify

from model import process_addresses

app: Flask = Flask(__name__);


@app.route("/api/format_addresses", methods=["POST"])
def format_address() -> List[Dict[str, Union[str, List[str]]]]:
    """
    Endpoint to format input address. This endpoint call model.process_address
    to format data according to the follow input/output.

    The input JSON is in the following format:

    [
        { "id": <address-id: int>, "address": <input-address: str> },
        ...
    ]

    The expected return JSON must be in the following format

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
    # if JSON not presence when POST request, return error code 400
    if not request.json:
        abort(400);
    
    addresses: dict = request.json;  # get request JSON
    formatted_addresses: dict = process_addresses(addresses);  # process requested JSON

    return jsonify(formatted_addresses);


def main() -> None:
    app.run(debug=True, host="0.0.0.0", port=9000);


if __name__ == "__main__":
    main();
