import time

ip = input("\n\033[1mEnter the ip address\033[0m (e.g. 192.168.0.1): ")
subnet_mask = input("\033[1mEnter the subnet mask\033[0m (e.g. 255.255.255.0): ")

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
print("\nNetwork Address:   ","\033[1m" + network + "\033[0m")
print("Broadcast Address: ","\033[1m" + broadcast + "\033[0m")
print("First IP Address:  ","\033[1m" + first_ip + "\033[0m")
print("Last IP Address:   ","\033[1m" + last_ip + "\033[0m")


print('\nReturning to main menu...', end='\r')
time.sleep(4)