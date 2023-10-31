from typing import List
import requests
import math
from marshmallow_dataclass import class_schema

from schemas import Opinion
from config import get_data_json, headers


def get_opinions() -> List[Opinion]:
    session = requests.Session()
    response = session.post(
            url='https://www.dns-shop.ru/opinion/opinions/get/',
            data=get_data_json(),
            headers=headers)

    data = response.json()

    if response.status_code != 200 or data["result"] == False:
        return []

    total_opinions = data.get("data").get("totalCount")
    response_count = math.ceil(total_opinions / 10)
    opinions = []

    for i in range(response_count):
        offset = i * 10
        response = session.post(
            url='https://www.dns-shop.ru/opinion/opinions/get/',
            data=get_data_json(offset=offset),
            headers=headers).json()

        opinions_data = response.get("data").get("opinions")

        for opinion_data in opinions_data:
            schema = class_schema(Opinion)()
            opinion = schema.load(opinion_data)
            opinions.append(opinion)

    return opinions
