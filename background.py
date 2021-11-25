import subprocess 
import time
import random

def tcpreplay(pcap, flag=""):
	command = f'tcpreplay -i en1 {flag} {pcap}.pcap '
	print(f'Playing {pcap}.pcap')
	ret = subprocess.run(command, shell=True, encoding='utf-8', timeout=1000)

while True:
	tcpreplay(f'confession_{random.randint(1,10)}')
	time.sleep(30)