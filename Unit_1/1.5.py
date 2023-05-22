with open("adv.txt", "r") as file:
    longest_name = max(file.read().split(), key=len)

print("The longest name in the file is:", longest_name)

with open("adv.txt", "r") as file:
    names = file.read().split()
    total_length = sum(len(name) for name in names)

print("The sum of the lengths of the names in the file is:", total_length)


with open("adv.txt", "r") as file:
    names = file.read().split()
    shortest_length = min(len(name) for name in names)
    shortest_names = [name for name in names if len(name) == shortest_length]

print("The shortest names in the file are:")
for name in shortest_names:
    print(name)


length = int(input("Enter the length of the name: "))
with open("names.txt", "r") as file:
    names = [name.strip() for name in file.readlines() if len(name.strip()) == length]
print('\n'.join(names))

