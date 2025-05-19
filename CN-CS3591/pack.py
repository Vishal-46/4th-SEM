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
