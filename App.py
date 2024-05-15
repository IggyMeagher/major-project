import customtkinter
from random import randint, sample
from PIL import Image
import os
import re
import bcrypt
import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('FruitsAndVegetables.csv', encoding='utf-8-sig')

# Extract the relevant columns
fruits_and_vegetables = df[['Name', 'Image Location']].dropna().values.tolist()

# Separate names and image paths
names = [item[0] for item in fruits_and_vegetables]
name_to_image = {item[0]: item[1] for item in fruits_and_vegetables}

class Page():
    def __init__(self, use_frame=True):
        self.app = customtkinter.CTk() #this is the app
        self.app.geometry('400x400') #how large the app is
        customtkinter.set_appearance_mode('light')  # Set appearance mode globally
        customtkinter.set_default_color_theme('green')  # Set theme globally

        if use_frame:
            self.frame = customtkinter.CTkFrame(self.app, fg_color ='white') #defining the frame
            self.frame.pack(pady=20, padx=60, expand=True, fill='both') #the frame is universal, hence within the page class

            for i in range(11): #acctually 12
                self.frame.grid_columnconfigure(i, weight=1,)#setting the grid, this is the columns
                self.app.grid_columnconfigure(i, weight=1)
            for i in range(12): #acctually 13
                self.frame.grid_rowconfigure(i, weight=1,) #and this is the rows
                self.app.grid_rowconfigure(i, weight=1)

    def run(self):
        self.app.mainloop()

class LoginPage(Page):
    def __init__(self):
        super().__init__()

        self.Label = customtkinter.CTkLabel(self.frame, text="HFM Learning", font=('inter', 20))
        self.UsernameTextbox = customtkinter.CTkEntry(self.frame, placeholder_text='Username')
        self.PasswordTextbox = customtkinter.CTkEntry(self.frame, placeholder_text='Password', show = "•") #hiding the inputs
        #self.SignUpLabel = customtkinter.CTkLabel(master=self.frame, text='Dont have an account? Sign up here!', font=('inter', 10), text_color='green')
        self.Button1 = customtkinter.CTkButton(self.frame, text='')

        #login button

        self.LoginButton = customtkinter.CTkButton(self.frame, text='login', command= lambda: self.CheckingDataBase())
        #making a button look like a label so people can press it
        self.SignUpLabel = customtkinter.CTkButton(self.frame, text='Dont have an account? Sign up here!', 
                                           font=('inter', 10), 
                                           text_color='black', 
                                           fg_color='white', # background color of the button it blends in, used eyedropper tool on google
                                           hover_color='white', # background color on hover
                                           border_width=0, # no border
                                           corner_radius=0) # no rounded corners to mimic a label
        
        self.UsernameTextbox.grid(row = 7, column = 6, pady = 1, padx = 10)
        self.PasswordTextbox.grid(row = 8, column = 6, pady = 1, padx = 10)
        self.LoginButton.grid(row = 9, column = 6, pady = 1, padx = 10)
        self.SignUpLabel.grid(row = 10, column = 6, padx = 10, pady = 1)
        self.Label.grid(row = 4, column = 6)
                


