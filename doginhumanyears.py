dog_years = {
    # dog year & human years
    1: [15, 15, 15, 12],
    2: [24, 24, 24, 22],
    3: [28, 28, 28, 31],
    4: [32, 32, 32, 38],
    5: [36, 36, 36, 45],
    6: [40, 42, 45, 49],
    7: [44, 47, 50, 56],
    8: [48, 51, 55, 64],
    9: [52, 56, 61, 71],
    10: [56, 60, 66, 79],
    11: [60, 65, 72, 86],
    12: [64, 69, 77, 93],
    13: [68, 74, 82, 100],
    14: [72, 78, 88, 107],
    15: [76, 83, 93, 114],
    16: [80, 87, 99, 121]
}


def determine_index(size):
    if size == 's':
        return 0
    elif size == 'm':
        return 1
    elif size == 'l':
        return 2
    elif size == 'g':
        return 3
    else:
        return -1


print("Determine the size of your dog:: ")
print("Enter s if 20lbs or less")
print("Enter m if 21lbs to 50lbs")
print("Enter l if 51lbs or 100lbs")
print("Enter g if 100+lbs\n")

# deal with dog's size
# ask the size of dog from the user
dogSize = input("Enter the size of your dog: ")

while dogSize != 's' and dogSize != 'm' and dogSize != 'l' and dogSize != 'g':
    dogSize = input("Enter a valid answer for the size of your dog: ")

index = determine_index(dogSize)

# deal with dog's year
# ask the age of the dog
dogYear = int(input("Enter the age of your dog(between 1 and 16): "))

while dogYear < 1 or dogYear > 16:
    dogYear = int(input('Enter a valid age for your dog: '))

dogAgeInHumanYear = dog_years[dogYear]

print(f"\nYour dog is {dogAgeInHumanYear[index]} years old in human years.")
