import requests as req


class EbayRequestException(Exception):

    def __init__(self, message: str):
        self.message = message

    def __str__(self):
        print(f"Request error whilst fetching listings from the ebay api.")
        return self.message


class EbayClient(object):

    def __init__(self, api_key: str, query: str):
        """
        Basic client object for fetching from the ebay api.
        :param api_key: auth token used for reaching out to ebay
        :param query: query to reach
        """
        self.api_key = api_key
        self.query = query

    def make_request(self, params: dict):
        """
        Makes request to ebay api with provided key and query
        :param params: dictionary of required params
        :return: dict of response json from ebay api
        """
        base_url = "https://api.ebay.com/buy/browse/v1/item_summary/search"
        try:
            response = req.get(base_url, headers=self.create_headers(), params=params)
            return response.json()
        except req.exceptions.Timeout:
            print(f"Timed out whilst making request to {base_url}")
        except req.exceptions.RequestException as e:
            raise EbayRequestException(e.request)

    def create_headers(self):
        """
        Create headers needed for request ebay api
        :return: str of headers
        """
        return {
            'Authorization': f'Bearer {self.api_key}',
            'X-EBAY-C-MARKETPLACE-ID': 'EBAY_GB'
        }


def create_parameter_dict(query: str, category_ids: str, filter: str, limit: str):
    """
    Create parameter dictionary
    :param limit:
    :param filter:
    :param query:
    :param category_ids:
    :return: dictionary of parameters
    """
    return {
            'q': query,
            'category_ids': category_ids,
            'limit': limit,
            'filter': filter
    }

# Above is what I would have done.


# base_url = "https://api.ebay.com/buy/browse/v1/item_summary/search"
# headers = {
#         'Authorization': f'Bearer {key}',
#         'X-EBAY-C-MARKETPLACE-ID': 'EBAY_GB'
# }
# params = {
#         'q': query,
#         'category_ids': category_ids,
#         'gtin': gtin,
#         'charity_ids': charity_ids,
#         'fieldgroups': fieldgroups,
#         'compatibility_filter': compatibility_filter,
#         'auto_correct': auto_correct,
#         'filter': filter,
#         'sort': sort,
#         'limit': limit,
#         'offset': offset,
#         'aspect_filter': aspect_filter,
#         'epid': epid,
# }


# def ripley(api_key, query, category_ids, gtin=None, charity_ids=None, fieldgroups=None, compatibility_filter=None,
#            auto_correct=None, filter=None, sort=None, limit=None, offset=None, aspect_filter=None, epid=None):
#     base_url = "https://api.ebay.com/buy/browse/v1/item_summary/search"
#     headers = {
#         'Authorization': f'Bearer {api_key}',
#         'X-EBAY-C-MARKETPLACE-ID': 'EBAY_GB'
#         # 'Content-Type': 'application/json',
#     }
#     params = {
#         'q': query,
#         'category_ids': category_ids,
#         'gtin': gtin,
#         'charity_ids': charity_ids,
#         'fieldgroups': fieldgroups,
#         'compatibility_filter': compatibility_filter,
#         'auto_correct': auto_correct,
#         'filter': filter,
#         'sort': sort,
#         'limit': limit,
#         'offset': offset,
#         'aspect_filter': aspect_filter,
#         'epid': epid,
#     }

# Remove None values from params
# params = {k: v for k, v in params.items() if v is not None}

# response = req.get(base_url, headers=headers, params=params)
# print((base_url + str(headers) + str(params)))
# print(str(base_url) + str(headers) + str(params))
# print(base_url + str(headers) + str(params))
# print(response.json())
# return response.json()

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
