import customtkinter
from random import randint, sample
from PIL import Image


with open('FruitsAndVegetables.txt', 'r') as file:
    FruitsAndVegetables = [line.strip() for line in file.readlines()]  # Using strip() to remove newline characters


class LoginPage():
    def __init__(self):

        #setting the variables

        self.app = customtkinter.CTk()
        self.app.geometry('400x400')

        #setting the colour theme

        customtkinter.set_appearance_mode('light')
        customtkinter.set_default_color_theme('green')

        #creating the main frame

        self.frame = customtkinter.CTkFrame(self.app)


        #textboxes

        self.Label = customtkinter.CTkLabel(master=self.frame, text="HFM Learning", font=('inter', 20))
        self.UsernameTextbox = customtkinter.CTkEntry(master=self.frame, placeholder_text='Username')
        self.PasswordTextbox = customtkinter.CTkEntry(master=self.frame, placeholder_text='Password', show = "•") #hiding the inputs
        self.SignUpLabel = customtkinter.CTkLabel(master=self.frame, text='Dont have an account? Sign up here!', font=('inter', 10), text_color='green')
        self.SignUpLabelButton = customtkinter.CTkButton(master=self.frame, text='')

        

        #login button

        self.LoginButton = customtkinter.CTkButton(master=self.frame, text='login')

        #setting the grid

        for i in range(11):
            self.frame.grid_columnconfigure(i, weight=1) #i is 11, same for next 1
        for i in range(12):
            self.frame.grid_rowconfigure(i, weight=1)   

        #placing the widgets into the app

        self.frame.pack(pady = 20, padx = 60, fill= 'both', expand = True)
        self.UsernameTextbox.grid(row = 7, column = 6, pady = 1, padx = 10)
        self.PasswordTextbox.grid(row = 8, column = 6, pady = 1, padx = 10)
        self.LoginButton.grid(row = 9, column = 6, pady = 1, padx = 10)
        self.SignUpLabel.grid(row = 10, column = 6, padx = 10, pady = 1)
        self.Label.grid(row = 4, column = 6)
        

    def run(self):
        self.app.mainloop()

    


class QuizzPage():
    def __init__(self):

       
        #setting the variables:
       
        self.randomnum = randint(0,5)
        self.last_num_of_array = True
        self.new_number_in_array = False
        self.correct = False
        self.CumulatedNums = sample(FruitsAndVegetables, 4)
        self.score = 0 

        #sorting cumulated nums

        self.CumulatedNums.sort()

        #setting the geometry, and app root
        
        self.app = customtkinter.CTk() 
        self.app.geometry('400x400')

        #cool feature, in CTK, allows a colour theme

        customtkinter.set_appearance_mode('light')
        customtkinter.set_default_color_theme('green')

        #setting the frames for the app

        self.answerframe = customtkinter.CTkFrame(master=self.app) #making the frame belong to this specific application. Hence master=self.app
        self.imageframe = customtkinter.CTkFrame(master=self.app) #the same here

        #setting the multiple choice buttons

        self.surveybutton1 = customtkinter.CTkButton(master=self.imageframe, text=self.CumulatedNums[0], command=lambda: self.commandss())
        self.surveybutton2 = customtkinter.CTkButton(master=self.imageframe, text=self.CumulatedNums[1], command=lambda: self.commandss())
        self.surveybutton3 = customtkinter.CTkButton(master=self.imageframe, text=self.CumulatedNums[2], command=lambda: self.commandss())
        self.surveybutton4 = customtkinter.CTkButton(master=self.imageframe, text=self.CumulatedNums[3], command=lambda: self.commandss())

        #temporary label that shows the answer

        self.label = customtkinter.CTkLabel(master=self.imageframe, text=self.CumulatedNums[randint(0,3)])
        self.RefImage = customtkinter.CTkImage(light_image=Image.open('images/broccoli.png'), size=(150,150))
        self.ImageLabel = customtkinter.CTkLabel(master=self.imageframe, text='', image=self.RefImage)

        #adding an image placeholder


        #placing the widjets into the frame, through the grid and pack system

        self.imageframe.pack(pady=10, padx=40, fill = 'both', expand = 'true')
        self.surveybutton1.grid(column=5, row=9, padx=7, pady=0) #have a very loose idea on how padx and pady work, sort just input values randomly untill to looks gud!
        self.surveybutton2.grid(column=8, row=9, padx=7, pady=0)
        self.surveybutton3.grid(column=5, row=10, padx=7, pady=0)
        self.surveybutton4.grid(column=8, row=10, padx=7, pady=0)
        self.label.grid(column = 7, row = 5, columnspan=2)
        self.ImageLabel.grid(column=5, row=5)

        #setting the grid, collumns and rows

        for i in range(11):
            self.imageframe.grid_columnconfigure(i, weight=1) #i is 11, same for next 1
        for i in range(12):
            self.imageframe.grid_rowconfigure(i, weight=1)   

    #function that gives a new question once answer is made, through the multiple choice buttons
        
    def commandss(self):
        
        if self.surveybutton1._text==self.label._text or self.surveybutton2._text==self.label._text or self.surveybutton3._text==self.label._text or self.surveybutton4._text==self.label._text:
            self.correct = True
            self.CumulatedNums.clear()
            self.score = self.score +1
            print(self.score)

            while len(self.CumulatedNums) == 0:
                while len(self.CumulatedNums) != 4:
                    self.CumulatedNums = sample(FruitsAndVegetables, 4)
                    
                    self.surveybutton1.configure(text=self.CumulatedNums[0])
                    self.surveybutton2.configure(text=self.CumulatedNums[1])
                    self.surveybutton3.configure(text=self.CumulatedNums[2])
                    self.surveybutton4.configure(text=self.CumulatedNums[3])

                    self.label.configure(text=self.CumulatedNums[randint(0,3)])
                    print(self.CumulatedNums)
        
                              
    #app.run, so when the file is executed the gui pops up
    
    def run(self):
        self.app.mainloop()

    

#creating an object out of quizpage so methods can be called

quizzpage = QuizzPage()
quizzpage.commandss()

quizzpage.run()

        