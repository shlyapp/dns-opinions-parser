from typing import Dict


def get_data_json(is_real_buyer: bool = False, has_photos: bool = False, offset: int = 0) -> Dict:
    data = {"objectTypeId": "610d4c8e-37fc-416c-a603-bce518d57c15",
        "objectId": "a75387d5-ac97-11e6-83a6-00155d03330d",
        "isRealBuyer": int(is_real_buyer),
        "hasPhotos": int(has_photos),
        "sort": 0,
        "offset": offset,
        "limit": 10,
        "onlyObjectOpinions": 0
        }

    # data = {"objectTypeId": "610d4c8e-37fc-416c-a603-bce518d57c15",
    #     "objectId": "a75387d5-ac97-11e6-83a6-00155d03330d",
    #     "isRealBuyer": 1,
    #     "hasPhotos": 1,
    #     "sort": 0,
    #     "offset": offset,
    #     "limit": 10,
    #     "onlyObjectOpinions": 0
    #     }
    
    return data


headers = {
        'x-requested-with': 'xmlhttprequest',
        'user-agent': 'mozilla/5.0 (windows nt 10.0; win64; x64; rv:70.0) gecko/20100101 firefox/70.0'
        }


