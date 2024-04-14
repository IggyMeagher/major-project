import customtkinter
from random import randint, sample

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
    "Dragonfruit",
    "Passionfruit",
    "Tangerine",
    "Clementine",
    "Date",
    "Fig"
]





class QuizzPage():
    def __init__(self):

        #setting the base properties for the application

       
        self.last_num_of_array = True
        self.new_number_in_array = False
        self.correct = False


        self.CumulatedNums = []

        self.CumulatedNums.append(sample(FruitsAndVegetables, 4))

        

        self.CumulatedNums.sort() #sorting

        #setting the geometry, might change later
        self.app = customtkinter.CTk() #.app just like gooeypie
        self.app.geometry('400x400')


        customtkinter.set_appearance_mode('light')
        customtkinter.set_default_color_theme('green')

    

        self.answerframe = customtkinter.CTkFrame(master=self.app) #making the frame belong to this specific application. Hence master=self.app
        self.imageframe = customtkinter.CTkFrame(master=self.app) #the same here
        
        #survey buttons

        

        self.surveybutton1 = customtkinter.CTkButton(master=self.imageframe, text=self.CumulatedNums[0][0], command=lambda: self.commandss())
        self.surveybutton2 = customtkinter.CTkButton(master=self.imageframe, text=self.CumulatedNums[0][1], command=lambda: self.commandss())
        self.surveybutton3 = customtkinter.CTkButton(master=self.imageframe, text=self.CumulatedNums[0][2], command=lambda: self.commandss())
        self.surveybutton4 = customtkinter.CTkButton(master=self.imageframe, text=self.CumulatedNums[0][3], command=lambda: self.commandss())

        print(self.CumulatedNums)

    


        self.label = customtkinter.CTkLabel(master=self.imageframe, text=self.CumulatedNums[0][randint(0,3)])

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

    def ensure_unique_numbers(self):
        # Track the indexes that have been used
        seen = set()
        for i in range(len(self.CumulatedNums)):
            while self.CumulatedNums[i] in seen:
                self.CumulatedNums[i] = randint(0, 21)  # Generate new number if duplicate
            seen.add(self.CumulatedNums[i])
    
    # Now update the buttons with the new unique numbers
        self.surveybutton1.configure(text=FruitsAndVegetables[self.CumulatedNums[0][0]])
        self.surveybutton2.configure(text=FruitsAndVegetables[self.CumulatedNums[0][1]])
        self.surveybutton3.configure(text=FruitsAndVegetables[self.CumulatedNums[0][2]])
        self.surveybutton4.configure(text=FruitsAndVegetables[self.CumulatedNums[0][3]])
        


    def checkingiflastnumberinarray(self): #There was a list out of range issue, so i created this function.
        for i in range(len(self.CumulatedNums) -1): #its probably over engineered, but it check if the last num of the array and makes sure the arr doesnt go out of range
            if i == 4 and self.CumulatedNums[i] > self.CumulatedNums[i-1] and self.last_num_of_array == True:
                self.last_num_of_array = False #returning this, so the next for loop can run without any issues.
    
        
    def commandss(self):
        
        if self.surveybutton1._text==self.label._text or self.surveybutton2._text==self.label._text or self.surveybutton3._text==self.label._text or self.surveybutton4._text==self.label._text:
            self.correct = True
            self.CumulatedNums.clear()

            while len(self.CumulatedNums) == 0:
                while len(self.CumulatedNums) != 4:
                    self.CumulatedNums.append(sample(FruitsAndVegetables, 4))
                    
                    self.surveybutton1.configure(text=self.CumulatedNums[0][0])
                    self.surveybutton2.configure(text=self.CumulatedNums[0][1])
                    self.surveybutton3.configure(text=self.CumulatedNums[0][2])
                    self.surveybutton4.configure(text=self.CumulatedNums[0][3])

                    self.label.configure(text=self.CumulatedNums[0][randint(0,3)])
                              
        

        print(self.CumulatedNums)

    
    def run(self):
        self.app.mainloop()

    



quizzpage = QuizzPage() #creating the object of login page from the original blueprint





quizzpage.commandss()
quizzpage.checkingiflastnumberinarray()
quizzpage.run() #now it can run methods



        
