from scapy.all import *

def packet_handler(packet):
    print(packet.summary())

try:
    # Use L3 socket as a workaround (no Ethernet layer)
    conf.L3socket
    packets = sniff(count=5, prn=packet_handler)
except Exception as e:
    print(f"An unexpected error occurred: {e}")
