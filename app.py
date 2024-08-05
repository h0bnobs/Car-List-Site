import sys

from flask import Flask, render_template
from ripley import EbayClient
from ripley import create_parameter_dict

app = Flask(__name__)


# TODO: need to figure out why im only getting a few responses, while when searching on ebay website, i get way more
# TODO: rough insurance quote on site?
# TODO: HPI check/car reg check also on site?
# TODO: filter ebay listings by auction, buy it now and both.
@app.route('/')
def index():
    inputfile = open('ebay_api_key')
    api_key = inputfile.read()

    query = 'Ford+Fiesta'
    category_ids = '9801'
    limit = '100'
    filter = 'buyingOptions:{AUCTION|FIXED_PRICE|BEST_OFFER|CLASSIFIED_AD}'

    print("https://api.ebay.com/buy/browse/v1/item_summary/search?q=" + query + "&category_ids=" +
          category_ids + "&filter=" + filter + "&limit=" + str(limit))

    ebay_client = EbayClient(api_key=api_key, query=query)
    result = ebay_client.make_request(create_parameter_dict(query=query, category_ids=category_ids,
                                                            limit=limit, filter=filter))

    items = []

    if 'itemSummaries' in result:
        for item in result['itemSummaries']:
            # match item['buyingOptions']:
            #     case item['buyingOptions'].get('AUCTION'):
            #         image_url = item['image']['imageUrl'] if 'image' in item else 'No image available'
            #         items.append({
            #             'title': item['title'],
            #             'cat': 'Cars',
            #             'price': item.get('currentBidPrice', {}).get('value', 'N/A'),
            #             'seller': item.get('seller', {}).get('username', 'Unknown'),
            #             'url': item['itemWebUrl'],
            #             'image': image_url,
            #         })
            #     case item['buyingOptions'].get('CLASSIFIED_AD'):
            #         # Check if 'thumbnailImages' is a list and has elements
            #         if 'thumbnailImages' in item and isinstance(item['thumbnailImages'], list) and len(
            #                 item['thumbnailImages']) > 0:
            #             image_url = item['thumbnailImages'][0]['imageUrl']
            #         else:
            #             image_url = 'No image available'
            #         items.append({
            #             'title': item['title'],
            #             'cat': 'Cars',
            #             'price': item['price']['value'],
            #             'seller': item.get('seller', {}).get('username', 'Unknown'),
            #             'url': item['itemWebUrl'],
            #             'image': image_url,
            #         })
            #     case _:
            #         print(f"Listing type not found within the list of listings")

            #print("Item:", item)  # Print each item for debugging
            if 'AUCTION' in item['buyingOptions']:
                image_url = item['image']['imageUrl'] if 'image' in item else 'No image available'
                items.append({
                    'title': item['title'],
                    'cat': 'Cars',
                    'price': item.get('currentBidPrice', {}).get('value', 'N/A'),
                    'seller': item.get('seller', {}).get('username', 'Unknown'),
                    'url': item['itemWebUrl'],
                    'image': image_url,
                })
            elif 'CLASSIFIED_AD' in item['buyingOptions']:
                # Check if 'thumbnailImages' is a list and has elements
                if 'thumbnailImages' in item and isinstance(item['thumbnailImages'], list) and len(
                        item['thumbnailImages']) > 0:
                    image_url = item['thumbnailImages'][0]['imageUrl']
                else:
                    image_url = 'No image available'
                items.append({
                    'title': item['title'],
                    'cat': 'Cars',
                    'price': item['price']['value'],
                    'seller': item.get('seller', {}).get('username', 'Unknown'),
                    'url': item['itemWebUrl'],
                    'image': image_url,
                })
    return render_template('index2.html', items=items)


if __name__ == '__main__':
    app.run(debug=True)
