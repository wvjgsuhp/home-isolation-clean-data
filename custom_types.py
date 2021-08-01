from typing import List, TypedDict


class RawAddress(TypedDict):
    id: int
    address: str


class ProcessedAddress(TypedDict):
    id: int
    HouseNumber: str
    PremiseName: str
    Moo: str
    SubStreetName: str
    StreetName: str
    SubDistrict: str
    District: str
    Province: str
    PostalCode: str
    Other: List[str]


Input = List[RawAddress]
Output = List[ProcessedAddress]
