import random

with open('FruitsAndVegetables.txt', 'r') as file:
    FruitsAndVegetables = file.readlines()

randomnum = random.randint(0,20)

print(FruitsAndVegetables[randomnum])