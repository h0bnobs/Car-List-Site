import sys

from flask import Flask, render_template
from ripley import ripley

app = Flask(__name__)


# TODO: need to figure out why im only getting a few responses, while when searching on ebay website, i get way more

@app.route('/')
def index():
    api_key = 'v^1.1#i^1#f^0#p^1#I^3#r^0#t^H4sIAAAAAAAAAOVYbWwURRi+a+8gFIqCgFiInNvij5q924/73PQuXr9oaXt39M5aDgmZ3Z1tF/Z2l925Xht+UJqmFSyKIoZE2lSMwQg0/JOg5StRFNGACLFBExM/wg9+YVATY3DvepRrJYD0Ei/x/lzmnXfeeZ5n3ndmdojeOfMqBxoGfi81zy0a7SV6i8xmcj4xb471uYXFRWVWE5HjYB7trei19BVfr9JBQlKZVqiriqxDW3dCknUmY/RjSU1mFKCLOiODBNQZxDHRYEszQ9kJRtUUpHCKhNkaa/2YBwjQ53MTPMkJAqQpwyrfiRlT/JjPJQDa4xNISAHg9ZBGv64nYaOsIyAjP0YRlBMn3DhNxEiScRIM6bJTlDuO2dqgpouKbLjYCSyQgctkxmo5WO8PFeg61JARBAs0Buuj4WBjbV0oVuXIiRXI6hBFACX16a0ahYe2NiAl4f2n0TPeTDTJcVDXMUdgcobpQZngHTCPAD8jNQWdFOBdrI/nWdIngLxIWa9oCYDujyNtEXlcyLgyUEYi6nmQooYa7GbIoWwrZIRorLWl/9YlgSQKItT8WF11cH0wEsECLaC7Gki8gnNAM/JrMx5prcUJF2Q52u3y4F6KhgL0cNl5JoNlVZ4xUY0i82JaM90WUlA1NEDDmdLQOdIYTmE5rAUFlAaU60dPSUjF02s6uYhJ1CmnlxUmDB1smeaDF2BqNEKayCYRnIowsyOjkB8Dqiry2MzOTCpms6db92OdCKmMw5FKpewp2q5oHQ6KIEhHe0tzlOuECSNBDN90rWf8xQcPwMUMFQ4aI3WRQT2qgaXbSFUDgNyBBZw+j8vryuo+HVZgpvUfhhzOjukFka8CYZ0k7XRRkHV7odcglo8CCWRz1JHGAVnQgyeAtgUiVQIcxDkjz5IJqIk8Q7sEivYKEOfdPgF3+gQBZ128GycFCAkIWZbzef9HdfKwmR6FnAZRflI9X2kOutqFeFuomePB2npaan4R8RE25UXh7mp3kwrWxlqqu+u2tqW6alP+hy2Ge5KvkURDmZgxf+HVeoOiI8jPil6UU1QYUSSR6ymsBaY1PgI01BOFkmQYZkUyqKqNedqq80Xv3+0Sj0Y7jyfUf3M63ZOVns7YwmKVHq8bAYAq2tPnj51TEg4FJNO1jjrT5k0Z1LPiLRrX1oJibZCcZCvyk/dNu0EZddr1Ls6uQV1JasZV2x5O379iyhYoG8cZ0hRJglobOetyTiSSCLASLLS6zkOCi6DAzlrSQ/o8To+bnB0vLnOSbiq0LSlPO7Gl5hHu1I7pH/gBU+ZH9pnPEn3mk0VmM1FFrCbLiWfmFL9gKV5QposI2kUg2HWxQza+WzVo3wJ7VCBqRU+Ybh7c11BTVhd+q3JbrOfi2+dMC3LeF0Y3EsunXhjmFZPzc54biJV3e6zkY0+WUk7CTRMk6SRIV5wov9trIZdZlqyurn+t9Yvlw6zpbOrkqvlxbeeyNUTplJPZbDVZ+symuZfxpj++VkeGflz4yY7wlQsbTx15tu7axT3Xif5K0Jos+uhdi2vVq9IP+48cvXLiu1+qDn0eaLeWNpxY+c6v/eNDv43c/nK8bJn61cb46JvfDtADnpsV607v/PmDHeXXdg+HsPPc0ZFPl1yqGcQXja0ZXOrcM3hp2zcVj7NbR/2R0jOm8t0vlzSt+pC+dW4iIdaN/VT7VPzArQn82OKusUVy/8QbHdYN+ntt48cmtl9t/2vl9p1DB85/P5j6+Om9w7uG31+xYv2h0/sP3yw5eLiy4qXPbjith327/gyFhspL+haOX7t0w2Ubk5LHSwbHNvSvGzo++nr582cii6/fPrWg6ermvRcSl6++sm/50sm1/BsJcRd0+REAAA=='
    query = 'Subaru+Impreza+WRX'
    category_ids = '9800'  # Category ID for Cell Phones & Smartphones
    limit = 100  # Limit the results to 5 items

    result = ripley(api_key, query, category_ids, limit)
    print(result['total'])
    items = []
    if 'itemSummaries' in result:
        for item in result['itemSummaries']:
            # if item['price']['value'] > 1999:
            items.append({
                'title': item['title'],
                'cat': 'Cars',
                'price': item['price']['value'],
                'seller': item.get('seller', {}).get('username', 'Unknown'),
                'url': item['itemWebUrl'],
                'image': item['image']['imageUrl'],
            })

    return render_template('index2.html', items=items)


if __name__ == '__main__':
    app.run(debug=True)
