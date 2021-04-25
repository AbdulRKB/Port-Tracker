#Libraries
import re, sys, nmap
from rich.console import Console

#Functions
IPv4_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
nm = nmap.PortScanner()
console = Console()

#Input
try:
	target = sys.argv[1]
	minPort = sys.argv[2]
	maxPort = sys.argv[3]
except IndexError:
	console.print(f'[yellow][+] Usage: python [red]{sys.argv[0]} [purple]<target> [blue]<port-start-range> <port-end-range>')
	sys.exit()

#Output
for port in range(int(minPort), int(maxPort)+1):
	try:
		connect = nm.scan(str(target), str(port))
		port_status = connect['scan'][target]['tcp'][port]['state']
		print(f'[yellow][+] Port {port} is {port_status}')
	except:
		print(f'[yellow][+] Cannot find port [red]{port}')
		sys.exit()
#Made by CyberTitus 2021
