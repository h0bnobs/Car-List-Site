import json
import datetime
from ebaysdk.finding import Connection as finding  # install with pip
from bs4 import BeautifulSoup  # install with pip
from ebayapi import ebayapi  # My API key


def get_kw():
    with open("ebay_search.txt", "r") as f:
        lines = f.readlines()
    Keywords = [line.strip() for line in lines]
    return Keywords

def get_items(keyword):
    # Define the API endpoint and parameters
    endpoint = 'https://api.ebay.com/buy/browse/v1/item_summary/search'
    category_id = '9800'  # eBay category ID for cars
    params = {
        'q': keyword,
        'category_ids': category_id,
        'limit': 30  # You can adjust the limit as needed
    }

    headers = {
        'Authorization': f'Bearer MaxBaldo-carproj-PRD-05ebc3657-823efe7c',
        'Content-Type': 'application/json'
    }

    response = requests.get(endpoint, headers=headers, params=params)

    if response.status_code == 200:
        items = response.json().get('itemSummaries', [])
        print("API call successful. Number of items found:", len(items))
        return items
    else:
        print(f"API call failed. Status code: {response.status_code}")
        print(response.json())
        return []


# def get_items(Keywords):
#     api = finding(appid=ebayapi, siteid='EBAY-GB', config_file=None)  # change country with 'siteid='
#     api_request = {'keywords': Keywords, 'outputSelector': 'SellerInfo'}
#     response = api.execute('findItemsByKeywords', api_request)
#     soup = BeautifulSoup(response.content, 'lxml')
#     items = soup.find_all('item')
#     print("API call successful. Number of items found:", len(items))
#     return items


def res_print(items):
    for item in items:
        try:
            price = int(round(float(item.currentprice.string)))
            if price >= 1000:
                cat = item.categoryname.string.lower()
                title = item.title.string.lower().strip()
                url = item.viewitemurl.string.lower()
                seller = item.sellerusername.text.lower()
                listingtype = item.listingtype.string.lower()

                print("Category:", cat)
                print("Title:", title)
                print("Price: £", price)
                print("URL:", url)
                print("Seller:", seller)
                print("Listing Type:", listingtype)
                print("*" * 20)
        except Exception as e:
            print("Error processing item:", e)


def wr_json(items):
    tdat = {}
    idat = {}
    with open(ebay_results, "a+") as json_file:
        for item in items:
            try:
                price = int(round(float(item.currentprice.string)))
                if price >= 1000:
                    idat["cat"] = item.categoryname.string.lower()
                    idat["title"] = item.title.string.lower().strip()
                    idat["price"] = price
                    idat["url"] = item.viewitemurl.string.lower()
                    idat["seller"] = item.sellerusername.text.lower()
                    tdat.update(idat)
                    json.dump(tdat, json_file)
                    json_file.write('\n')
            except Exception as e:
                print("Error writing item to JSON:", e)


def read_json():
    try:
        with open(ebay_results) as json_file:
            data = json_file.read()
        print(data)
    except Exception as e:
        print("Error reading JSON file:", e)


####################### main ##########################

today = str(datetime.date.today())
ebay_results = 'ebay_results-' + today + '.json'

Keywords = get_kw()  # text file in same dir - one search term per line

for i in range(len(Keywords)):
    print("Processing keyword:", Keywords[i])
    items = get_items(Keywords[i])
    wr_json(items)
    res_print(items)  # Display filtered items

read_json()  # Appends at moment, may make new one, with date/time in filename.
