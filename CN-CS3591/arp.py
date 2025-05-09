# arp.py

arp_table = {
    '192.168.1.1': '00:1A:2B:3C:4D:5E',
    '192.168.1.2': '00:1A:2B:3C:4D:5F',
    '192.168.1.3': '00:1A:2B:3C:4D:60'
}

def lookup_mac(ip):
    return arp_table.get(ip, "MAC address not found")

def main():
    ip = input("Enter IP address to lookup: ")
    mac = lookup_mac(ip)
    print(f"MAC address for {ip}: {mac}")

if __name__ == "__main__":
    main()
