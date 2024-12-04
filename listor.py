import os
os.system("cls")


my_numbers = [1, 2, 3, 4, 5, 6, 7, "hejo", 8]

print(my_numbers)

for numbers in my_numbers:
    print(numbers)

names = ["mrtouchytouchy", "gigarigga", "flingusbingus", "chinese_ninja"]

print(names)
print(len(names))

names.pop(2)
print(names)

names.append("tristina")

for name in names:
    print(name)
    
print(names[0])
exit()

candy_bars = ["twix", "snickers", "daim", "karlfazer"]
while True:
    os.system("cls")

    for bar in candy_bars:
        print(bar)

    #     new_bar = input("Lägg till choklad? ")
    # candy_bars.append(new_bar)

    print("\nVill du ändra något? ")
    position = input("vilken? ")
    if position:
        new_name = input("skriv nytt namn på chokladen ")
        candy_bars(int(position)) == new_name
        continue


