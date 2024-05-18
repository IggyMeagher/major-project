import customtkinter
from random import randint, sample
from PIL import Image
import os
import re
import bcrypt
import pandas as pd

# Read the CSV file into a DataFrame using pandas
df = pd.read_csv('FruitsAndVegetables.csv', encoding='utf-8-sig')
# Extract the relevant columns (Name, Category, Image Location) and drop any rows with missing values
fruits_and_vegetables = df[['Name', 'Category', 'Image Location']].dropna().values.tolist()

# Initialize an empty dictionary to group items by category
category_to_items = {}

# Loop through the list of fruits and vegetables
for name, category, image_location in fruits_and_vegetables:
    if category not in category_to_items:
        category_to_items[category] = []
    category_to_items[category].append((name, image_location))


class Page:
    def __init__(self, master=None, use_frame=True):
        if master is None:
            self.app = customtkinter.CTk()
        else:
            self.app = master
        self.app.geometry('600x600')
        customtkinter.set_appearance_mode('light')
        customtkinter.set_default_color_theme('green')

        if use_frame:
            self.frame = customtkinter.CTkFrame(self.app, fg_color='white')
            self.frame.pack(pady=20, padx=60, expand=True, fill='both')

            for i in range(11):
                self.frame.grid_columnconfigure(i, weight=1)
                self.app.grid_columnconfigure(i, weight=1)
            for i in range(12):
                self.frame.grid_rowconfigure(i, weight=1)
                self.app.grid_rowconfigure(i, weight=1)
        else:
            self.frame = None

    def run(self):
        self.app.mainloop()

    def destroy_current_page(self):
        for widget in self.app.winfo_children():
            widget.destroy()

    def show_page(self, page_class):
        self.destroy_current_page()
        page_class(master=self.app)


class LoginPage(Page):
    def __init__(self, master=None):
        super().__init__(master)

        self.UsernameTextbox = customtkinter.CTkEntry(self.frame, placeholder_text='Username')
        self.PasswordTextbox = customtkinter.CTkEntry(self.frame, placeholder_text='Password', show="•")
        self.Button1 = customtkinter.CTkButton(self.frame, text='')
        self.logo = customtkinter.CTkImage(light_image=Image.open('images/logo.png'), size=(275, 200))
        self.Label = customtkinter.CTkLabel(self.frame, text='', image=self.logo)

        self.LoginButton = customtkinter.CTkButton(self.frame, text='login', command=self.CheckPW)
        self.SignUpLabel = customtkinter.CTkButton(self.frame, text='Dont have an account? Sign up here!',
                                                   font=('inter', 10),
                                                   text_color='black',
                                                   fg_color='white',
                                                   hover_color='white',
                                                   border_width=0,
                                                   corner_radius=0,
                                                   command=lambda: self.show_page(RegisterPage))

        self.Label.pack(pady=50, padx=6)
        self.UsernameTextbox.pack(pady=10, padx=0)
        self.PasswordTextbox.pack(pady=10, padx=0)
        self.LoginButton.pack(pady=10, padx=10)
        self.SignUpLabel.pack(padx=10, pady=1)

    def CheckPW(self):
        if not os.path.exists(f'user_data/{self.UsernameTextbox.get()}.txt'):
            print("get out")
            return

        with open(f'user_data/{self.UsernameTextbox.get()}.txt', 'r') as file:
            file_lines = file.readlines()

        login_password = self.PasswordTextbox.get().encode('utf-8')
        stored_hashed_password = file_lines[1].strip().encode('utf-8')

        if bcrypt.checkpw(login_password, stored_hashed_password):
            self.show_page(QuizzPage)


class RegisterPage(Page):
    def __init__(self, master=None):
        super().__init__(master)

        self.TitleLabel = customtkinter.CTkLabel(self.frame, text='HFM Learning Registration', font=('inter', 20))
        self.NameTextbox = customtkinter.CTkEntry(self.frame, placeholder_text="Enter username")
        self.PasswordTextBox = customtkinter.CTkEntry(self.frame, placeholder_text='Enter password', show='•')
        self.ConfirmPasswordTextBox = customtkinter.CTkEntry(self.frame, placeholder_text='Confirm Password', show='•')
        self.NoticeLabel = customtkinter.CTkLabel(self.frame, text='', font=('inter', 12))
        self.Progressbar = customtkinter.CTkProgressBar(self.frame)
        self.RegisterButton = customtkinter.CTkButton(self.frame, text='Register', command=self.RetrieveUserData)
        self.Backbutton = customtkinter.CTkButton(master=self.frame, text='✖', width=30, height=30, command=lambda: self.show_page(LoginPage))

        self.Backbutton.place(x=425, y=20)
        self.TitleLabel.pack(padx=0, pady=100)
        self.NameTextbox.pack(padx=0, pady=10)
        self.PasswordTextBox.pack(padx=0, pady=10)
        self.ConfirmPasswordTextBox.pack(padx=0, pady=10)
        self.RegisterButton.pack(padx=0, pady=10)
        self.Progressbar.pack(padx=0, pady=10)
        self.NoticeLabel.pack(padx=0, pady=10)

        self.PasswordTextBox.bind("<KeyRelease>", self.PasswordStrengthChecker)

        self.Progressbar.set(0)

    def PasswordStrengthChecker(self, event):
        password = self.PasswordTextBox.get()
        strength = 0
        if re.search(r'[A-Z]', password):
            strength += 1
        if re.search(r'[a-z]', password):
            strength += 1
        if re.search(r'[0-9]', password):
            strength += 1
        if re.search(r'[\W_]', password):
            strength += 1
        if len(password) >= 8:
            strength += 1
        if strength <= 1:
            self.NoticeLabel.configure(text="Password Strength low")
        elif strength < 4:
            self.NoticeLabel.configure(text="Password Strength Moderate")
        elif strength >= 4:
            self.NoticeLabel.configure(text="Password Strength Excellent")

        self.Progressbar.set(strength / 5.0)

    def RetrieveUserData(self):
        if self.PasswordTextBox.get() != self.ConfirmPasswordTextBox.get() or len(self.NameTextbox.get()) < 3 or len(self.PasswordTextBox.get()) < 3:
            print("passwords need to match")
        else:
            self.password = self.PasswordTextBox.get().encode('utf-8')
            self.hashed_password = bcrypt.hashpw(self.password, bcrypt.gensalt())
            directory = 'user_data'
            if not os.path.exists(directory):
                os.makedirs(directory)
            with open(os.path.join(directory, f"{self.NameTextbox.get()}.txt"), 'w') as file:
                file.write(f'{self.NameTextbox.get()}\n')
                file.write(self.hashed_password.decode('utf-8'))


