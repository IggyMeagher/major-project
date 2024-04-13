def update_quiz(self):
    old_numbers = self.CumulatedNums[:]
    self.RandomNum1 = randint(0, len(FruitsAndVegetables)-1)
    self.RandomNum2 = randint(0, len(FruitsAndVegetables)-1)
    self.RandomNum3 = randint(0, len(FruitsAndVegetables)-1)
    self.RandomNum4 = randint(0, len(FruitsAndVegetables)-1)
    self.CumulatedNums = [self.RandomNum1, self.RandomNum2, self.RandomNum3, self.RandomNum4]

    # Update the button texts with new values
    self.surveybutton1.configure(text=FruitsAndVegetables[self.CumulatedNums[0]])
    self.surveybutton2.configure(text=FruitsAndVegetables[self.CumulatedNums[1]])
    self.surveybutton3.configure(text=FruitsAndVegetables[self.CumulatedNums[2]])
    self.surveybutton4.configure(text=FruitsAndVegetables[self.CumulatedNums[3]])

    # Check if numbers have changed
    if old_numbers != self.CumulatedNums:
        print("Numbers have changed.")
    else:
        print("Numbers have not changed.")
