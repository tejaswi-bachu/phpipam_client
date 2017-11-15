"""PHP IPAM client"""

import requests
from requests.auth import HTTPBasicAuth

from ipam_urls import AUTH_URL
from ipam_urls import FREE_IP_URL
from ipam_urls import RESERVE_IP_URL
from ipam_urls import RESERVED_IPS_URL
from ipam_urls import UNRESERVE_IP_URL


class IPAMClient(object):
    """IPAM client to interact with PHP IPAM"""

    def __init__(self, username, password, ip, app_id, subnet_id):
        """Instantiate IPAM client"""

        self.username = username
        self.password = password
        self.ip = ip
        self.app_id = app_id
        self.subnet_id = subnet_id

    def get_token(self):
        """Return token for a given username and password"""

        headers = {'Accept': 'application/json',
                   'Content-Type': 'application/json'}
        url = AUTH_URL % (self.ip, self.app_id)
        response = requests.post(url=url,
                                 headers=headers,
                                 auth=HTTPBasicAuth(self.username,
                                                    self.password))
        return response.json()['data']['token']

    def get_first_free_ip(self, token):
        """Return first available IP"""

        headers = {'phpipam-token': token}
        url = FREE_IP_URL % (self.ip, self.app_id, self.subnet_id)
        response = requests.get(url=url, headers=headers)
        return response.json()['data']

    def reserve_ip(self, token, client_ip, owner):
        """Reserve IP for a owner"""

        headers = {'phpipam-token': token}
        url = RESERVE_IP_URL % (self.ip, self.app_id, self.subnet_id,
                                client_ip, owner)
        requests.post(url=url, headers=headers)

    def get_reserved_ips(self, token):
        """Return all reserved IPs"""

        headers = {'phpipam-token': token}
        url = RESERVED_IPS_URL % (self.ip, self.app_id, self.subnet_id)
        response = requests.get(url=url, headers=headers)
        return response.json()['data']

    def get_address_id(self, addresses, owner):
        """Return address Id of a owner"""

        for address in addresses:
            if address['owner'] == owner:
                return address['id']

    def unreserve_ip(self, token, address_id):
        """Unreserve IP for a given address Id"""

        headers = {'phpipam-token': token}
        url = UNRESERVE_IP_URL % (self.ip, self.app_id, address_id)
        requests.delete(url=url, headers=headers)
