import requests

url = "https://api.leboncoin.fr/finder/search"
payload_main = {'api_key': 'f993fc88f7601bebdf3c35ccf527ad11', 'url': 'https://api.leboncoin.fr/finder/search'}
payload = {
    # 'api_key': 'f993fc88f7601bebdf3c35ccf527ad11',
    # 'url': 'https://api.leboncoin.fr/finder/search',
    "limit": 35,
    "limit_alu": 3,
    "limit_sponsored": 1,
    "sort_by": "relevance",
    "sort_order": "desc",
    "filters": {
        "enums": {"ad_type": ["offer"]},
        "location": {"locations": [
                {
                    "locationType": "city",
                    "city": "Paris",
                    "label": "Paris (toute la ville)",
                    "area": {
                        "lat": 48.8495376581948,
                        "lng": 2.340572835508209,
                        "default_radius": 8691
                    }
                }
            ]}
    },
    "offset": 35,
    "disable_total": True,
    "referrer_id": "c246aeeb-c56a-44d4-9ba5-495c5e493882",
    "pivot": "{\"es_pivot\":\"1664891317000|2231955742\",\"page_number\":1}",
    "extend": True,
    "listing_source": "pagination"
}
headers = {
    "cookie": "__Secure-Install=7d7ab2b1-0e77-47b2-b59a-24b999cec6bf; __Secure-InstanceId=7d7ab2b1-0e77-47b2-b59a-24b999cec6bf; didomi_token=eyJ1c2VyX2lkIjoiMTgzOWM0NjktOGY0OC02NjQxLWIzYTUtMzUwYTkxNDA3YmFhIiwiY3JlYXRlZCI6IjIwMjItMTAtMDNUMDU6MTc6MTIuMzExWiIsInVwZGF0ZWQiOiIyMDIyLTEwLTAzVDA1OjE3OjEyLjMxMVoiLCJ2ZW5kb3JzIjp7ImVuYWJsZWQiOlsiZ29vZ2xlIiwiYzpsYmNmcmFuY2UiLCJjOnJldmxpZnRlci1jUnBNbnA1eCIsImM6ZGlkb21pIl19LCJwdXJwb3NlcyI6eyJlbmFibGVkIjpbInBlcnNvbm5hbGlzYXRpb25tYXJrZXRpbmciLCJwcml4IiwibWVzdXJlYXVkaWVuY2UiLCJleHBlcmllbmNldXRpbGlzYXRldXIiXX0sInZlbmRvcnNfbGkiOnsiZW5hYmxlZCI6WyJnb29nbGUiXX0sInZlcnNpb24iOjIsImFjIjoiRExXQS1BRUlBSXdBV1FCLWdHRkFQeUFra0JKWUVBd0lrZ1NrQXR5QnhBRHB3SFZnUlVBam5CSk9DV3NGQmdLRVFVV2dybkJZS0MyOEZ4Z0xsZ1lEQXdpQmlhRExVQUFBLkRMV0E4QUVJQUl3QV9RRENnSDVBU1NBa3NDQVlFU1FKU0FXNUE0Z0IwNERxd0lxQVJ6Z2tuQkxXQ2d3RkNJS0xRVnpnc0ZCYmVDNHdGeXdNQmdZUkF4TkJscUFBIn0=; euconsent-v2=CPgRXwAPgRXwAAHABBENCiCgAPLAAHLAAAAAIAtB_G_dTyPi-f59YvtwYQ1P4VQnoyACjgaNgwwJiRLBMI0EhmAIKAHqAAACIBAEICJAAQBlCAHAAAAA4IEAASMMAAAAIRAIIgCAAEAAAiJICABZCxAAAQAQgkwAABQAgAICABMgSDAAAAAAFAAAAAgAAAAAAAAAAAAAQAAAAAAAAggCACYatxAA2JY4E0gYRAAARhAEAUAIAKKAIWCAAgJEAAgjAAUYAAAAAoAAAAAACAgBgAAAAEACEAAAADggEABAAgAAAAgEAgAAAAAQAAAYAAAAAABgAAAAAEABAAABQCAAAIAEABIEAAQAAAEAAAAAAAAAEAgAAAAAAAAAAAAAAACAGKAAwABBIAYABgACCQBAADAAEEgA.flgADlgAAAAA; include_in_experiment=true; utag_main=v_id:01839c469798001dc57de7c52f4804065005b05d00bd0$_sn:2$_ss:1$_st:1664893257538$_pn:1%3Bexp-session$ses_id:1664891455191%3Bexp-session; datadome=QD00ck_eBnaVVMQTmuclIqi5DVZ47B4FCUwnHInHIsk~Jg3boX18QwcJk8aqxNKcW2HnjrLxtBX.SQgdUBqZikVBRdpOr_ZOWxheqiwppoXj6epAHVsZNFoofd8MYNZ; dblockS=7; dblockV=1;",
    "authority": "api.leboncoin.fr",
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.9",
    "api_key": "ba0c2dad52b3ec",
    "cache-control": "no-cache",
    "content-type": "application/json",
    "origin": "https://www.leboncoin.fr",
    "pragma": "no-cache",
    "referer": "https://www.leboncoin.fr/",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "sec-gpc": "1",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
}

response = requests.request("POST", url=url,  headers=headers,json=payload)

print(response.text)