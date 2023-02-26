#!/usr/bin/python3
# Script Name:  MACobfuscator.py
# Description:  The script changes first three octets of (OUI, vendor information) MAC address to another OUI.
#               New OUIs are taken randomly from the file with vendors OUIs. You can select specific hardware
#               vendors using the list vendor_name. Last three octets (NIC, interface information)
#               are randomly generated.
#               Tested on Linux, RHEL 8.5
# Usage: MACobfuscator.py
#        Before run the script, download and put mac-vendor.txt to directory with MACobfuscator.py.
#        Text file with vendors: https://gist.github.com/aallan/b4bb86db86079509e6159810ae9bd3e4
# Author: gaznick - katoda.pl - gaznick@katoda.pl
# Version: 1.0
# Date: 20 March 2022 - 15:00 (UTC+02:00)

import random

mac_to_obfuscate = "00:02:B3:12:34:56"
mac_to_obfuscate = mac_to_obfuscate.replace(":", "")

new_mac = str()

hexbase = "123456789abcdef"

vendors_list_unique = set()

file = open("mac-vendor.txt", "r", encoding="utf8")
oui_vendors_list = file.readlines()
file.close()

vendor_name = ["d-link", "cisco", "linksys", "meraki", "mikrotik"]

for element in oui_vendors_list:
    for vendor in vendor_name:
        if vendor.casefold() in element.casefold():         # case insensitive string comparison
            vendors_list_unique.add(element)                # makes only unique sets of vendors
                                                            # (e.g. Cisco can be in Meraki string) - set()

vendors_list = list(vendors_list_unique)

for digit in range(len(mac_to_obfuscate) // 2, len(mac_to_obfuscate)):  # change last six digits
    new_mac += hexbase[random.randint(0, 14)]

# take only first six digits from file for version without vendors name
# new_mac = vendors_list[random.randint(0, len(vendors_list) - 1)][0:6] + new_mac

new_mac_vendor = vendors_list[random.randint(0, len(vendors_list) - 1)]
new_mac = new_mac_vendor[0:6] + new_mac
new_mac_vendor = new_mac_vendor[7:].strip()


def string_delimiter(value_to_delimit, delimit_after="2", delimiter=":"):  # add delimiter to MAC

    delimited_value = str()
    delimit_after = int(delimit_after)

    x = 1
    for character in value_to_delimit:
        delimited_value += character
        if not x % delimit_after and x < len(value_to_delimit):
            delimited_value += delimiter
        x += 1
    return delimited_value


mac_to_obfuscate_vendor = str()

for i in range(len(oui_vendors_list)):  # find vendor for obfuscate MAC
    if oui_vendors_list[i][0:6].casefold() == mac_to_obfuscate[0:6].casefold():
        mac_to_obfuscate_vendor = oui_vendors_list[i][7:].strip()
        break


print("\nMAC to obfuscate: ")
print(mac_to_obfuscate_vendor) if mac_to_obfuscate_vendor else print('unknown')
print(string_delimiter(mac_to_obfuscate).upper())

print("\nNew MAC:")
print(new_mac_vendor)
print(string_delimiter(new_mac).upper())
