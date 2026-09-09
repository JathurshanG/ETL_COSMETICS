import requests

url = "https://www.sephora.com/sitemaps/products-sitemap.xml"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers, timeout=30)

print(response.status_code)
print(response.url)
response.text