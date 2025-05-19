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
