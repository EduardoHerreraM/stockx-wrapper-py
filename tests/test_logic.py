from stockx_wrapper.stockx import Stockx


def main():
    stockx = Stockx()

    product = stockx.products.search_products('Jordan 1 low elephant ', more_data=True)[0]
    product_size = product.get_specific_size(size='9')
    price_chart = product_size.prices.get_price_chart_data(country='ES', currency='EUR')
    prices_sold = product_size.prices.get_price_sold_data(number_of_items=510, country='ES', currency='EUR')
    stockx.products.search_products_new_api('Jordan 1')


if __name__ == "__main__":
    main()
