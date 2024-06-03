import customtkinter
from random import randint, sample
from PIL import Image
import re
import bcrypt
import pandas as pd
import csv
global score
score = 0


temp = ['yex67']

df = pd.read_csv('FruitsAndVegetables.csv', encoding='utf-8-sig')#Reading the CSV file into a DataFrame using pandas, i am unsure of how this works fully.

fruits_and_vegetables = df[['Name', 'Category', 'Image Location']].dropna().values.tolist()# Extract the relevant columns (Name, Category, Image Location) and drop any rows with missing values. CHATGPT helped with this.(a bit cheeky)

category_to_items = {} #Initialize an empty dictionary to group items by category, dictionaries are good because i groups items in pairs, which is essential for this usecase

for name, category, image_location in fruits_and_vegetables: #Loop through the list of fruits and vegetables
    if category not in category_to_items: #If the category is not already a key in the dictionary, add it with an empty list as its value
        category_to_items[category] = []
    category_to_items[category].append((name, image_location))  #Append the current item's name and image location to the list for its category


class Page:
    def __init__(self, master=None, use_frame=True):
        if master is None:
            self.app = customtkinter.CTk() #if there is no master, one will be created
        else:
            self.app = master #when a master is there, it uses it. This is useful for switching pages as it can change.
        self.app.geometry('600x600') #setting the geometry
        customtkinter.set_appearance_mode('light') #cool feature of customtkitner, allowing for themes
        customtkinter.set_default_color_theme('green') #chose green as it matches the 'fresh' vibe
        self.score = 0

        if use_frame:
            self.frame = customtkinter.CTkFrame(self.app, fg_color='white') #so, some of pages use the basic frame. Like loginpage and Registerpage. But some dont, like Quizpage. So i needed the ability to opt out.
            self.frame.pack(pady=20, padx=60, expand=True, fill='both') #setting the frame. Using pack so it looks nice

            for i in range(11): #setting the grid. 
                self.frame.grid_columnconfigure(i, weight=1) #setting the grids 11 times
                self.app.grid_columnconfigure(i, weight=1)
            for i in range(12):
                self.frame.grid_rowconfigure(i, weight=1) #same with the rows
                self.app.grid_rowconfigure(i, weight=1)
        else:
            self.frame = None #useful for apps that do not use frame

    def run(self):
        self.app.mainloop() #universal run method. good for debugging so i can skip the login process and needed as well, to run the app.

    def destroy_current_page(self): 
        for widget in self.app.winfo_children():
            widget.destroy() #the For loop loops through every widjet in the master and subsiquently destroys it.

    def show_page(self, page_class): #this destroys eveytihng and shows a different master/page.
        self.destroy_current_page()
        page_class(master=self.app) #here it is changing the page.  

class LoginPage(Page):
    def __init__(self, master=None):
        super().__init__(master)


        self.UsernameTextbox = customtkinter.CTkEntry(self.frame, placeholder_text='Username')
        self.PasswordTextbox = customtkinter.CTkEntry(self.frame, placeholder_text='Password', show = "•") #hiding the inputs
        #self.SignUpLabel = customtkinter.CTkLabel(master=self.frame, text='Dont have an account? Sign up here!', font=('inter', 10), text_color='green')
        self.Button1 = customtkinter.CTkButton(self.frame, text='')
        self.logo = customtkinter.CTkImage(light_image=Image.open('images/logo.png'), size=(275, 200))
        self.Label = customtkinter.CTkLabel(self.frame, text='', image=self.logo)
        #login button

        self.LoginButton = customtkinter.CTkButton(self.frame, text='login', command= lambda: self.CheckPW())
        #making a button look like a label so people can press it
        self.SignUpLabel = customtkinter.CTkButton(self.frame, text='Dont have an account? Sign up here!', 
                                           font=('inter', 10), 
                                           text_color='black', 
                                           fg_color='white', # background color of the button it blends in, used eyedropper tool on google
                                           hover_color='white', # background color on hover
                                           border_width=0, # no border
                                           corner_radius=0,
                                           command= lambda: self.show_page(RegisterPage)) # no rounded corners to mimic a label
        self.Label.pack(pady = 50, padx = 6)
        self.UsernameTextbox.pack(pady = 10, padx = 0)
        self.PasswordTextbox.pack(pady = 10, padx = 0)
        self.LoginButton.pack(pady = 10, padx = 10)
        self.SignUpLabel.pack(padx = 10, pady = 1)
   

    def CheckPW(self):
        df = pd.read_csv('user_data.csv') #opening the csv file
        username = self.UsernameTextbox.get() #getting the input
        user_row = df[df['Username'] == username] #finding the row with the username in it   
        if not user_row.empty: #checking if the row has the username in it, or is empty
            hashed_password = user_row.iloc[0]['Password'].encode('utf-8') #line location
            input_password = self.PasswordTextbox.get().encode('utf-8') #getting the password input
            if bcrypt.checkpw(input_password, hashed_password): #decrypting the hashing, and then finding out what it is so we can check it against the criteria
                self.show_page(HomePage) 
            else:
                pass

