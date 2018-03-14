#!/usr/bin/env python2

import json
import ovh
import requests
from ConfigParser import RawConfigParser, NoSectionError, NoOptionError

domain_config = RawConfigParser()
domain_config.read("./domain.conf")
domain = domain_config.get("zone", "domain")
subdomain = domain_config.get("zone", "subdomain")

# Instanciate an OVH Client, reads from ovh.conf
client = ovh.Client()

# 1. Get the dynhost ID
dynhost_id = client.get('/domain/zone/' + domain + '/dynHost/record',
    subDomain=subdomain)[0]

# 2. Get the current IP address of the DynHost
ip = client.get('/domain/zone/' + domain + '/dynHost/record/' + str(dynhost_id))

# 3. Get the current public IP of this host
curr_ip = json.loads(requests.get("http://v4.ifconfig.co/json").content)['ip']

# 4. Compare with the current public IP address of this host
if (curr_ip == ip):
    sys.exit()
else:
    print "IP address is still the same, no need to update"

# 5. If the public IP has been changed, update the DynHost IP address
result = client.put('/domain/zone/' + domain + '/dynHost/record/' + str(dynhost_id), 
    ip=curr_ip,
    subDomain='cloud',
)
