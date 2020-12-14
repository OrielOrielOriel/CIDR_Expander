#!/usr/bin/python3

from netaddr import IPNetwork
import sys

HELP = """
Help scren
"""

if len(sys.argv) != 2:
	print(HELP)
	exit(1)

with open(sys.argv[1], "r") as cidr_file, open("expanded_"+sys.argv[1], "w") as target_file:
	for subnet in cidr_file:
		ip_list = IPNetwork(subnet)

		for ip in ip_list:
			target_file.write(str(ip)+"\n")
