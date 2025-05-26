import meraki
from pprint import pprint

token = #(Your_token_goes_here)
meraki = meraki.DashboardAPI(token)

#################### GET ORGANIZATIONS ####################

orgs = meraki.organizations.getOrganizations()
pprint(orgs)

for org in orgs:
    print('*********************\n')
    for key, value in org.items():
        print(f"{key}: {str(value)}")
        if org['name'] == 'DevNet Sandbox':
            orgId = org['id']

print('*********************\n')
print(orgId)

#################### GET ORGANIZATION NETWORKS ####################

networks = meraki.organizations.getOrganizationNetworks(orgId)
pprint(networks)

for network in networks:
    if network['name'] == 'DevNet Sandbox ALWAYS ON':
        netId = network['id']

#################### GET NETWORK VLANS ####################

vlans = meraki.networks.getNetworkVlanProfiles(netId)
vlan = vlans[0]
print(vlan)

vlan['name'] = 'Knox Wuz Here'
new_name = vlan['name']

updated_vlan = {}
updated_vlan['netword_id'] = netId
updated_vlan['vlan_id'] = vlan['vlanNames'][0]['vlanId']
updated_vlan['update_network_vlan'] = vlan

vlanGroups = [""]

result = meraki.networks.updateNetworkVlanProfile('Default', 'Default Profile', {'name': 'Knox was here', 'vlanId': '1'})

result_vlan = vlans = meraki.networks.getNetworkVlanProfiles(netId)

pprint(result_vlan)





