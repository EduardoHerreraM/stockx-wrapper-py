from stockx_wrapper.stockx import Stockx


def main():
    stockx = Stockx()

    product = stockx.products.search_products('Jordan 1 low elephant ', more_data=True)[0]
    product_size = product.get_specific_size(size='9')
    price_chart = product_size.prices.get_price_chart_data(country='ES', currency='EUR')
    prices_sold = product_size.prices.get_price_sold_data(number_of_items=510, country='ES', currency='EUR')
    # stockx.products.search_products_new_api('Jordan 1')
    stockx.products.search_products('Chicago', product_category='sneakers', gender='men', retail_price=['lte-200'],
                                    year=2019, shoe_size='9', market_lowest_ask=['gte-200'], tags=['air jordan', 'one'])
    stockx.products.search_products('Jordan 1', number_of_products=200)


if __name__ == "__main__":
    main()
