import requests
import json

url = "https://dashboard.meraki.com/api/v0/organizations"

headers = {
  'X-Cisco-Meraki-API-Key': 'cda1694c0cb04ebd24afd36a715b56879ae1f472'
}

response = requests.get(url, headers=headers).json()

print(json.dumps(response, indent=2, sort_keys=True))

for response_org in response:
    if response_org['Name'] == 'Devnet Sandbox':
        orgId = response_org['id']

print(orgId)
