import scapy.all as s

# packet = s.IP(src = "192.168.1.70",dst = "192.168.1.0/24")/s.ICMP()
# ither = s.Ether(src = "3C:A6:F6:4A:32:05" ,dst= "ff:ff:ff:ff:ff:ff")
# packet1 = ither/packet
# answer,unanswer = s.srp(packet1)
# # print(packet.summary())
# for i in answer:
#     print('==========================================')
#     print(i.show()) 

# arp_request = s.Ether(dst = "ff:ff:ff:ff:ff:ff")/s.ARP( pdst = "192.168.1.0/24")
# d = s.srp(arp_request)[0]
# print(d)



# icmp = s.IP(dst= "192.168.1.100")/s.ICMP()
# c = s.sr1(icmp, timeout = 10,verbose = True)
# print(c.summary())
# 

# arp = s.Ether(dst = "ff:ff:ff:ff:ff:ff")/s.ARP(pdst = "192.168.1.0/24")
# ans, unasn= s.sendp(arp)
# print(ans.summary())
# print(arp.summary())
# ether = 
tcp = s.IP(dst = "192.168.1.65")/s.TCP(sport = 11111, dport =22)
ans= s.sr1(tcp, timeout = 1, verbose = True)
# print(tcp.show())
print(ans)



