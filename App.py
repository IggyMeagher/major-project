import customtkinter
from random import randint, sample
from PIL import Image
import os
import re
import bcrypt


with open('FruitsAndVegetables.txt', 'r') as file: #setting this globaly, for the methods to work
    FruitsAndVegetables = [line.strip() for line in file.readlines()]


class Page():
    def __init__(self):
        self.app = customtkinter.CTk()  # Changed from CTk("Ignatius App") as CTk does not take title here.
        self.frame = customtkinter.CTkFrame(self.app)
        self.app.geometry('400x400')
        customtkinter.set_appearance_mode('light')  # Set appearance mode globally
        customtkinter.set_default_color_theme('green')  # Set theme globally

        self.frame.pack(pady=20, padx=60, fill='both', expand=True)

        for i in range(11):
            self.frame.grid_columnconfigure(i, weight=1,)
        for i in range(12):
            self.frame.grid_rowconfigure(i, weight=1,)

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

        self.LoginButton = customtkinter.CTkButton(self.frame, text='login')
        #making a button look like a label so people can press it
        self.SignUpLabel = customtkinter.CTkButton(self.frame, text='Dont have an account? Sign up here!', 
                                           command=lambda: self.TransitionToRegister(),
                                           font=('inter', 10), 
                                           text_color='black', 
                                           fg_color='#dbdbdb', # background color of the button
                                           hover_color='#dbdbdb', # background color on hover
                                           border_width=0, # no border
                                           corner_radius=0) # no rounded corners to mimic a label
        
        self.UsernameTextbox.grid(row = 8, column = 6, pady = 1, padx = 10)
        self.PasswordTextbox.grid(row = 7, column = 6, pady = 1, padx = 10)
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

        self.Progressbar.set(0)

        self.TitleLabel.grid(row = 3, column = 6)
        self.NameTextbox.grid(row = 5, column = 6)
        self.PasswordTextBox.grid(row = 6, column = 6)
        self.ConfirmPasswordTextBox.grid(row = 7, column = 6)
        self.RegisterButton.grid(row = 8, column = 6)
        self.Progressbar.grid(row = 9, column = 6)
        self.NoticeLabel.grid(row = 10, column = 6)

    def PasswordStrengthChecker(self, event=None):
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
    
    def RetrieveUserData(self):  

            if self.PasswordTextBox.get() != self.ConfirmPasswordTextBox.get() and len(self.NameTextbox.get()) >=1:
                print("passwords need to match")
            else:    
                self.password = self.PasswordTextBox.get().encode('utf-8')  # Encode the password to bytes
                self.hashed_password = bcrypt.hashpw(self.password, bcrypt.gensalt())  #encryption through the bcrypt API
                directory = 'user_data'
                with open(os.path.join(directory, f"{self.NameTextbox.get()}.txt"), 'w') as file: #'w' means write
                    file.write(f'Fullname: {self.NameTextbox.get()} \n') #When writing to a file the DLL os doesn't allow for commas, in how i would usually do it. So I am using fstrings
                    file.write(f'Password: {self.hashed_password} \n')

class QuizzPage(Page):
    def __init__(self):
        super().__init__()

        self.correct = False
        self.CumulatedNums = sample(FruitsAndVegetables, 4)
        self.score = 0
        self.AnsweredQuestions = []
            
        self.surveybutton1 = customtkinter.CTkButton(master=self.frame, text=self.CumulatedNums[0], command=lambda: self.ListeningIfCorrect(self.surveybutton1)) #setting this up so the paramater (clicked button works)
        self.surveybutton2 = customtkinter.CTkButton(master=self.frame, text=self.CumulatedNums[1], command=lambda: self.ListeningIfCorrect(self.surveybutton2))
        self.surveybutton3 = customtkinter.CTkButton(master=self.frame, text=self.CumulatedNums[2], command=lambda: self.ListeningIfCorrect(self.surveybutton3))
        self.surveybutton4 = customtkinter.CTkButton(master=self.frame, text=self.CumulatedNums[3], command=lambda: self.ListeningIfCorrect(self.surveybutton4))

        #temporary label that shows the answer

        self.label = customtkinter.CTkLabel(master=self.frame, text=self.CumulatedNums[randint(0,3)])
        self.RefImage = customtkinter.CTkImage(light_image=Image.open('images/broccoli.png'), size=(150,150))
        self.ImageLabel = customtkinter.CTkLabel(master=self.frame, text='', image=self.RefImage)

        self.surveybutton1.grid(column=5, row=9, padx=7, pady=0) #have a very loose idea on how padx and pady work, sort just input values randomly untill to looks gud!
        self.surveybutton2.grid(column=8, row=9, padx=7, pady=0)
        self.surveybutton3.grid(column=5, row=10, padx=7, pady=0)
        self.surveybutton4.grid(column=8, row=10, padx=7, pady=0)
        self.label.grid(column = 7, row = 5, columnspan=2)
        self.ImageLabel.grid(column=5, row=5)
    

    def ListeningIfCorrect(self, clicked_button):
        
        self.correct = False #orgininally starts off as false

        if clicked_button._text == self.label._text: #checking if the answer is right, a bit buggy for some reason it doesnt detect the paramater
                self.correct = True #if the correct label is correct
                self.score = self.score +1 #changes the score accordingly
                self.AnsweredQuestions.append(self.label._text)
                self.UpdateQuestions() #gives the user new questions
        else:
            clicked_button.configure(text='✖') #informs the user if the answer is wrong, and makes them continue untill it is correct
        
    def UpdateQuestions(self):
        print(self.AnsweredQuestions)
        self.CumulatedNums = sample(FruitsAndVegetables, 4) #generating new questions
        self.label.configure(text=self.CumulatedNums[randint(0,3)]) #generating new answer
        self.surveybutton1.configure(text=self.CumulatedNums[0])
        self.surveybutton2.configure(text=self.CumulatedNums[1])
        self.surveybutton3.configure(text=self.CumulatedNums[2])
        self.surveybutton4.configure(text=self.CumulatedNums[3])   




if __name__ == "__main__":
    Running = QuizzPage()
    Running.run()
    
