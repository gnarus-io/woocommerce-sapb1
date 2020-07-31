from dotenv import load_dotenv
from sapb1 import SAPB1Adaptor
from woocommerce import API
import os

load_dotenv()

sapb1Adaptor = SAPB1Adaptor()

wcapi = API(
    url=os.getenv('WOOURL'),
    consumer_key=os.getenv('WOOKEY'),
    consumer_secret=os.getenv('WOOSECRET'),
    version="wc/v3"
)

orders = wcapi.get('orders').json()

order = {
    'doc_due_date': None,
    'card_code': None,
    'billto_firstname': orders[0]['billing']['first_name'],
    'billto_lastname': orders[0]['billing']['last_name'],
    'expenses_freightname': None,
    'expenses_linetotal': None,
    'expenses_taxcode': None,
    'discount_percent': None,
    'transport_name': None,
    'payment_method': orders[0]['payment_method'],
    'fe_order_id': None,

    'billto_email': orders[0]['billing']['email'],
    'billto_city': orders[0]['billing']['city'],
    'billto_country':  orders[0]['billing']['country'],
    'billto_state': orders[0]['billing']['state'],
    'billto_address': orders[0]['billing']['address_1'] + "\n" + orders[0]['billing']['address_2'],
    'billto_zipcode': orders[0]['billing']['postcode'],
    'shipto_city': orders[0]['shipping']['city'],
    'shipto_country': orders[0]['shipping']['country'],
    'shipto_state': orders[0]['shipping']['state'],
    'shipto_address': orders[0]['shipping']['address_1'] + "\n" + orders[0]['shipping']['address_2'],
    'shipto_zipcode': orders[0]['billing']['postcode'],
    'items': []
}

for line_item in orders[0]['line_items']:
    item = {
        'itemcode': line_item['sku'],
        'quantity': line_item['quantity'],
        'price': line_item['price'],
        'taxcode': line_item['tax_class'],
        'linetotal': line_item['total']
    }
    order['items'].append(item)

print(order)
# sapb1Adaptor.insertOrder()
