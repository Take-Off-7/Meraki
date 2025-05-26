import requests
import json

url = "https://dashboard.meraki.com/api/v0/organizations"

headers = {
  'X-Cisco-Meraki-API-Key': #(Your_key_goes_here)
}

response = requests.get(url, headers=headers).json()

print(json.dumps(response, indent=2, sort_keys=True))

for response_org in response:
    if response_org['Name'] == 'Devnet Sandbox':
        orgId = response_org['id']

print(orgId)
