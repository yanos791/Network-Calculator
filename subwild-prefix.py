import time

print("\nWill you be entering a subnet mask or a wildcard mask?")
print("\n\033[1m1.\033[0m Subnet Mask")
print("\033[1m2.\033[0m Wildcard Mask\n")
mask_choice = input("Enter your choice: ")
if mask_choice == "1":
    subnet_mask = input("\n\033[1mEnter the subnet mask\033[0m (e.g. 255.255.255.0): ")

    mask_parts = subnet_mask.split('.')

    mask_binary = ''

    for i in mask_parts:
        mask_binary += '.'.join(bin(int(i))[2:])

    prefix = mask_binary.count('1')

    print("The prefix length is:", "\033[1m" + str(prefix) + "\033[0m")
if mask_choice == "2":
    wildcard_mask = input("\033[1mEnter the wildcard mask\033[0m (e.g. 0.0.0.255): ")

    mask_parts = wildcard_mask.split('.')

    mask_binary = ''

    for i in mask_parts:
        mask_binary += '.'.join(bin(int(i))[2:].zfill(8))

    prefix = mask_binary.count('0')

    print("The prefix length is:", "\033[1m" + str(prefix) + "\033[0m")

print('\nReturning to main menu...', end='\r')
time.sleep(4)

