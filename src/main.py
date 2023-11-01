import asyncio
from parser import gather_data, get_opinions
from time import time
from datetime import datetime

def main():
    products = []

    with open("data", "r") as file:
        for line in file:
            products.append(line.rstrip())

    
    start_time = datetime.now()
    product_id = products[0]
    asyncio.run(gather_data(product_id))
    # get_opinions(product_id)
    end_time = datetime.now()
    execution_time = end_time - start_time
    print(execution_time)

            
if __name__ == "__main__":
    main()
