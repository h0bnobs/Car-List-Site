import requests


def ripley(api_key, query, category_ids, gtin=None, charity_ids=None, fieldgroups=None, compatibility_filter=None,
           auto_correct=None, filter=None, sort=None, limit=None, offset=None, aspect_filter=None, epid=None):
    base_url = "https://api.ebay.com/buy/browse/v1/item_summary/search"
    headers = {
        'Authorization': f'Bearer {api_key}',
        'X-EBAY-C-MARKETPLACE-ID': 'EBAY_GB'
        # 'Content-Type': 'application/json',
    }
    params = {
        'q': query,
        'category_ids': category_ids,
        'gtin': gtin,
        'charity_ids': charity_ids,
        'fieldgroups': fieldgroups,
        'compatibility_filter': compatibility_filter,
        'auto_correct': auto_correct,
        'filter': filter,
        'sort': sort,
        'limit': limit,
        'offset': offset,
        'aspect_filter': aspect_filter,
        'epid': epid,
    }

    # Remove None values from params
    params = {k: v for k, v in params.items() if v is not None}

    response = requests.get(base_url, headers=headers, params=params)
    #print((base_url + str(headers) + str(params)))
    # print(str(base_url) + str(headers) + str(params))
    # print(base_url + str(headers) + str(params))
    # print(response.json())
    return response.json()

    # if response.status_code == 200:
    #     return response.json()
    # else:
    #     response.raise_for_status()


# Replace 'YOUR_API_KEY' with your actual eBay API key
# inputfile = open('ebay_api_key')
# ebay_api_key = inputfile.read()
# query = 'subaru impreza wrx'
# category_ids = '9801'  # Category ID for Cell Phones & Smartphones
# limit = 10  # Limit the results to 5 items
#
# result = ripley(ebay_api_key, query, category_ids, limit=limit)

# Print the search results
# for item in result['itemSummaries']:
#     print(f"Title: {item['title']}")
#     print(f"Price: {item['price']['value']} {item['price']['currency']}")
#     print(f"Item Web URL: {item['itemWebUrl']}")
#     print("-" * 40)