class RegisterPage(Page):
    def __init__(self, master=None):
        super().__init__(master)

        self.TitleLabel = customtkinter.CTkLabel(self.frame, text='HFM Learning Registration', font=('inter', 20)) #just all the widjets being intialised, not really anything special
        self.NameTextbox = customtkinter.CTkEntry(self.frame, placeholder_text="Enter username")
        self.PasswordTextBox = customtkinter.CTkEntry(self.frame, placeholder_text='Enter password', show='•')
        self.ConfirmPasswordTextBox = customtkinter.CTkEntry(self.frame, placeholder_text='Confirm Password', show='•')
        self.NoticeLabel = customtkinter.CTkLabel(self.frame, text='', font=('inter', 12), text_color='red')
        self.Progressbar = customtkinter.CTkProgressBar(self.frame)
        self.RegisterButton = customtkinter.CTkButton(self.frame, text='Register', command= lambda: self.RetrieveUserData()) #lambda is needed in order to delay the exectution untill a button press
        self.Backbutton = customtkinter.CTkButton(master=self.frame, text='✖', width=30, height=30, command=self.Exit)
        self.IncorrectLabel = customtkinter.CTkLabel(master=self.frame, text='')

        self.Backbutton.place(x=425,y=20) #button for exiting the pogram

        self.TitleLabel.pack(padx = 0, pady = 100) #states the title of the program

        self.NameTextbox.pack(padx = 0, pady = 10) #where you enter your username
        self.PasswordTextBox.pack(padx = 0, pady = 10) #where you enter your password
        self.ConfirmPasswordTextBox.pack(padx = 0, pady = 10) #confirm password

        self.RegisterButton.pack(padx = 0, pady = 10) #registration button
        self.Progressbar.pack(padx = 0, pady = 10) #password strength bar
        self.NoticeLabel.pack(padx = 0, pady = 10) #tells you if your password is bad.

        self.PasswordTextBox.bind("<KeyRelease>", self.PasswordStrengthChecker) #setting it to when a key is

        self.Progressbar.set(0)

    def Exit(self):
        self.show_page(LoginPage)

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
        with open('user_data.csv', 'r', newline='') as file:
            if self.NameTextbox.get() in file:
                file.readlines()
                self.NoticeLabel.configure(text='Username already taken, try again')
        if self.PasswordTextBox.get() != self.ConfirmPasswordTextBox.get():
            self.NoticeLabel.configure(text="The password has to be the same in both feilds")
        elif len(self.PasswordTextBox.get()) and len(self.PasswordTextBox.get()) <3:
            self.NoticeLabel.configure(text="Password/Username length must be greater than 3")
        elif len(self.NameTextbox.get()) > 12:
            self.NoticeLabel.configure(text="You username must be under 12 characters")
        else:    
            self.password = self.PasswordTextBox.get().encode('utf-8')  # Encode the password to bytes
            self.hashed_password = bcrypt.hashpw(self.password, bcrypt.gensalt())  #encryption through the bcrypt API
            with open('user_data.csv', 'a', newline='') as UserDataFile: #a+ means read and append
                writer = csv.writer(UserDataFile)
                UserDataFile.seek(0, 2) #this moves the file pointer to the end of the file
                if UserDataFile.tell() == 0: #checks if the fole is empty
                    writer.writerow('') #writing the data
                writer.writerow([self.NameTextbox.get(), self.hashed_password.decode('utf-8')])
                self.NoticeLabel.configure(text="Registration successful!", text_color='black')
                

                print(UserDataFile)
            
