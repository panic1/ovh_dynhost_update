#!/usr/bin/env python2

import ovh

# create a client using configuration
client = ovh.Client()

# Request GET, POST, PUT, /domain/zone/* API access
ck = client.new_consumer_key_request()
ck.add_rules(ovh.API_READ_WRITE_SAFEONLY, "/domain/zone/*")

# Request token
validation = ck.request()

print "Please visit %s to authenticate" % validation['validationUrl']
raw_input("and press Enter to continue...")

# Print nice welcome message
print "your 'consumerKey' is '%s', add this to ovh.conf" % validation['consumerKey']

