import scapy.all as s
# from what i understadn scapy module is used in packet mainpulation
transport_layer = s.TCP(sport = 35000, dport = 443)
network_layer = s.IP(src = "192.168.1.70" ,dst = "8.8.8.8", ttl = 70)  #ttl is time to live means how many hops tthe packet will do before getting discarded by the router.
print(network_layer)
# print(a.src) #the src stands for source
c = network_layer/transport_layer
link_layer = s.Ether(src = "3C:A6:F6:4A:32:05")
# print(s.ls(datalink_layer))
d = link_layer/ c
print(c.summary()) #the summary shows a only a line summary of the packet where as the
print(c.show()) #show commands shoes the full packet
# print(d.shwow())
# print(s.sr(d).show())
# print(s.ls(c))


#the / is fo r stacking layers so hwat it means is that a packet will have a ip or ther header with a protocol herader so the / helps you to stack both of them together before send them  on the network. 


# so 











