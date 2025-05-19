``` python
---

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

```



-----
```python
# distance_vector.py

def distance_vector_routing(graph, source):
    # initialize all distances to infinity
    distance = {node: float('inf') for node in graph}
    distance[source] = 0

    # relax edges |V|−1 times
    for _ in range(len(graph) - 1):
        for u in graph:
            for v, w in graph[u].items():
                if distance[u] + w < distance[v]:
                    distance[v] = distance[u] + w

    return distance


if __name__ == "__main__":
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 7},
        'C': {'A': 4, 'B': 2, 'D': 3},
        'D': {'B': 7, 'C': 3}
    }

    result = distance_vector_routing(graph, 'A')
    print("Distance Vector Routing Conclusion:",result)

```

----

```python
from scapy.all import *

def packet_handler(packet):
    print(packet.summary())  # use summary for brief, or packet.show() for full dump

try:
    # Change 'Ethernet' to your actual interface name, e.g., 'eth0', 'wlan0', etc.
    packets = sniff(iface='Ethernet', prn=packet_handler, count=5)
except PermissionError:
    print("Error: You need root privileges to capture packets.")
except OSError as e:
    if "No such device" in str(e):
        print("Error: Interface 'Ethernet' not found. Please specify a valid network interface.")
    else:
        print(f"An unexpected error occurred: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

```
----
```python 
def crc(dividend, divisor):
    len_divisor = len(divisor)
    padded_dividend = dividend + '0' * (len_divisor - 1)
    padded_dividend = list(padded_dividend)

    for i in range(len(dividend)):
        if padded_dividend[i] == '1':
            for j in range(len_divisor):
                padded_dividend[i + j] = str(int(padded_dividend[i + j]) ^ int(divisor[j]))

    remainder = ''.join(padded_dividend[-(len_divisor - 1):])
    return remainder


data = '1101011'
divisor = '10011'
remainder = crc(data, divisor)
print("CRC Remainder:", remainder)

transmitted_data = data + remainder
print("Transmitted Data:", transmitted_data)
```
