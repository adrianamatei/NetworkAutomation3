import ipaddress

intf=ipaddress.ip_network('10.0.0.0/16')
print(intf.compressed)
print(intf.netmask)
print(intf.network_address.compressed)