class RegisterPage(Page):
    def __init__(self):
        super().__init__()

        self.TitleLabel = customtkinter.CTkLabel(self.frame, text='HFM Learning Registration', font=('inter', 20))
        self.NameTextbox = customtkinter.CTkEntry(self.frame, placeholder_text="Enter full name")
        self.PasswordTextBox = customtkinter.CTkEntry(self.frame, placeholder_text='Enter password', show='•')
        self.ConfirmPasswordTextBox = customtkinter.CTkEntry(self.frame, placeholder_text='Confirm Password', show='•')
        self.NoticeLabel = customtkinter.CTkLabel(self.frame, text='', font=('inter', 12))
        self.Progressbar = customtkinter.CTkProgressBar(self.frame)
        self.RegisterButton = customtkinter.CTkButton(self.frame, text='Register', command= lambda: self.RetrieveUserData()) #lambda is needed in order to delay the exectution untill a button press


        self.TitleLabel.grid(row = 3, column = 6) #placing the widjets on a grid that is defined within the page class
        self.NameTextbox.grid(row = 5, column = 6)
        self.PasswordTextBox.grid(row = 6, column = 6)
        self.ConfirmPasswordTextBox.grid(row = 7, column = 6)
        self.RegisterButton.grid(row = 8, column = 6)
        self.Progressbar.grid(row = 9, column = 6)
        self.NoticeLabel.grid(row = 10, column = 6)

        self.PasswordTextBox.bind("<KeyRelease>", self.PasswordStrengthChecker) #setting it to when a key is

        self.Progressbar.set(0)

    def PasswordStrengthChecker(self):
        password = self.PasswordTextBox.get() #getting the password input
        strength = 0
        if re.search(r'[A-Z]', password): #searching for uppercase characters within the textbox
            strength += 1  
        if re.search(r'[a-z]', password): #same here but for lowercase
            strength += 1   
        if re.search(r'[0-9]', password): #same here but nums
            strength += 1  
        if re.search(r'[\W_]', password): #and special characters
            strength += 1  
        if len(password) >= 8:
            strength += 1            
        if strength <=1:
            self.NoticeLabel.configure(text="Password Strength low") #strength is the strength of the password, hence <1 would bew low
        elif strength <4:
            self.NoticeLabel.configure(text="Password Strength Moderate")
        elif strength >=4:
            self.NoticeLabel.configure(text="Password Stregnth Excellent")

        self.Progressbar.set(strength / 5.0)  #  the progress bar's range is 0.0 to 1.0
            
    
    def RetrieveUserData(self):  

            if self.PasswordTextBox.get() != self.ConfirmPasswordTextBox.get() and len(self.NameTextbox.get()) <3 and len(self.PasswordTextBox) <3:
                print("passwords need to match")
            else:    
                self.password = self.PasswordTextBox.get().encode('utf-8')  # Encode the password to bytes
                self.hashed_password = bcrypt.hashpw(self.password, bcrypt.gensalt())  #encryption through the bcrypt API
                directory = 'user_data'
                with open(os.path.join(directory, f"{self.NameTextbox.get()}.txt"), 'w') as file: #'w' means write
                    file.write(self.NameTextbox) #When writing to a file the DLL os doesn't allow for commas, in how i would usually do it. So I am using fstrings
                    file.write(self.hashed_password)

