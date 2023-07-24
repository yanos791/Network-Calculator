import subprocess

while True:
    print("\nWhat conversion would you like to do?\n")
    print("\033[1m1.\033[0m Prefix to Subnet Mask/Wildcard Mask")
    print("\033[1m2.\033[0m Subnet Mask/Wildcard Mask to Prefix")
    print("\033[1m3.\033[0m Subnet Calculator")
    print("\033[1m4.\033[0m Exit\n")
    choice = input("Enter your choice: ")
    if choice == "1":
        subprocess.run(["python", "prefix-subnet.py"])
    if choice == "2":
        subprocess.run(["python", "subwild-prefix.py"])
    if choice == "3":
        subprocess.run(["python", "subnet-calculator.py"])
    if choice == "4":
        exit()
