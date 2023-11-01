from typing import Dict


def get_data_json(object_id: int, is_real_buyer: bool = False, has_photos: bool = False, offset: int = 0) -> Dict:
    data = {"objectTypeId": "610d4c8e-37fc-416c-a603-bce518d57c15",
        "objectId": object_id,
        "isRealBuyer": int(is_real_buyer),
        "hasPhotos": int(has_photos),
        "sort": 0,
        "offset": offset,
        "limit": 10,
        "onlyObjectOpinions": 0
        }

    return data


headers = {
        'x-requested-with': 'xmlhttprequest',
        'user-agent': 'mozilla/5.0 (windows nt 10.0; win64; x64; rv:70.0) gecko/20100101 firefox/70.0'
        }

cookies = {
    'lang': 'ru',
    '_gid': 'GA1.2.1317012125.1698812293',
    '_gcl_au': '1.1.1334288358.1698812293',
    'phonesIdentV2': 'fc51d2bb-c25d-423f-b42c-a47d78760f95',
    'rrpvid': '223344124656938',
    'cartUserCookieIdent_v3': 'c4e4f6d61016a7aa4e0c659462600c43742c995e704278c87e4deb7017bf893ea%3A2%3A%7Bi%3A0%3Bs%3A22%3A%22cartUserCookieIdent_v3%22%3Bi%3A1%3Bs%3A36%3A%22967ebed4-7015-32fe-ae01-4b753c6c539d%22%3B%7D',
    'rcuid': '6541d186f56769610a9a5873',
    '_ab_': '%7B%22search-sandbox%22%3A%22new_specs%22%7D',
    'tmr_lvid': '8c8e45543c5ecdd85efaff27b9c7391b',
    'tmr_lvidTS': '1698812293093',
    '_ym_uid': '1698812293352279814',
    '_ym_d': '1698812293',
    '_ym_isad': '2',
    'city_path': 'izhevsk',
    'current_path': 'c4008ac1318a0ec4a9ac427a95d8b7b7098b183c4f98cd760c966e92cef7ed2fa%3A2%3A%7Bi%3A0%3Bs%3A12%3A%22current_path%22%3Bi%3A1%3Bs%3A115%3A%22%7B%22city%22%3A%22c5073532-0f65-11e0-ae93-001517c526f0%22%2C%22cityName%22%3A%22%5Cu0418%5Cu0436%5Cu0435%5Cu0432%5Cu0441%5Cu043a%22%2C%22method%22%3A%22manual%22%7D%22%3B%7D',
    'PHPSESSID': '92567be0840296e7d58be65593039d27',
    '_csrf': 'ebb99ee97541d49901b11e940af27cdfc167130656c7264bd93e8c2d89516e3ca%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22dYav19o3hzTgjYqoD2C2aDA2dSEt3XAm%22%3B%7D',
    'cookieImagesUploadId': 'a9c190c472ad3c624f43798301cad71d243a4c5cfd4c4b3471b07e9ad03056daa%3A2%3A%7Bi%3A0%3Bs%3A20%3A%22cookieImagesUploadId%22%3Bi%3A1%3Bs%3A36%3A%2213e2863e-3b5c-4cc1-bc58-6fe0e650457d%22%3B%7D',
    'qrator_jsr': '1698822434.528.FvjcEUExt66D6Sum-47t9fjv873kndj2jua4tou5d70su2gmt-00',
    'qrator_jsid': '1698822434.528.FvjcEUExt66D6Sum-pj8h1q9l7g44irevuffa3mlqcmj48qpj',
    'rr-testCookie': 'testvalue',
    '_gat': '1',
    '_gat_%5Bobject%20Object%5D': '1',
    '_ga': 'GA1.1.603270105.1698812293',
    '_ym_visorc': 'b',
    '_ga_FLS4JETDHW': 'GS1.1.1698819280.2.1.1698822435.59.0.0',
    'tmr_detect': '0%7C1698822437109',
}

headers_list = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    # 'Cookie': 'lang=ru; _gid=GA1.2.1317012125.1698812293; _gcl_au=1.1.1334288358.1698812293; phonesIdentV2=fc51d2bb-c25d-423f-b42c-a47d78760f95; rrpvid=223344124656938; cartUserCookieIdent_v3=c4e4f6d61016a7aa4e0c659462600c43742c995e704278c87e4deb7017bf893ea%3A2%3A%7Bi%3A0%3Bs%3A22%3A%22cartUserCookieIdent_v3%22%3Bi%3A1%3Bs%3A36%3A%22967ebed4-7015-32fe-ae01-4b753c6c539d%22%3B%7D; rcuid=6541d186f56769610a9a5873; _ab_=%7B%22search-sandbox%22%3A%22new_specs%22%7D; tmr_lvid=8c8e45543c5ecdd85efaff27b9c7391b; tmr_lvidTS=1698812293093; _ym_uid=1698812293352279814; _ym_d=1698812293; _ym_isad=2; city_path=izhevsk; current_path=c4008ac1318a0ec4a9ac427a95d8b7b7098b183c4f98cd760c966e92cef7ed2fa%3A2%3A%7Bi%3A0%3Bs%3A12%3A%22current_path%22%3Bi%3A1%3Bs%3A115%3A%22%7B%22city%22%3A%22c5073532-0f65-11e0-ae93-001517c526f0%22%2C%22cityName%22%3A%22%5Cu0418%5Cu0436%5Cu0435%5Cu0432%5Cu0441%5Cu043a%22%2C%22method%22%3A%22manual%22%7D%22%3B%7D; PHPSESSID=92567be0840296e7d58be65593039d27; _csrf=ebb99ee97541d49901b11e940af27cdfc167130656c7264bd93e8c2d89516e3ca%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22dYav19o3hzTgjYqoD2C2aDA2dSEt3XAm%22%3B%7D; cookieImagesUploadId=a9c190c472ad3c624f43798301cad71d243a4c5cfd4c4b3471b07e9ad03056daa%3A2%3A%7Bi%3A0%3Bs%3A20%3A%22cookieImagesUploadId%22%3Bi%3A1%3Bs%3A36%3A%2213e2863e-3b5c-4cc1-bc58-6fe0e650457d%22%3B%7D; qrator_jsr=1698822434.528.FvjcEUExt66D6Sum-47t9fjv873kndj2jua4tou5d70su2gmt-00; qrator_jsid=1698822434.528.FvjcEUExt66D6Sum-pj8h1q9l7g44irevuffa3mlqcmj48qpj; rr-testCookie=testvalue; _gat=1; _gat_%5Bobject%20Object%5D=1; _ga=GA1.1.603270105.1698812293; _ym_visorc=b; _ga_FLS4JETDHW=GS1.1.1698819280.2.1.1698822435.59.0.0; tmr_detect=0%7C1698822437109',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}
