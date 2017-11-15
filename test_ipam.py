"""IPAM client usage script"""

from ipam import IPAMClient

owner = 'OWNER'

# Instantiate IPAM client
ipam_client = IPAMClient()

# Get token
token = ipam_client.get_token()
print(token)

# Get first free IP
free_ip = ipam_client.get_first_free_ip(token)
print(free_ip)

# Reserve IP
ipam_client.reserve_ip(token, free_ip, owner)

# Get reserved IPs
res_ips = ipam_client.get_reserved_ips(token)
print(res_ips)

# Get address Id
addr_id = ipam_client.get_address_id(res_ips, owner)
print(addr_id)

# Unreserve IP
ipam_client.unreserve_ip(token, addr_id)

