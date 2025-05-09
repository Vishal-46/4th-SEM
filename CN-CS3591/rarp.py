# rarp.py
rarp_table = {
    '00:1A:2B:3C:4D:5E': '192.168.1.1',
    '00:1A:2B:3C:4D:5F': '192.168.1.2',
    '00:1A:2B:3C:4D:60': '192.168.1.3'
}

def lookup_ip(mac):
    return rarp_table.get(mac, "IP address not found")

def main():
    mac = input("Enter MAC address to lookup: ")
    ip = lookup_ip(mac)
    print(f"IP address for {mac}: {ip}")

if __name__ == "__main__":
    main()
