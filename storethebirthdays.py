# Raj's friends' birthdays

birthdays = {}

print("Enter the birthdays of Raj's five friends:")

for i in range(5):
    name = input(f"Enter name of friend {i+1}: ")
    birthday = input(f"Enter birthday of {name} (DD/MM/YYYY): ")
    birthdays[name] = birthday

print("\nBirthdays of Raj's Friends:")
for name, birthday in birthdays.items():
    print(name, ":", birthday)