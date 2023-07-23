print("Will you be entering a subnet mask or a wildcard mask?")
print("1. Subnet Mask")
print("2. Wildcard Mask")
mask_choice = input("Enter your choice: ")
if mask_choice == "1":
    subnet_mask = input("Enter the subnet mask (e.g. 255.255.255.0): ")

    mask_parts = subnet_mask.split('.')

    mask_binary = ''

    for i in mask_parts:
        mask_binary += '.'.join(bin(int(i))[2:].zfill(8))

    prefix = mask_binary.count('1')

    print("The prefix length is:", prefix)
if mask_choice == "2":
    wildcard_mask = input("Enter the wildcard mask (e.g. 0.0.0.255): ")

    mask_parts = wildcard_mask.split('.')

    mask_binary = ''

    for i in mask_parts:
        mask_binary += '.'.join(bin(int(i))[2:].zfill(8))

    prefix = mask_binary.count('0')

    print("The prefix length is:", prefix)



