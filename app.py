import requests
from flask import Flask, render_template
import json
import datetime
from ebaysdk.finding import Connection as finding  # install with pip
from bs4 import BeautifulSoup  # install with pip
from ebayapi import ebayapi  # My API key

app = Flask(__name__)


# Functions from your provided code
def get_kw():
    with open("ebay_search.txt", "r") as f:
        lines = f.readlines()
    return [line.strip() for line in lines]


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
        'Authorization': f'Bearer v^1.1#i^1#I^3#p^1#r^0#f^0#t^H4sIAAAAAAAAAOVYf2wTVRxft26GwBgyQJ0OyqEQMHe96/Xa3tHWdL/cZrcWWgcMEa9379jR691573XdNOKyIP6IYNQMJSgZgiYEjRJEQBMRTSDGkBBMRNH4hwkEh5igMSRgjHdtGd0kgKyJTew/zfu+7/u+z+fzvt/33j1yoGrSog2tGy5W224rHx4gB8ptNmoyOamq8v6pFeV1lWVkgYNteODeAftgxVk/5FOKzi0FUNdUCBx9KUWFXNYYwNKGymk8lCGn8ikAOSRwsVBHmHMRJKcbGtIETcEcbU0BjGYZkGAE2u2jSYGhPKZVvRIzrpn9pFdyiTQl+GjWR4tusx/CNGhTIeJVFMBcpMuNkx7cxcYphqNozsUSHrevG3N0AQPKmmq6ECQWzMLlsmONAqzXh8pDCAxkBsGCbaGWWCTU1tTcGfc7C2IF8zrEEI/ScGyrUROBo4tX0uD608CsNxdLCwKAEHMGczOMDcqFroC5Bfg5qb0M66XdEsXQgPeJYlGkbNGMFI+uj8OyyCIuZV05oCIZ9d9IUVONxFogoHyr0wzR1uSw/pakeUWWZGAEsOaG0IpQNIoFO/i+Bl4RNVzgDTO/1uLRpU04aWaWQHsYL+5z0UACXiE/Ty5YXuVxEzVqqihbmkFHp4YagAkajJeGLJDGdIqoESMkIQtQoZ93VEJ3t7WmuUVMox7VWlaQMnVwZJs3XoDR0QgZciKNwGiE8R1ZhQIYr+uyiI3vzKZiPnv6YADrQUjnnM5MJkNkaEIz1jhdJEk5l3eEY0IPSPGY5WvVetZfvvEAXM5SEYA5Esoc6tdNLH1mqpoA1DVY0M16GR+T130srOB46z8MBZydYwuiWAXCCjTNMIyX8rAMKXjYYhRIMJ+jTgsHSPD9eIo3kgDpCi8AXDDzLJ0ChixyNCO5aJ8EcNHDSriblSQ8wYgenJIAIAFIJATW9z+qk5vN9BgQDICKk+rFSnO+d7nU3dUZFkS+vYVWwsuQGE1kfCjS1+B5SOfb4x0Nfc2Pd2V6mzKBmy2Ga5JvVGRTmbg5f+nVeqsGERAnRC8maDqIaoos9JfWAtOGGOUN1B8DimIaJkQypOttRdqqi0Xv3+0St0a7iCfUf3M6XZMVtDK2tFhZ46EZgNdlwjp/CEFLOTU+bdU66rHMq7OoJ8RbNq+tJcXaJJljK4u5+yZhUkY9BOwVCANALW2YV20iYt2/4loSqOZxhgxNUYDRRU24nFOpNOITCii1ui5Cgst8iZ21lJdiPV43SbIT4iVkT9LVpbYlFWkntjfewp3aOfYDP1iW/VGDts/JQdun5TYb6Sfvo+aRc6sqHrZXTKmDMgKEzEsElNeo5nerAYgk6Nd52SivLfvtraHWxrrmyOZFT8b7j289Wjal4H1heBV55+gLw6QKanLBcwN5z9WeSqrmjmqXm/S4WIqhaBfbTc672munZtlnzH3jnTOHkp1HZp27ePbZDXvKj9dtaiWrR51stsoy+6CtbP3Cli1HjB+jSeHSnyPPr1R3Ll6y6/DbYfanMqn2dJClPqx9peWujUMIPPPqL8uWXtg7UlMfOLbuxEeZy9P0R2Z/tv2s+7tZxxT/DPv2B07CF86cTnRXbTsM6/f7e/fVnJqz8eSBqWuZacGwb2CKsnPk9k9WTZ8eXUdGuR2RHTs2Jra+OH/219O2rzuyb8/Rl9bvvTDn6GOpj3fbTh34de/wppn1l7+cGTqRXvDU4oOHXq5ntCfaf3+9uX3bez8v8Ca/Pw8vzb87UPP+rvP+RxNfnPMHDny7YuirVQufWeAZ8jv21yaM6s0/PI1/82bvu51h7dhfQeIg9truP55jRnZ94KBXbk4O7nEN9Wx5MLeWfwP5Oa8U+REAAA==',
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
#     api_request = {'keywords': Keywords, 'categoryId': 6001, 'outputSelector': 'SellerInfo'}
#     response = api.execute('findItemsByKeywords', api_request)
#     soup = BeautifulSoup(response.content, 'lxml')
#     items = soup.find_all('item')
#     return items


def wr_json(items):
    tdat = []
    for item in items:
        idat = {}
        idat["cat"] = item.categoryname.string.lower()
        idat["title"] = item.title.string.lower().strip()
        idat["price"] = int(round(float(item.currentprice.string)))
        idat["url"] = item.viewitemurl.string.lower()
        idat["seller"] = item.sellerusername.text.lower()
        tdat.append(idat)

    return tdat


@app.route('/')
def index():
    Keywords = get_kw()
    all_items = []
    for keyword in Keywords:
        items = get_items(keyword)
        all_items.extend(wr_json(items))
    return render_template('index.html', items=all_items)


if __name__ == '__main__':
    app.run(debug=True)
