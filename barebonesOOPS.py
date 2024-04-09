import random
import time

FruitsAndVegetables = [   "Chili Pepper - Habanero",
    "Chili Pepper - Serrano",
    "Lemon",
    "Lime",
    "Kiwi",
    "Pineapple",
    "Mango",
    "Peach",
    "Nectarine",
    "Apricot",
    "Cherry",
    "Plum",
    "Grapefruit",
    "Pomegranate",
    "Avocado",
    "Papaya",
    "Guava",
    "Durian",
    "Lychee",
    "Dragon Fruit",
    "Passion Fruit",
    "Tangerine",
    "Clementine",
    "Date",
    "Fig"
]

class quizz():

    def __init__(self, score=0):
        
        #defining the variables
        self.score = score

    def FruitAndVegQuizz(self):
     
        for i in range(5): #if it were and actual test, it would be 20

            RandomFruitOrVeg = FruitsAndVegetables[random.randint(0,24)]

            print("what is", RandomFruitOrVeg) #it just asks "what is avocado" in future with UI, it would be image
            answer = input("") #the user input
            if answer == RandomFruitOrVeg:
                self.score +=1
                time.sleep(0.5)
                i = i+1
                #this process checks if the user input is right
            else:
                time.sleep(0.5)
                print("you got", RandomFruitOrVeg, "wrong")
                time.sleep(0.5)
                i = i+1
                #if the user gets something wrong
        
        print("you got", self.score, '/ 20')



QuizzObject = quizz()

QuizzObject.FruitAndVegQuizz()

