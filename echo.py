import subprocess 
import time
import random

def tcpreplay(pcap):
	command = f'tcpreplay -i en1 -t {pcap}.pcap '
	print(f'Playing {pcap}.pcap')
	ret = subprocess.run(command, shell=True, encoding='utf-8', timeout=100)
	if ret.returncode == 0:
		print(f'Replay {pcap}.pcap sucessfully')
	else:
		print(f'Replay {pcap}.pcap failed !')

def tcprecord(pcap):
	command = f'tcpdump -i en1 -c 100 -w {pcap}.pcap '
	print(f'Recording {pcap}.pcap')
	ret = subprocess.run(command, shell=True, encoding='utf-8', timeout=100)
	if ret.returncode == 0:
		print(f'Record {pcap}.pcap sucessfully')
	else:
		print(f'Record {pcap}.pcap failed !')

while True:
	tcprecord(f'confession_{random.randint(5,10)}')
	tcpreplay(f'confession_{random.randint(1,4)}')
	time.sleep(600)