class QuizzPage(Page):
    def __init__(self):
        super().__init__(use_frame=False)


        self.correct = False
        self.CumulatedNums = sample(names, 4)
        self.score = 0
        self.AnsweredQuestions = []
        self.CorrectAnswer = self.CumulatedNums[randint(0,3)]

        self.QuizzFrame = customtkinter.CTkFrame(self.app, fg_color='white') #defining the frame
        self.ImageFrame = customtkinter.CTkFrame(self.app, fg_color='white')
            
        self.surveybutton1 = customtkinter.CTkButton(master=self.QuizzFrame, text=self.CumulatedNums[0],font=self.get_font(self.CumulatedNums[0]), command=lambda: self.ListeningIfCorrect(self.surveybutton1)) #setting this up so the paramater (clicked button works)
        self.surveybutton2 = customtkinter.CTkButton(master=self.QuizzFrame, text=self.CumulatedNums[1],font=self.get_font(self.CumulatedNums[0]), command=lambda: self.ListeningIfCorrect(self.surveybutton2)) #setting as lambda, so the function wont initiate untill the button is pressed
        self.surveybutton3 = customtkinter.CTkButton(master=self.QuizzFrame, text=self.CumulatedNums[2],font=self.get_font(self.CumulatedNums[0]), command=lambda: self.ListeningIfCorrect(self.surveybutton3))
        self.surveybutton4 = customtkinter.CTkButton(master=self.QuizzFrame, text=self.CumulatedNums[3],font=self.get_font(self.CumulatedNums[0]), command=lambda: self.ListeningIfCorrect(self.surveybutton4))

        #intialising the frames

        self.ImageFrame.pack(pady=5, padx=40, expand=True, fill='both') 
        self.QuizzFrame.pack(pady=10, padx=40, expand=False, fill='none')

        for i in range(11): #acctually 12
            self.ImageFrame.grid_columnconfigure(i, weight=1,)#setting the grid, this is the columns
            self.QuizzFrame.grid_columnconfigure(i, weight=1)
        for i in range(12): #acctually 13
            self.ImageFrame.grid_rowconfigure(i, weight=1,)#setting the grid, this is the columns
            self.QuizzFrame.grid_rowconfigure(i, weight=1)
            

        #temporary label that shows the answer

        self.RefImage = customtkinter.CTkImage(light_image=Image.open(name_to_image[self.CorrectAnswer]), size=(150,150)) #this is the uscase of the 'import pillow' api, allowing for the size= and light_image functionality
        self.ImageLabel = customtkinter.CTkLabel(master=self.ImageFrame, text='', image=self.RefImage) #I intitialise this label as you cannot pack or grid the CTKimage, so this allows for image placement onto the self.frame
        self.surveybutton1.grid(column=5, row=6, padx=10, pady=5) #placing the widjets on a grid that is defined within the page class
        self.surveybutton2.grid(column=8, row=6, padx=10, pady=5)
        self.surveybutton3.grid(column=5, row=7, padx=10, pady=5)
        self.surveybutton4.grid(column=8, row=7, padx=10, pady=5)
        self.ImageLabel.grid(column=5, row=5)

    def get_font(self, text):
        length = len(text)
        if length <= 5:
            return ('Helvetica', 14)
        elif length <= 10:
            return ('Helvetica', 13)
        elif length <= 15:
            return ('Helvetica', 12)
        else:
            return ('Helvetica', 8)
    

    def ListeningIfCorrect(self, clicked_button):
        
        self.correct = False #orgininally starts off as false

        if clicked_button._text == self.CorrectAnswer: #checking if the answer is right, a bit buggy for some reason it doesnt detect the paramater
                self.correct = True #if the correct label is correct
                self.score = self.score +1 #changes the score accordingly
                self.UpdateQuestions() #gives the user new questions
        else:
            clicked_button.configure(text='✖') #informs the user if the answer is wrong, and makes them continue untill it is correct
            clicked_button.configure(fg_color='#800020', hover_color='#800020')
        
    def UpdateQuestions(self):

        #changing the appropriate data

        self.CumulatedNums = sample(names, 4) #generating new questions
        self.CorrectAnswer = self.CumulatedNums[randint(0, 3)]
        print(self.AnsweredQuestions)
        
        #changing the image

        self.RefImage = customtkinter.CTkImage(light_image=Image.open(name_to_image[self.CorrectAnswer]), size=(150,150)) #update the image
        self.ImageLabel.configure(image=self.RefImage)

        #changing the buttons
       
        self.surveybutton1.configure(text=self.CumulatedNums[0],font=self.get_font(self.CumulatedNums[0]), fg_color='#2cc984', hover_color='#09955b') #changing the text of the buttons, when the answer is correct
        self.surveybutton2.configure(text=self.CumulatedNums[1],font=self.get_font(self.CumulatedNums[1]), fg_color='#2cc984', hover_color='#09955b')
        self.surveybutton3.configure(text=self.CumulatedNums[2],font=self.get_font(self.CumulatedNums[2]), fg_color='#2cc984', hover_color='#09955b')
        self.surveybutton4.configure(text=self.CumulatedNums[3],font=self.get_font(self.CumulatedNums[3]), fg_color='#2cc984', hover_color='#09955b')   
        print(self.CorrectAnswer)




if __name__ == "__main__": #name always == main so, its essentially a constant true variable
    Running = QuizzPage() #initualising the Quizzpage as an object
    Running.run() #then running the run method through that so that the program pops up when your run the python file
    
