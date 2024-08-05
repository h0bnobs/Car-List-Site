# Ripley
Fetch car listings from various apis used within the UK and represent listings
across webpage using a small flask server.

Link to source for finding the best apis to use [here](https://www.thecarexpert.co.uk/best-websites-buying-a-car/)

## Outstanding API requirements
     - autotrader (enquired about api)
     - motors (enquired about api)
     - ebay (got api access)
     - fb marketplace (still researching)
     - carwow?
     - Motorpoint
     - CarGurus
     - PistonHeads
     - Heycar
     - Cinch
     - Vertu Motors
     - CarShop

## Options when querying the ebay api
Supported parameters are: 
```json
    {
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
```
