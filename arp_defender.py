instalation prosess

mkdir arp_defender
cd arp_defender
nano arp_defender.py
Paste the full updated script inside it.

Save and exit (Ctrl + O, Enter, then Ctrl + X in nano).
  pip install scapy requests
chmod +x arp_defender.py
sudo python3 arp_defender.py
you should see
  [*] Monitoring ARP packets on interface: eth0
logs are stored at
  logs/arp_defender.log
cat logs/arp_defender.log 
  __________________________________________________________________________________________________.
To simulate ARP spoofing:

Use another device or virtual machine with arpspoof:

arpspoof -i eth0 -t <target IP> <gateway IP>