class HomePage(Page):
    def __init__(self, master=None):
        super().__init__(master, use_frame=False)

        self.test_completed = False

        self.MainFrame = customtkinter.CTkFrame(master=self.app, width=550, height=450) #the frame where the score information will be
        self.NameFrame = customtkinter.CTkFrame(master=self.app, width=550, height=100) #the frame where the user is welcomed
        self.NameLabel = customtkinter.CTkLabel(master=self.NameFrame, #the label which says "welcome, name"
                                                text=f'Welcome, {temp[0]}',
                                                font=('inter', 30))
        self.FVTestButton = customtkinter.CTkButton(master=self.MainFrame, #take the test button
                                                    width=500,
                                                    height=50,
                                                    text='Take your test',
                                                    font=('inter', 20),
                                                    command=lambda: self.show_page(QuizzPage))
        
        self.showscore = customtkinter.CTkLabel(master=self.MainFrame, #tells the user the score
                                                text="Your score is ",
                                                font=('inter', 16))
        self.score = customtkinter.CTkLabel(master=self.MainFrame, #score
                                            text=self.score,
                                            font=('inter', 16))
        
        self.NameFrame.pack(padx=25, pady=10)
        self.NameLabel.place(x=25,y=25)
        self.MainFrame.pack(pady=10, padx=25, expand=True, fill='both')

        self.FVTestButton.place(x=25, y=375)

class SuccessPage(HomePage):
    def __init__(self, master=None):
        super().__init__(master)
        global score

        self.FVTestButton.place_forget()

        self.FVTestButton = customtkinter.CTkButton(master=self.MainFrame, #take the test button
                                                    width=500,
                                                    height=50,
                                                    text='Okay',
                                                    font=('inter', 20),
                                                    command=lambda: self.show_page(QuizzPage))

        self.showscore = customtkinter.CTkLabel(master=self.MainFrame,
                                                text=(f'Your score is:'),
                                                font=('inter', 20))
        self.scorenumber = customtkinter.CTkLabel(master=self.MainFrame,
                                                  text=(f'{score}/20'),
                                                  font=('inter', 100))
        self.showscore.pack(padx = 25, pady = 30)
        self.FVTestButton.configure(text='Okay')
        self.scorenumber.pack(padx=25, pady=15)

        if score <=15:
            self.scorenumber.configure(text_color='#FFB833')
        elif score <=14:
            self.scorenumber.configure(text_color='#800020')
        else:
            self.scorenumber.configure(text_color='green')


    
