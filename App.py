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

        self.app = customtkinter.CTk()
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

        self.surveybutton1 = customtkinter.CTkButton(master=self.imageframe, text=FruitsAndVegetables[randint(0,20)])
        self.surveybutton2 = customtkinter.CTkButton(master=self.imageframe, text=FruitsAndVegetables[randint(0,20)])
        self.surveybutton3 = customtkinter.CTkButton(master=self.imageframe, text=FruitsAndVegetables[randint(0,20)])
        self.surveybutton4 = customtkinter.CTkButton(master=self.imageframe, text=FruitsAndVegetables[randint(0,20)])

        #pady
        

        self.imageframe.pack(pady=10, padx=40, fill = 'both', expand = 'true')
        
        self.surveybutton1.grid(column=5, row=9, padx=7, pady=0)
        self.surveybutton2.grid(column=8, row=9, padx=7, pady=0)
        self.surveybutton3.grid(column=5, row=10, padx=7, pady=0)
        self.surveybutton4.grid(column=8, row=10, padx=7, pady=0)

        for i in range(11):
            self.imageframe.grid_columnconfigure(i, weight=1, minsize=0)  # reduced minsize for closer placement
        for i in range(12):
            self.imageframe.grid_rowconfigure(i, weight=1, minsize=0)


    def run(self):
        self.app.mainloop()



QuizzPage = QuizzPage() #creating the object of login page from the original blueprint
QuizzPage.run() #now it is an object, we can utilise the run() method

        