class HomePage(Page):
    def __init__(self, master=None):
        super().__init__(master, use_frame=True)

        self.MainFrame = customtkinter.CTkFrame(master=self.app, fg_color='white')
        self.MainFrame.pack(pady=20, padx=60, expand=True, fill='both')

        self.label = customtkinter.CTkLabel(self.MainFrame, text='Home Page', font=('Arial', 24))
        self.label.pack(pady=20)

        self.navigate_button = customtkinter.CTkButton(self.MainFrame, text='Go to Quiz Page', command=lambda: self.show_page(QuizzPage))
        self.navigate_button.pack(pady=10)


class QuizzPage(Page):
    def __init__(self, master=None):
        super().__init__(master, use_frame=False)

        self.correct = False
        self.score = 0
        self.AnsweredQuestions = []

        self.QuizzFrame = customtkinter.CTkFrame(self.frame, fg_color='white')
        self.ImageFrame = customtkinter.CTkFrame(self.frame, fg_color='white')

        self.surveybutton1 = customtkinter.CTkButton(master=self.QuizzFrame, text='', command=lambda: self.ListeningIfCorrect(self.surveybutton1))
        self.surveybutton2 = customtkinter.CTkButton(master=self.QuizzFrame, text='', command=lambda: self.ListeningIfCorrect(self.surveybutton2))
        self.surveybutton3 = customtkinter.CTkButton(master=self.QuizzFrame, text='', command=lambda: self.ListeningIfCorrect(self.surveybutton3))
        self.surveybutton4 = customtkinter.CTkButton(master=self.QuizzFrame, text='', command=lambda: self.ListeningIfCorrect(self.surveybutton4))

        self.ImageFrame.pack(pady=5, padx=40, expand=True, fill='both')
        self.QuizzFrame.pack(pady=10, padx=40, expand=False, fill='none')

        for i in range(11):
            self.ImageFrame.grid_columnconfigure(i, weight=1)
            self.QuizzFrame.grid_columnconfigure(i, weight=1)
        for i in range(12):
            self.ImageFrame.grid_rowconfigure(i, weight=1)
            self.QuizzFrame.grid_rowconfigure(i, weight=1)

        self.ImageLabel = customtkinter.CTkLabel(master=self.ImageFrame, text='')

        self.surveybutton1.grid(column=5, row=6, padx=10, pady=5, sticky='nsew', columnspan=3)
        self.surveybutton2.grid(column=8, row=6, padx=10, pady=5, sticky='nsew', columnspan=3)
        self.surveybutton3.grid(column=5, row=7, padx=10, pady=5, sticky='nsew', columnspan=3)
        self.surveybutton4.grid(column=8, row=7, padx=10, pady=5, sticky='nsew', columnspan=3)

        self.ImageLabel.grid(column=5, row=5)

        self.UpdateQuestions()

    def select_random_category_items(self):
        category = sample(list(category_to_items.keys()), 1)[0]
        selected_items = sample(category_to_items[category], 4)
        return selected_items

    def ListeningIfCorrect(self, clicked_button):
        self.correct = False

        if clicked_button.cget("text") == self.CorrectAnswer:
            self.correct = True
            self.score += 1
            self.UpdateQuestions()
            self.AnsweredQuestions.append(self.CorrectAnswer)
        else:
            clicked_button.configure(text='✖')
            clicked_button.configure(fg_color='#800020', hover_color='#800020')

    def UpdateQuestions(self):
        if self.score == 20:
            exit()

        selected_items = self.select_random_category_items()
        self.CumulatedNums = [item[0] for item in selected_items]
        self.CorrectAnswer = self.CumulatedNums[randint(0, 3)]

        image_location = [item[1] for item in selected_items if item[0] == self.CorrectAnswer][0]
        self.RefImage = customtkinter.CTkImage(light_image=Image.open(image_location), size=(250, 250))
        self.ImageLabel.configure(image=self.RefImage)

        self.surveybutton1.configure(text=self.CumulatedNums[0], fg_color='#2cc984', hover_color='#09955b')
        self.surveybutton2.configure(text=self.CumulatedNums[1], fg_color='#2cc984', hover_color='#09955b')
        self.surveybutton3.configure(text=self.CumulatedNums[2], fg_color='#2cc984', hover_color='#09955b')
        self.surveybutton4.configure(text=self.CumulatedNums[3], fg_color='#2cc984', hover_color='#09955b')

        print(self.CorrectAnswer)


if __name__ == "__main__":
    app = LoginPage()
    app.run()
