import requests


def ripley(api_key, query, category_ids, limit, gtin=None, charity_ids=None, fieldgroups=None, compatibility_filter=None,
           auto_correct=None, filter=None, sort=None, offset=None, aspect_filter=None, epid=None):
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
    # print(str(base_url) + str(headers) + str(params))
    # print(base_url + str(headers) + str(params))
    # print(response.json())
    return response.json()

    # if response.status_code == 200:
    #     return response.json()
    # else:
    #     response.raise_for_status()


# Replace 'YOUR_API_KEY' with your actual eBay API key
api_key = 'v^1.1#i^1#f^0#p^1#I^3#r^0#t^H4sIAAAAAAAAAOVYbWwURRi+a+8gFIqCgFiInNvij5q924/73PQuXr9oaXt39M5aDgmZ3Z1tF/Z2l925Xht+UJqmFSyKIoZE2lSMwQg0/JOg5StRFNGACLFBExM/wg9+YVATY3DvepRrJYD0Ei/x/lzmnXfeeZ5n3ndmdojeOfMqBxoGfi81zy0a7SV6i8xmcj4xb471uYXFRWVWE5HjYB7trei19BVfr9JBQlKZVqiriqxDW3dCknUmY/RjSU1mFKCLOiODBNQZxDHRYEszQ9kJRtUUpHCKhNkaa/2YBwjQ53MTPMkJAqQpwyrfiRlT/JjPJQDa4xNISAHg9ZBGv64nYaOsIyAjP0YRlBMn3DhNxEiScRIM6bJTlDuO2dqgpouKbLjYCSyQgctkxmo5WO8PFeg61JARBAs0Buuj4WBjbV0oVuXIiRXI6hBFACX16a0ahYe2NiAl4f2n0TPeTDTJcVDXMUdgcobpQZngHTCPAD8jNQWdFOBdrI/nWdIngLxIWa9oCYDujyNtEXlcyLgyUEYi6nmQooYa7GbIoWwrZIRorLWl/9YlgSQKItT8WF11cH0wEsECLaC7Gki8gnNAM/JrMx5prcUJF2Q52u3y4F6KhgL0cNl5JoNlVZ4xUY0i82JaM90WUlA1NEDDmdLQOdIYTmE5rAUFlAaU60dPSUjF02s6uYhJ1CmnlxUmDB1smeaDF2BqNEKayCYRnIowsyOjkB8Dqiry2MzOTCpms6db92OdCKmMw5FKpewp2q5oHQ6KIEhHe0tzlOuECSNBDN90rWf8xQcPwMUMFQ4aI3WRQT2qgaXbSFUDgNyBBZw+j8vryuo+HVZgpvUfhhzOjukFka8CYZ0k7XRRkHV7odcglo8CCWRz1JHGAVnQgyeAtgUiVQIcxDkjz5IJqIk8Q7sEivYKEOfdPgF3+gQBZ128GycFCAkIWZbzef9HdfKwmR6FnAZRflI9X2kOutqFeFuomePB2npaan4R8RE25UXh7mp3kwrWxlqqu+u2tqW6alP+hy2Ge5KvkURDmZgxf+HVeoOiI8jPil6UU1QYUSSR6ymsBaY1PgI01BOFkmQYZkUyqKqNedqq80Xv3+0Sj0Y7jyfUf3M63ZOVns7YwmKVHq8bAYAq2tPnj51TEg4FJNO1jjrT5k0Z1LPiLRrX1oJibZCcZCvyk/dNu0EZddr1Ls6uQV1JasZV2x5O379iyhYoG8cZ0hRJglobOetyTiSSCLASLLS6zkOCi6DAzlrSQ/o8To+bnB0vLnOSbiq0LSlPO7Gl5hHu1I7pH/gBU+ZH9pnPEn3mk0VmM1FFrCbLiWfmFL9gKV5QposI2kUg2HWxQza+WzVo3wJ7VCBqRU+Ybh7c11BTVhd+q3JbrOfi2+dMC3LeF0Y3EsunXhjmFZPzc54biJV3e6zkY0+WUk7CTRMk6SRIV5wov9trIZdZlqyurn+t9Yvlw6zpbOrkqvlxbeeyNUTplJPZbDVZ+symuZfxpj++VkeGflz4yY7wlQsbTx15tu7axT3Xif5K0Jos+uhdi2vVq9IP+48cvXLiu1+qDn0eaLeWNpxY+c6v/eNDv43c/nK8bJn61cb46JvfDtADnpsV607v/PmDHeXXdg+HsPPc0ZFPl1yqGcQXja0ZXOrcM3hp2zcVj7NbR/2R0jOm8t0vlzSt+pC+dW4iIdaN/VT7VPzArQn82OKusUVy/8QbHdYN+ntt48cmtl9t/2vl9p1DB85/P5j6+Om9w7uG31+xYv2h0/sP3yw5eLiy4qXPbjith327/gyFhspL+haOX7t0w2Ubk5LHSwbHNvSvGzo++nr582cii6/fPrWg6ermvRcSl6++sm/50sm1/BsJcRd0+REAAA=='
query = 'subaru impreza wrx'
category_ids = '6001'  # Category ID for Cell Phones & Smartphones
limit = 10  # Limit the results to 5 items

result = ripley(api_key, query, category_ids, limit=limit)

# Print the search results
# for item in result['itemSummaries']:
#     print(f"Title: {item['title']}")
#     print(f"Price: {item['price']['value']} {item['price']['currency']}")
#     print(f"Item Web URL: {item['itemWebUrl']}")
#     print("-" * 40)
