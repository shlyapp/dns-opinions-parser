from typing import List
import requests
import math
from marshmallow_dataclass import class_schema
from bs4 import BeautifulSoup
from seleniumbase import Driver
from urllib.request import quote
from typing import List
import aiohttp
import asyncio

from asyncio_throttle import Throttler

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

    for page in range(0, pages + 1):
        url = "https://www.dns-shop.ru/search/?q={0}&p={1}".format(quote(search), quote(str(page)))
        soup = BeautifulSoup(response, "html.parser")
        products = soup.find_all("div", {"data-id": "product",
                                        "class": "catalog-product ui-button-widget"})
        
        for product in products:
            product_id.append(product['data-product'])

    return product_id


def get_response_count(id: str) -> int:
    session = requests.Session()
    response = session.post(
            url='https://www.dns-shop.ru/opinion/opinions/get/',
            data=get_data_json(object_id=id),
            headers=headers)

    data = response.json()

    if response.status_code != 200 or data["result"] == False:
        return 0

    total_opinions = data.get("data").get("totalCount")
    response_count = math.ceil(total_opinions / 10)

    return response_count


def get_opinions(id: str):
    response_count = get_response_count(id)
    session = requests.Session()
    opinions = [] 

    for i in range(response_count):
        response = session.post(url="https://www.dns-shop.ru/opinion/opinions/get/",
                data=get_data_json(object_id=id,
                                   offset=i*10),
                headers=headers).json()

        if response["result"] == False:
            return
    
        opinions_data = response.get("data").get("opinions")
            
        if opinions_data is None:
            return
           
        for opinion_data in opinions_data:
            schema = class_schema(Opinion)()
            opinion = schema.load(opinion_data)
            opinions.append(opinion)

    return opinions


async def get_opinions_async(session, id: str, offset: int, throrrler):
    opinions = []
    async with throrrler:
        async with session.post(url="https://www.dns-shop.ru/opinion/opinions/get/",
                                data=get_data_json(object_id=id,
                                offset=offset),
                                headers=headers) as response:
            response = await response.json()

            if response["result"] == False:
                return
    
            opinions_data = response.get("data").get("opinions")
            
            if opinions_data is None:
                return
           
            for opinion_data in opinions_data:
                schema = class_schema(Opinion)()
                opinion = schema.load(opinion_data)
                opinions.append(opinion)

    return opinions
       

async def gather_data(id: str):
    response_count = get_response_count(id)
    tasks = []
    throttler = Throttler(rate_limit=22, period=1)
    async with aiohttp.ClientSession() as session:
        for i in range(response_count):
            task = asyncio.create_task(get_opinions_async(session, id, i * 10, throttler))
            tasks.append(task)
        
        await asyncio.gather(*tasks)
