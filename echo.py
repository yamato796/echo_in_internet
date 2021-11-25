import subprocess 
import time
import random

def tcpreplay(pcap, flag=""):
	command = f'tcpreplay -i en1 {flag} {pcap}.pcap '
	print(f'Playing {pcap}.pcap')
	ret = subprocess.run(command, shell=True, encoding='utf-8', timeout=10000)
	if ret.returncode == 0:
		print(f'Replay {pcap}.pcap sucessfully')
	else:
		print(f'Replay {pcap}.pcap failed !')

def tcprecord(pcap):
	command = f'tcpdump -i en1 -c 100 -w {pcap}.pcap '
	print(f'Recording {pcap}.pcap')
	ret = subprocess.run(command, shell=True, encoding='utf-8', timeout=10000)
	if ret.returncode == 0:
		print(f'Record {pcap}.pcap sucessfully')
	else:
		print(f'Record {pcap}.pcap failed !')

while True:
	try:
		for i in range(0,10):
			tcpreplay(f'confession_{random.randint(1,10)}', '-t')
			print(f'Wait for 1 seconds.....')
			time.sleep(1)	
		sec = random.randint(10,600)
		if sec % 100 ==0:
			tcprecord(f'confession_{random.randint(5,10)}')
		tcpreplay(f'confession_{random.randint(1,10)}')
		print(f'Wait for {sec} seconds.....')
		time.sleep(sec)
	except:
		pass
