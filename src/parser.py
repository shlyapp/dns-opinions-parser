from typing import List
import requests
import math
from marshmallow_dataclass import class_schema
from bs4 import BeautifulSoup
import re
from seleniumbase import Driver
from urllib.parser import quote
from typing import List

from schemas import Opinion
from config import get_data_json, headers


def get_id_products(search: str) -> List[int]:
    url = "https://www.dns-shop.ru/search/?q={0}&p={1}".format(quote(search), quote("1"))

    driver = Driver(uc=True)
    driver.get(url)

    response = driver.page_source
    soup = BeautifulSoup(response, "html.parser")
    pages = soup.find_all("li", {"class": "pagination-widget__page",
                                "data-role": "pagination-page"})

    pages = int(pages[-1]['data-page-number'])
    product_id = []

    for page in range(1, pages):
        url = "https://www.dns-shop.ru/search/?q={0}&p={1}".format(quote(search), quote(str(page)))
        soup = BeautifulSoup(response, "html.parser")
        products = soup.find_all("div", {"data-id": "product",
                                        "class": "catalog-product ui-button-widget"})

        for product in products:
            product_id.append(product['data-product'])

    return product_id


def get_opinions(id: int) -> List[Opinion]:
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
