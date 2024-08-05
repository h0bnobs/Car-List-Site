import fetch from 'node-fetch';
import fs from 'fs/promises';

class Api {
    constructor(apiKey, query) {
        this.apiKey = apiKey;
        this.query = query;
    }

    async makeRequest(params) {
        const baseUrl = 'https://api.ebay.com/buy/browse/v1/item_summary/search';
        const url = new URL(baseUrl);

        Object.keys(params).forEach(key => url.searchParams.append(key, params[key]));

        console.log('Request URL:', url.toString());

        const options = {
            method: 'GET',
            headers: {
                'Authorization': `Bearer ${this.apiKey}`,
                'X-EBAY-C-MARKETPLACE-ID': 'EBAY_GB',
                'X-EBAY-C-ENDUSERCTX': 'affiliateCampaignId=<ePNCampaignId>,affiliateReferenceId=<referenceId>'
            }
        };

        try {
            const response = await fetch(url, options);
            const responseCode = response.status;
            console.log('Response Code:', responseCode);

            if (responseCode === 200) {
                const content = await response.json();
                console.log('Response Content:', content);
                return content;
            } else {
                const errorContent = await response.text();
                console.error('Error response from eBay API:', errorContent);
                throw new Error(`Failed to get response from eBay API. HTTP response code: ${responseCode} - ${response.statusText}`);
            }
        } catch (error) {
            throw new Error(`Request error while fetching listings from the eBay API. Exception: ${error.message}`);
        }
    }
}

(async () => {
    try {
        const apiKey = (await fs.readFile('ebay_api_key', 'utf8')).trim();
        const query = 'Ford+Fiesta';
        const categoryIds = '9801';
        const limit = '100';
        const filter = 'buyingOptions:{AUCTION|CLASSIFIED_AD|AUCTION_WITH_BIN|FIXED_PRICE|BEST_OFFER}';
        const sort = 'price'; //if you want descending then its -price. ascending is 'price'

        const api = new Api(apiKey, query);
        const params = {
            q: query,
            category_ids: categoryIds,
            limit: limit,
            filter: filter,
            sort: sort
        };

        const result = await api.makeRequest(params);
        const items = [];

        if (result.itemSummaries) {
            result.itemSummaries.forEach(item => {
                const itemData = {
                    title: item.title,
                    cat: 'Cars'
                };

                if (item.buyingOptions.includes('AUCTION')) {
                    itemData.price = item.currentBidPrice.value;
                    itemData.seller = item.seller.username;
                    itemData.url = item.itemWebUrl;
                    itemData.image = item.image ? item.image.imageUrl : 'No image available';
                    itemData.buyingOptions = item.buyingOptions;
                } else if (item.buyingOptions.includes('CLASSIFIED_AD')) {
                    itemData.price = item.price.value;
                    itemData.seller = item.seller.username;
                    itemData.url = item.itemWebUrl;
                    itemData.image = item.thumbnailImages ? item.thumbnailImages[0].imageUrl : 'No image available';
                    itemData.buyingOptions = item.buyingOptions;
                } else if (item.buyingOptions.includes('AUCTION_WITH_BIN')) {
                    itemData.price = item.price.value;
                    itemData.seller = item.seller.username;
                    itemData.url = item.itemWebUrl;
                    itemData.image = item.thumbnailImages ? item.thumbnailImages[0].imageUrl : 'No image available';
                    itemData.buyingOptions = item.buyingOptions;
                } else if (item.buyingOptions.includes('FIXED_PRICE')) {
                    itemData.price = item.price.value;
                    itemData.seller = item.seller.username;
                    itemData.url = item.itemWebUrl;
                    itemData.image = item.thumbnailImages ? item.thumbnailImages[0].imageUrl : 'No image available';
                    itemData.buyingOptions = item.buyingOptions;
                } else if (item.buyingOptions.includes('FIXED_PRICE')) {
                    itemData.price = item.price.value;
                    itemData.seller = item.seller.username;
                    itemData.url = item.itemWebUrl;
                    itemData.image = item.thumbnailImages ? item.thumbnailImages[0].imageUrl : 'No image available';
                    itemData.buyingOptions = item.buyingOptions;
                } else if (item.buyingOptions.includes('BEST_OFFER')) {
                    itemData.price = item.price.value;
                    itemData.seller = item.seller.username;
                    itemData.url = item.itemWebUrl;
                    itemData.image = item.thumbnailImages ? item.thumbnailImages[0].imageUrl : 'No image available';
                    itemData.buyingOptions = item.buyingOptions;
                }

                items.push(itemData);
            });
        }

        console.log('Items to send:', items);

        // Send the JSON data to the Node.js server
        const nodeServerUrl = 'http://localhost:3000/data';
        const nodeResponse = await fetch(nodeServerUrl, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(items)
        });

        if (nodeResponse.status === 200) {
            console.log('Data sent to Node.js server successfully.');
        } else {
            console.error(`Failed to send data to Node.js server. HTTP response code: ${nodeResponse.status}`);
        }

    } catch (error) {
        console.error(error);
    }
})();
