ip = input("Enter the ip address (e.g. 192.168.0.1): ")
subnet_mask = input("Enter the subnet mask (e.g. 255.255.255.0): ")

ip_octets = ip.split('.')
mask_octets = subnet_mask.split('.')

network = [int(ip_octets[i]) & int(mask_octets[i]) for i in range(4)]
broadcast = [int(ip_octets[i]) | (255 - int(mask_octets[i])) for i in range(4)]

last_ip = broadcast
first_ip = network

network = ".".join(str(i) for i in network)
broadcast = ".".join(str(i) for i in broadcast)
last_ip[3] = last_ip[3] - 1
first_ip[3] = first_ip[3] + 1
last_ip = ".".join(str(i) for i in last_ip)
first_ip = ".".join(str(i) for i in first_ip)
print("Network Address: ",network)
print("Broadcast Address: ",broadcast)
print("First IP Address: ",first_ip)
print("Last IP Address: ",last_ip)