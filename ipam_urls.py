""" IPAM URLs module"""

AUTH_URL = 'http://%s/api/?app_id=%s&controller=user'
FREE_IP_URL = 'http://%s/api/?app_id=%s&controller=subnets&id=%d&id2=first_free'
RESERVE_IP_URL = 'http://%s/api/?app_id=%s&controller=addresses&subnetId=%d&ip=%s&tag=2&owner=%s'
RESERVED_IPS_URL = 'http://%s/api/?app_id=%s&controller=subnets&id=%d&id2=addresses'
UNRESERVE_IP_URL = 'http://%s/api/?app_id=%s&controller=addresses&id=%s'
