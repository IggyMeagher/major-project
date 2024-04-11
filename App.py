import customtkinter
from random import randint

FruitsAndVegetables = [   
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





class QuizzPage():
    def __init__(self):

        #setting the base properties for the application

        self.CumulatedNums = []
        self.last_num_of_array = True

        self.RandomNum1 = randint(0,21) #these are the random numbers to be used, for the labels of buttons. Hoping to have an algoritim better than this
        self.RandomNum2 = randint(0,21)
        self.RandomNum3 = randint(0,21)
        self.RandomNum4 = randint(0,21)

        self.CumulatedNums.append(self.RandomNum1) #appending the nums so they can be sorted
        self.CumulatedNums.append(self.RandomNum2)
        self.CumulatedNums.append(self.RandomNum3)
        self.CumulatedNums.append(self.RandomNum4)

        self.CumulatedNums.sort() #sorting

        #setting the geometry, might change later
        self.app = customtkinter.CTk() #.app just like gooeypie
        self.app.geometry('400x400')


        customtkinter.set_appearance_mode('light')
        customtkinter.set_default_color_theme('green')

        #defining a grid

        #grid cols


        #defining the widgets for the application

        self.answerframe = customtkinter.CTkFrame(master=self.app) #making the frame belong to this specific application. Hence master=self.app
        self.imageframe = customtkinter.CTkFrame(master=self.app) #the same here
        self.testbutton = customtkinter.CTkButton(master=self.imageframe, text='avocado')
        
        #survey buttons

        self.surveybutton1 = customtkinter.CTkButton(master=self.imageframe, text=FruitsAndVegetables[self.RandomNum1])
        self.surveybutton2 = customtkinter.CTkButton(master=self.imageframe, text=FruitsAndVegetables[self.RandomNum2])
        self.surveybutton3 = customtkinter.CTkButton(master=self.imageframe, text=FruitsAndVegetables[self.RandomNum3])
        self.surveybutton4 = customtkinter.CTkButton(master=self.imageframe, text=FruitsAndVegetables[self.RandomNum4])


        self.label = customtkinter.CTkLabel(master=self.imageframe, text=FruitsAndVegetables[self.RandomNum1])

        #pady
        

        self.imageframe.pack(pady=10, padx=40, fill = 'both', expand = 'true')
        
        self.surveybutton1.grid(column=5, row=9, padx=7, pady=0) #have a very loose idea on how padx and pady work, sort just input values randomly untill to looks gud!
        self.surveybutton2.grid(column=8, row=9, padx=7, pady=0)
        self.surveybutton3.grid(column=5, row=10, padx=7, pady=0)
        self.surveybutton4.grid(column=8, row=10, padx=7, pady=0)
        self.label.grid(column = 7, row = 5, columnspan=2)

        for i in range(11):
            self.imageframe.grid_columnconfigure(i, weight=1) #i is 11, same for next 1
        for i in range(12):
            self.imageframe.grid_rowconfigure(i, weight=1)


    def checkingiflastnumberinarray(self): #There was a list out of range issue, so i created this function.
        for i in range(len(self.CumulatedNums) -1): #its probably over engineered, but it check if the last num of the array and makes sure the arr doesnt go out of range
            if i == 4 and self.CumulatedNums[i] > self.CumulatedNums[i-1] and self.last_num_of_array == True:
                self.last_num_of_array = False #returning this, so the next for loop can run without any issues.
                

    def MakingSureNoRepeatedLabelsForButtons(self):  #checks if there are any repeated values, so they dont show up on the buttons

        for i in range(len(self.CumulatedNums) -1):
            if self.CumulatedNums[i] == self.CumulatedNums[i+1] and self.last_num_of_array == False: 
                self.CumulatedNums.pop(i) #if repeated number is evident, it gets removed
                i = i+1 #process is repeated.
                print(self.CumulatedNums)
            else:
                i = i+1
        
        
    
    def run(self):
        self.app.mainloop()



quizzpage = QuizzPage() #creating the object of login page from the original blueprint

quizzpage.MakingSureNoRepeatedLabelsForButtons()

quizzpage.run() #now it can run methods



        
