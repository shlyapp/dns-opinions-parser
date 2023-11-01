from parser import get_product_id, get_opinions


def main():
    url ="https://www.dns-shop.ru/product/bf41006e0b2fed20/videokarta-palit-geforce-rtx-4060-dual-ne64060019p1-1070d/"
    id = get_product_id(url)

    if id == -1:
        print("Not find id")

    opinions = get_opinions(id)
    print(opinions[0].plus)

if __name__ == "__main__":
    main()
