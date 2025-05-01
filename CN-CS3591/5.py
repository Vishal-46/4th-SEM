from scapy.all import *

def packet_handler(packet):
    print(packet.show())

try:
    packets = sniff(iface='Wi-Fi', prn=packet_handler, count=5)
except PermissionError:
    print("Error: You need root/administrator privileges to capture packets.")
except OSError as e:
    if "No such device" in str(e):
        print("Error: Interface not found. Please specify a valid network interface.")
    else:
        print(f"An unexpected OS error occurred: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
