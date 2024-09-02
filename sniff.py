import scapy.all as s
i = 0 
def print_packet_summary(packet):
    print((packet.summary()))
    # print("Source",packet[IP].src)


# sniff(iface = 'en0', prn=print_packet_summary,count = 5,filter = 'ARP')
c = s.sniff(iface = 'en0', count = 0,prn = print_packet_summary,filter = 'udp')
print((c.summary()))
# print(ls())
