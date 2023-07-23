import subprocess

print("What conversion would you like to do?")
print("1. Prefix to Subnet Mask/Wildcard Mask")
print("2. Subnet Mask/Wildcard Mask to Prefix")
print("3. Subnet Calculator")
print("4. Exit")
choice = input("Enter your choice: ")
if choice == "1":
    subprocess.run(["python", "prefix-subnet.py"])
if choice == "2":
    subprocess.run(["python", "subwild-prefix.py"])
if choice == "3":
    subprocess.run(["python", "subnet-calculator.py"])
