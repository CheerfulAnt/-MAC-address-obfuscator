# MAC-address-obfuscator

The script changes first three octets of (OUI, vendor information) MAC address to another OUI. 
New OUIs are taken randomly from the file with vendors OUIs. You can select specific hardware vendors using the list vendor_name. 
Last three octets (NIC, interface information) are randomly generated.

Before run the script, download and put mac-vendor.txt to directory with MACobfuscator.py.
Text file with vendors: https://gist.github.com/aallan/b4bb86db86079509e6159810ae9bd3e4
