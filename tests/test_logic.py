from stockx_wrapper.stockx import Stockx


def main():
    stockx = Stockx()

    data = stockx.products.search_products('Jordan 1 low elephan')
    stockx.products.search_products_new_api('Jordan 1 low elephan')
    data = stockx.products.get_product_specific_size(product_id=data['id'], size='9')
    stockx.products.get_product_data(product_id=data['id'], country='ES', currency='EUR', output_keys=['market'])
    stockx.products.prices.get_product_price_data(product_id=data['id'], country='ES', currency='EUR')


if __name__ == "__main__":
    main()
