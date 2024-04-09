import customtkinter

class QuizzPage():
    def __init__(self):

        #setting the base properties for the application

        self.app = customtkinter.CTk()
        self.app.geometry('500x350')
        customtkinter.set_appearance_mode('light')
        customtkinter.set_default_color_theme('green')

        #defining a grid

        #grid cols

        self.app.columnconfigure((0,1,2,3,4,5,6,7,8,9), weight=1) #for some reason it indexes from 0, so this is in fact, grid 1 

        #grid rows

        self.app.rowconfigure((0,1,2,3,4,5,6,7,8,9), weight=1) #again indexes from 0 


        #defining the widgets for the application

        self.answerframe = customtkinter.CTkFrame(master=self.app, width=450, height=125) #making the frame belong to this specific application. Hence master=self.app
        self.imageframe = customtkinter.CTkFrame(master=self.app) #the same here

        self.testbutton = customtkinter.CTkButton(master=self.imageframe, text='avocado')

        #pady

        self.answerframe.grid(row = 1, column = 5, ipadx = 10, ipady = 20)

    def run(self):
        self.app.mainloop()



QuizzPage = QuizzPage() #creating the object of login page from the original blueprint
QuizzPage.run() #now it is an object, we can utilise the run() method

        
