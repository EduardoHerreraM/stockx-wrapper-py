from stockx_wrapper.stockx import Stockx


def main():
    stockx = Stockx()

    data = stockx.search_products('Jordan 1 low elephan')
    stockx.search_products_new_api('Jordan 1 low elephan')
    data = stockx.get_product_specific_size(product_id=data['id'], size='9')
    stockx.get_product_data(product_id=data['id'], country='ES', currency='EUR', output_keys=['market'])


if __name__ == "__main__":
    main()
