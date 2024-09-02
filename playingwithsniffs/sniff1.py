from scapy.all import *
from scapy.all import IP,TCP,Ether,UDP,ARP,ICMP
from scapy.layers.inet6 import ICMPv6MRD_Solicitation as ICMPv6

from scapy.all import *


def print_sniffed_packet(packet):
    pkt_no = str(print_sniffed_packet.counter)
    pkt_time = str(packet.time)
    pkt_proto = packet.payload.name

    if IP in packet:
        pkt_dst = packet[IP].dst
        pkt_src = packet[IP].src

    elif Ether in packet:
        pkt_dst = packet[Ether].dst
        pkt_src = packet[Ether].src

    else:
        pkt_dst = "Unknown"
        pkt_src = "Unknown"
        pkt_proto = "Unknown"
    if TCP in packet:
        pkt_proto = "TCP"
    elif UDP in packet:
        pkt_proto = "UDP"
    elif ARP in packet:
        pkt_proto = "ARP"
    elif ICMP in packet:
        pkt_proto = "ICMPv6"    
    elif ICMPv6 in packet:
        pkt_proto = "ICMPv6"
        


    print("Packet {}: Time: {}, Destination: {}, Source: {}, Protocol: {}".format(pkt_no, pkt_time, pkt_dst, pkt_src, pkt_proto))
    print("===========================")

    print_sniffed_packet.counter += 1


print_sniffed_packet.counter = 1

captured = sniff(prn=print_sniffed_packet, count=0)



