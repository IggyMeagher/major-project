import customtkinter
from random import randint, sample
from PIL import Image

with open('FruitsAndVegetables.txt', 'r') as file:
    FruitsAndVegetables = [line.strip() for line in file.readlines()]

class QuizzPage():
    def __init__(self):
        self.app = customtkinter.CTk()
        self.app.geometry('400x400')
        customtkinter.set_appearance_mode('light')
        customtkinter.set_default_color_theme('green')

        self.imageframe = customtkinter.CTkFrame(master=self.app)
        self.imageframe.pack(pady=10, padx=40, fill='both', expand=True)

        # Sample four unique items from FruitsAndVegetables
        self.CumulatedNums = sample(FruitsAndVegetables, 4)
        self.correct_answer = self.CumulatedNums[randint(0, 3)]  # Choose a correct answer randomly from the sampled items

        # Buttons for the quiz
        self.surveybutton1 = customtkinter.CTkButton(master=self.imageframe, text=self.CumulatedNums[0], command=lambda: self.Refresh(self.surveybutton1))
        self.surveybutton2 = customtkinter.CTkButton(master=self.imageframe, text=self.CumulatedNums[1], command=lambda: self.Refresh(self.surveybutton2))
        self.surveybutton3 = customtkinter.CTkButton(master=self.imageframe, text=self.CumulatedNums[2], command=lambda: self.Refresh(self.surveybutton3))
        self.surveybutton4 = customtkinter.CTkButton(master=self.imageframe, text=self.CumulatedNums[3], command=lambda: self.Refresh(self.surveybutton4))
        self.surveybutton1.grid(column=5, row=9, padx=7, pady=0)
        self.surveybutton2.grid(column=8, row=9, padx=7, pady=0)
        self.surveybutton3.grid(column=5, row=10, padx=7, pady=0)
        self.surveybutton4.grid(column=8, row=10, padx=7, pady=0)

        # Label for displaying the correct or incorrect feedback
        self.label = customtkinter.CTkLabel(master=self.imageframe, text="Select the correct answer!")
        self.label.grid(column=7, row=5, columnspan=2)

        # Image display
        self.RefImage = customtkinter.CTkImage(light_image=Image.open('images/broccoli.png'), size=(150,150))
        self.ImageLabel = customtkinter.CTkLabel(master=self.imageframe, text='', image=self.RefImage)
        self.ImageLabel.grid(column=5, row=5)

        self.score = 0  # Initialize score

    def Refresh(self, clicked_button):
        # Check if the button text matches the correct answer
        if clicked_button.text == self.correct_answer:
            self.label.configure(text="Correct!")
            self.score += 1
        else:
            self.label.configure(text="Incorrect! Try again.")

        # Resample new questions
        self.CumulatedNums = sample(FruitsAndVegetables, 4)
        self.correct_answer = self.CumulatedNums[randint(0, 3)]
        self.surveybutton1.configure(text=self.CumulatedNums[0])
        self.surveybutton2.configure(text=self.CumulatedNums[1])
        self.surveybutton3.configure(text=self.CumulatedNums[2])
        self.surveybutton4.configure(text=self.CumulatedNums[3])

    def run(self):
        self.app.mainloop()

# To use the QuizzPage class
quizzpage = QuizzPage()
quizzpage.run()
