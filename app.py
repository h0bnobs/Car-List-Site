import sys

from flask import Flask, render_template
from ripley import ripley

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
    category_ids = '9801'  # Category ID for Cell Phones & Smartphones
    limit = 100  # Limit the results to 5 items
    filter = 'buyingOptions:{AUCTION|FIXED_PRICE|BEST_OFFER|CLASSIFIED_AD}'  #

    print("https://api.ebay.com/buy/browse/v1/item_summary/search?q=" + query + "&category_ids=" +
          category_ids + "&filter=" + filter + "&limit=" + str(limit))

    result = ripley(api_key, query, category_ids, filter=filter, limit=limit)
    #print("result " + str(result))
    # print(result['total'])

    items = []
    auctions = []
    fixed_price = []  # buy it now!
    classified_ad = []
    auction_with_fixed_price = []  # AUCTION and FIXED_PRICE. Before the auction listing has received a qualifying bid.
    fixed_price_with_best_offer = []

    if 'itemSummaries' in result:
        for item in result['itemSummaries']:
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
