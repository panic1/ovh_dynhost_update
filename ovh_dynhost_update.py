#!/usr/bin/env python3

import json
import ovh
import requests
from configparser import RawConfigParser, NoSectionError, NoOptionError

CONF_FILE = 'domain.conf'

domain_config = RawConfigParser()
domain_config.read(CONF_FILE)
zone = domain_config.sections()[0]
domain = domain_config.get(zone, "domain")
subdomain = domain_config.get(zone, "subdomain")

# Instanciate an OVH Client, reads from ovh.conf
client = ovh.Client()

# 1. Get the dynhost ID
dynhost_id = client.get('/domain/zone/' + domain + '/dynHost/record',
    subDomain=subdomain)[0]

# 2. Get the current IP address of the DynHost
ip = client.get('/domain/zone/' + domain + '/dynHost/record/' + str(dynhost_id))

# 3. Get the current public IP of this host
# curr_ip = json.loads(requests.get("http://v4.ifconfig.co/json").content)['ip']
curr_ip = requests.get("http://ip4only.me/api/").text.split(',')[1]

# 4. Compare with the current public IP address of this host
if (curr_ip == ip):
    sys.exit()

# 5. If the public IP has been changed, update the DynHost IP address
result = client.put('/domain/zone/' + domain + '/dynHost/record/' + str(dynhost_id), 
    ip=curr_ip,
    subDomain=subdomain,
)

