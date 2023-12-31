import time

prefix = int(input("\n\033[1mEnter the prefix:\033[0m "))
basic_subnet_mask = 4294967295
subnet = basic_subnet_mask - (2 ** (32 - prefix) - 1)
bin_subnet = bin(subnet)
bin_subnet = str(bin_subnet[2:])
bin_wildcard = 11111111111111111111111111111111 - int(bin_subnet)

bin_wildcard = str(bin_wildcard).zfill(32)

chunk_size = 8

chunks_subnet = []
chunks_wildcard = []

for i in range(0, 25, chunk_size):
    chunks_subnet.append(bin_subnet[i:i + chunk_size])
    chunks_wildcard.append(bin_wildcard[i:i + chunk_size])

for i in range(len(chunks_subnet)):
    chunks_subnet[i] = int(chunks_subnet[i], 2)
    chunks_wildcard[i] = int(chunks_wildcard[i], 2)

for i in range(len(chunks_subnet)):
    chunks_subnet[i] = str(chunks_subnet[i])
    chunks_wildcard[i] = str(chunks_wildcard[i])

chunks_subnet = '.'.join(chunks_subnet)
chunks_wildcard = '.'.join(chunks_wildcard)

print("\nThe subnet mask is:   " + "\033[1m" + chunks_subnet + "\033[0m")
print("The wildcard mask is: " + "\033[1m" + chunks_wildcard + "\033[0m")

print('\nReturning to main menu...\n', end='\r')
time.sleep(4)