#!/usr/bin/env python3

import ovh

# create a client using configuration
client = ovh.Client()

# Request GET, POST, PUT, /domain/zone/* API access
ck = client.new_consumer_key_request()
ck.add_rules(ovh.API_READ_WRITE_SAFE, "/domain/zone/*")

# Request token
validation = ck.request()

print("Please visit {} to authenticate".format(validation['validationUrl']))
input("and press Enter to continue...")

# Print nice welcome message
print("your 'consumerKey' is '{}', add this to ovh.conf".format(validation['consumerKey']))

