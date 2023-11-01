from parser import get_product_id, get_opinions


def main():
    url ="https://www.dns-shop.ru/product/bf41006e0b2fed20/videokarta-palit-geforce-rtx-4060-dual-ne64060019p1-1070d/"
    url = "https://www.dns-shop.ru/product/bbd9468ebcb2ed20/156-noutbuk-gigabyte-g5-mf-cernyj/"
    url = "https://www.dns-shop.ru/product/d1a3848c5f26ed20/korpus-cougar-duoface-pro-rgb-cgr-5ad1b-rgb--cernyj/"
    url = "https://www.dns-shop.ru/product/d1a3848c5f26ed20/korpus-cougar-duoface-pro-rgb-cgr-5ad1b-rgb--cernyj/"

    opinions = get_opinions(url)

    if opinions == None:
        return

    for count, opinion in enumerate(opinions):
        try:
            print(opinion.plus + "\n")
        except:
            continue


if __name__ == "__main__":
    main()
