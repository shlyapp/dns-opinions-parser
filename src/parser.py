from typing import List
import requests
import math
from marshmallow_dataclass import class_schema
from bs4 import BeautifulSoup
import re

from schemas import Opinion
from config import get_data_json, headers, cookies


def get_product_id(url: str):
    response = requests.get(
        url=url,
        cookies=cookies,
        headers=headers,
    )

    if response.status_code != 200:
        print("[ERROR] Не удается получить соддержимое сайта.")
        return -1

    soup = BeautifulSoup(response.text, "html.parser")
    script_tag = soup.find("script", text=re.compile(r'window.cardMicrodataUrl = \'/product/microdata/[^/]+/\';'))

    if script_tag:
        match = re.search(r'window.cardMicrodataUrl = \'/product/microdata/([^/]+)/\';', script_tag.string)
        if match:
            value = match.group(1)
            return value
    
    return -1


def get_opinions(url: str) -> List[Opinion]:
    id = get_product_id(url)

    if id == -1:
        return

    session = requests.Session()
    response = session.post(
            url='https://www.dns-shop.ru/opinion/opinions/get/',
            data=get_data_json(object_id=id),
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
            data=get_data_json(object_id=id,
                               offset=offset),
            headers=headers).json()

        opinions_data = response.get("data").get("opinions")

        for opinion_data in opinions_data:
            schema = class_schema(Opinion)()
            opinion = schema.load(opinion_data)
            opinions.append(opinion)

    return opinions
