
from scapy.all import ARP, Ether, srp                   # srp-->  send recive packets 
def scan_networks(ip_range):  
    arp = ARP(pdst=ip_range)                            #pdst --> target ip
    ether_broadcast = Ether(dst="FF:FF:FF:FF:FF:FF")    #dst --> destination 
    send_packet = ether_broadcast / arp
    output = srp(send_packet, timeout=1, verbose=0)[0]
    devices = []
    for sent,received in output:
       devices.append({'ip': received.psrc, 'mac': received.hwsrc})     #psrc--> recievers  ip for arp request it is build in function
    return devices                                                      #hwsrc-->recievers  mac for arp request it is build in function
        
final_result = scan_networks("192.168.1.0/24")














        





        




