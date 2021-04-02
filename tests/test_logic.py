from stockx_wrapper.stockx import Stockx


def main():
    stockx = Stockx()

    product = stockx.products.search_products('Jordan 1 low elephan')
    product_size = product.get_specific_size(size='9')
    price_chart = product_size.prices.get_product_price_data(country='ES', currency='EUR')


if __name__ == "__main__":
    main()
