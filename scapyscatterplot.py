from scapy.all import *
import matplotlib.pyplot as plt

ans, unans=sr(IP(dst="www.bbc.co.uk")/TCP(sport=[RandShort()]*1000), timeout=1)

#Incomplete
plt.scatter()

plt.show()