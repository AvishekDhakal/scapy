import scapy.all as s
from scapy.all import ls,Ether,TCP
e = Ether()
d = s.Ether()/s.IP(dst = "www.google.com")/TCP(sport = 50000, flags = "R")
print(ls(Ether))
# print(s.Ether.summary())
c = e.show()
# print(c)
print(type(c))
print(type(Ether))
print(type(s.IP))
print(d.summary())




#so the conclusion is a packet to be sent out on the network is build with a Ether() /network layer/TCP()

# if you want to find the arguments take by each class in the scapy you should simply go to another terminal type scapy and do ls(Ether) 