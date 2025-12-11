import requests

headers = {
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'priority': 'u=1, i',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Chromium";v="143", "Not A(Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36',
}

data = f'type=card&card[number]=5518277065657015&card[cvc]=866&card[exp_month]=03&card[exp_year]=30&guid=92f88592-061f-452d-b5dd-66c699ffbec313c7dc&muid=bea27f56-7c90-4b5e-992f-d8f075bdd1ea77db3a&sid=72f1bc21-865e-4d6a-adfc-979f505a59bfd23631&pasted_fields=number&payment_user_agent=stripe.js%2F6c35f76878%3B+stripe-js-v3%2F6c35f76878%3B+card-element&referrer=https%3A%2F%2Fallcoughedup.com&time_on_page=75898&client_attribution_metadata[client_session_id]=386ab77f-cef5-4bed-999c-e2fbb17eddd3&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=card-element&client_attribution_metadata[merchant_integration_version]=2017&key=pk_live_51PvhEE07g9MK9dNZrYzbLv9pilyugsIQn0DocUZSpBWIIqUmbYavpiAj1iENvS7txtMT2gBnWVNvKk2FHul4yg1200ooq8sVnV&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwZCI6MCwiZXhwIjoxNzY1NDU3ODI4LCJjZGF0YSI6ImptU1RJeC9Jdm9WUzl6dlN0QUZQTFpGTUNBMFBzdHA4ZGp4bk9zSkZXRTlvTTlpaFhCYXZuVXNoOFFhOHNGODZNUmVqbkkyWjE3TXc2WWs5VG1hcERZa2JuNksxUWNVRlBCb3RRL1I3MHhvL1JXTVBZdHRWR1VremJodFV5YlJhMXVja1NSZmtXZmUzZVhqb2xMVGhyNDJoREt6L1BZTzMrMERIQUExMUxiSHdpNkVaYTJocmpiaHN1M1lLZ3EwWVlGN3V4RVh6bWhYNjBXcGMiLCJwYXNza2V5IjoiTmtVUENDYWNuTTFGdWpXcFZ1ZVo0dDRJUXQrd1ViN3JLVURudGtZYjdaMk41V3MxTys2NXN3QlBGQnZiblhLMitUNU94VmZhRmxCdzVxMmhZbjk5Vzl1Ykh4RmNlaXNQR2IzSlpQWncvWjByWVROaDRTeWxLTmErZHdBRWR6UUY1ajJTbmNkdlV2UlJSOVNVOTJIUHZ6bTNNVkxrYlo0UXJEb2xXTGhsYkJIT0ZITnl5ckRUVjhyTE1abUlXRlJYeU4zWWpEZE1GemJ2K0FhdFZPYU5GWWVCM3pxdDc1bUdicWxwTlUzWFZrejJUU0swajZsbDdXYWQ5cE5NTGc4WG11MU5YNXJ2MnZxb1J4eVN6bnlGWmptYko0Y04vMS9keFY5UUpiRHVuT01xdWdTWnNmLzYwUGM0M2lVdUczajNXcVNYcDVnVElwZHhoZ1ZTTGE4aVdNek0vanF2dnEwQ2RtbDBnM3R3blI0YWNZekE3ZHoxWUJ2QU43OWhEZSt2ME4wSXFyTmRiN09NcjBXVWRtQjNhMDBKSDZCRW1sa09BaGZRQ1BmMWg5aHZIMEZqZFkvcnJXM0dqMHpPSmt4MW1jOWlYTUdLWUZubHEzdkdYMEpSZldkZXp6VG83d2ZlZGg5RmM1UldsVzNyWlkzQ3JUM1ZXZkhzV3R4SldSdjd2c1RJU1lXUVI3U25ZcDhVYXhhQU1VaGpLdmtiWVN6bTNJMjgzRVhXN1JXUDU2ZjQ3ZDhqOVR5alhPcmI1RnBnSldMaUhaR2piZEU3R0JQNWRqUC9LWVRvWUNyY1pIMDRpd1BVQWZOUi9rTDVzYWNTTVk0MWo3K3N5QkN4Rzg3a2x6QzVnNmlwTkZkeTBkUVlKVDY4V2NXUEl2dkl6UlU1eGYxTzhjTUd2cHJveXJDdmViQ2h3OFplZVNMQk9uMTBrUERXd2JPbzZTRUlpblkrOUVTVjFCYVVXR0NnaWtEK3lIem03aEtDbEEwbHNxN1ZkNm9iTTBhbmNQUjg2ZlgwUVllb1RCemhWc2VrS3VvU1dJbU1QMU5WMzN0L0RmL2NhbmZNMjd0UDZHZytta3Rva1dRd2ZZTEVBOHVFZ3pTc2pPMTFSZlFCdm5MTTg3bHQ4S2hSOUQvQUlwanhEdTRjcjN0WlpYWXBNWURLNlphK2l3em9HRGZJTGR5QzFybDF5RlU2SDdpWkpaNDdtRVdFcjNvbkJNQmVTVnN1a1pQN3dXUm9uUE8zemNacCs5WVhCNCtKMFVCbVRHSVJaVnFXWWZrb1liTVkvSVZSSjlTdWlSTGRzODFrV0o2STZ2d2FJaTU0SFRQT3MycnNwYWhHMy9mRENZM2tHSTFHYVd5bkY3YTNBQjBicWNYajN2YUYzejBxa2dpcDl6OVBLY2xIaDZjeGN0T0ZWZ052dFh4WUdqa1l6azB4TDZWR2tBM0NoVzIvNWthRnBmNGtQdTlvZGRsQU1zSjhmZDZIOExXR050ajllandsOGJNdkljZS9wOFZYS2xObHZyUnNXcUxrRW9xYy9zVVVkQ3hxcWtMd3MwaFI4MnJ5U0NDTnA5aXl3SDdGN3ZmQmJWN1BVTjRMZHN5dGxqMGltZUtNSlBVakNVc29GaHNoMkpCYnc0MlJZMGRHMWtYd2hjbVJEQ0dlZ05FWW9DZUR0Ykk2SzlHV0Q0NXJ5VUZydTRzbWpjcENCb0xTdVFuN2gxQjJ5akxOaU5JWlZXSS9Ua21XRytTNVllOTl4a1F2NlNSelNlT1ppQkhSMk1vdUl4anUzeEt0WTZna0llRXVzLzNNZ3lEUFQvd1dQSlBWUXlnaWxFZ0pBRXpaSGZWK1prWmRVYjdFbHZXT1ZCUEE4QzlwYmhkb3RITUxkM3paWllneGlIb2I0UWpTdnZNT0RGTDBvQ0drZG9kaHdlR2wzUlB1S2dBVnZLWDZER2kxVXQyZ2ZHYWdYSFZ6VTViOU1vKzg1V1ZmMFcyeFNVNXU1VUhGTmh1WnpzSjZnMXFUTWxTSXJ5Ni9JNk0xTVlaWnRVZE0rVnBUUXBMTi92SFdzYStKNmhXdStOTXowcTcrR0JudG1tMURPaDN0N2FtN0QvdjcyWm1USlNtM2ZyVjZSSWh3S2tENG54bGUvRFFpSjU3N29WR2JyQ0psV2ZkNnFFdlgvOWx4azNpS29mUGdqaE1XUmJiNEhVaklCd3NGY3RkQnlJUFRPc0EvZGhRRnNIRkpBemN6aE5kWDJiNFIrcFhxdzJBSUhQdzNJaXJpTG9HSkE3dTM3QXBMYWNKT2JCQ3VBMlJmdUxSb21IMmMxeEl0NzdNY0Y0WGk4clVkTXRtaXFSVHl5alhrb2luM1F3U1B5UEhpd0ZTeStxZW9JNmt3eUxsNm93eGx2UVE4ejBjT2tHZ0QrMjI5aWhLbFJmUVhRQjBnQ05oU3VRWk8vZTlIYlZsQjFjYW5sRFFyYTZFNlR0SlB1VUJjWlRJYkFvSGxOVlN4MXU4clJUNXkzc28vQUxuV3JjUXZ6Z1g5ZGg5M1drZkJ0VlZLNHkxeU9xTHozYTQwZTJKeFJSTHUyVFQxN1c0cFJ6blB4Zz09Iiwia3IiOiI0MGVlNjZiMSIsInNoYXJkX2lkIjozNjI0MDY5OTZ9.zNmeUdptlpeTLBTlHEscDxcWTnZ2yiQErY1POyChbgQ'

response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)

id=(response.json()["id"])

import requests

cookies = {
    '__stripe_mid': 'bea27f56-7c90-4b5e-992f-d8f075bdd1ea77db3a',
    '__stripe_sid': '72f1bc21-865e-4d6a-adfc-979f505a59bfd23631',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://allcoughedup.com',
    'priority': 'u=1, i',
    'referer': 'https://allcoughedup.com/registry/',
    'sec-ch-ua': '"Chromium";v="143", "Not A(Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    
}

params = {
    't': '1765457776015',
}

data = {
f'data': '__fluent_form_embded_post_id=3612&_fluentform_4_fluentformnonce=ef1301b3d9&_wp_http_referer=%2Fregistry%2F&names%5Bfirst_name%5D=min%20min%20&email=ssiren103%40gmail.com&custom-payment-amount=10&description=hello%20&payment_method=stripe&__stripe_payment_method_id={id}}',
    'action': 'fluentform_submit',
    'form_id': '4',
}

response = requests.post(
    'https://allcoughedup.com/wp-admin/admin-ajax.php',
    params=params,
    cookies=cookies,
    headers=headers,
    data=data,
)
print (response.text)
