from random import sample, randint

with open('FruitsAndVegetables.txt', 'r') as file:
    FruitsAndVegetables = [line.strip() for line in file.readlines()]  # Using strip() to remove newline characters

# Now sample 4 whole items (strings) from the list
CumulatedNums = sample(FruitsAndVegetables, 4)

print(CumulatedNums[1])