class QuizzPage(Page):
    def __init__(self, master=None):
        super().__init__(master, use_frame=False)

        self.correct = False
        self.AnsweredQuestions = []

        self.QuizzFrame = customtkinter.CTkFrame(self.app, fg_color='white') #defining the frame
        self.ImageFrame = customtkinter.CTkFrame(self.app, fg_color='white')
            
        self.surveybutton1 = customtkinter.CTkButton(master=self.QuizzFrame, text='', width=275, height=50, command=lambda: self.ListeningIfCorrect(self.surveybutton1)) #setting this up so the paramater (clicked button works)
        self.surveybutton2 = customtkinter.CTkButton(master=self.QuizzFrame, text='', width=275, height=50, command=lambda: self.ListeningIfCorrect(self.surveybutton2)) #setting as lambda, so the function wont initiate untill the button is pressed
        self.surveybutton3 = customtkinter.CTkButton(master=self.QuizzFrame, text='', width=275, height=50, command=lambda: self.ListeningIfCorrect(self.surveybutton3))
        self.surveybutton4 = customtkinter.CTkButton(master=self.QuizzFrame, text='', width=275, height=50, command=lambda: self.ListeningIfCorrect(self.surveybutton4))
        

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

        self.ImageLabel = customtkinter.CTkLabel(master=self.ImageFrame, text='') #I intitialise this label as you cannot pack or grid the CTKimage, so this allows for image placement onto the self.frame
        
        self.surveybutton1.grid(column=5, row=6, padx=10, pady=5, sticky = 'nsew',  columnspan = 3) #placing the widjets on a grid that is defined within the page class
        self.surveybutton2.grid(column=8, row=6, padx=10, pady=5, sticky = 'nsew',  columnspan = 3)
        self.surveybutton3.grid(column=5, row=7, padx=10, pady=5, sticky = 'nsew',  columnspan = 3)
        self.surveybutton4.grid(column=8, row=7, padx=10, pady=5, sticky = 'nsew', columnspan = 3)
        
        self.ImageLabel.grid(column=5, row=5)

        self.UpdateQuestions()
    def select_random_category_items(self):
        category = sample(list(category_to_items.keys()), 1)[0] #converting the  categories to a list and randomly select one category
        selected_items = sample(category_to_items[category], 4) #Putting four items from the catagorty and putting it into a list as well
        return selected_items #returning the selected items to be used later


    def ListeningIfCorrect(self, clicked_button):

        self.correct = False #orgininally starts off as false
        global score

        if clicked_button._text == self.CorrectAnswer: #checking if the answer is right, a bit buggy for some reason it doesnt detect the paramater
                self.correct = True #if the correct label is correct
                score = score +1 #changes the score accordingly
                self.UpdateQuestions() #gives the user new questions
                self.AnsweredQuestions.append(self.CorrectAnswer)
        else:
            clicked_button.configure(text='✖') #informs the user if the answer is wrong, and makes them continue untill it is correct
            clicked_button.configure(fg_color='#800020', hover_color='#800020')
            self.AnsweredQuestions.append(self.CorrectAnswer)
     
    def UpdateQuestions(self):

            selected_items = self.select_random_category_items() #selecting a new set of items from the random catagory
            self.CumulatedNums = [item[0] for item in selected_items] #using a for loop, to place items in cumulated nums
            self.CorrectAnswer = self.CumulatedNums[randint(0, 3)] #randomly selecting one of them to be the answer
            
            image_location = [item[1] for item in selected_items if item[0] == self.CorrectAnswer][0] #Finding the image location of the correct answer and updates the image displayed in the quiz
            self.RefImage = customtkinter.CTkImage(light_image=Image.open(image_location), size=(250, 250)) #defining the referance image after this, however the label above is used to grid it.
            self.ImageLabel.configure(image=self.RefImage) #as you can see, it is being used in unicen.

            #Updating the text on the quiz buttons with the new set of items
            self.surveybutton1.configure(text=self.CumulatedNums[0], fg_color='#2cc984', hover_color='#09955b')
            self.surveybutton2.configure(text=self.CumulatedNums[1], fg_color='#2cc984', hover_color='#09955b')
            self.surveybutton3.configure(text=self.CumulatedNums[2], fg_color='#2cc984', hover_color='#09955b')
            self.surveybutton4.configure(text=self.CumulatedNums[3], fg_color='#2cc984', hover_color='#09955b')
            
            # Print out the correct answer for debugging purposes

            if score == 20:
                self.show_page(SuccessPage)
                self.testcompleted = True




if __name__ == "__main__": #name always == main so, its essentially a constant true variable
    Running = LoginPage() #initualising the Quizzpage as an object
    Running.run() #then running the run method through that so that the program pops up when your run the python file
    
