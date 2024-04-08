import random


arr = ['apple', 'pear', 'orange', 'broccoli']



for question in range(20): #loops through 20 questions
    rand = random.randint(0,3) #random number to be used in the array
    rand_fv = arr[rand]
    print("What fruit is ", rand_fv)
    answer = input("")
    if answer == rand_fv:
        question = question +1
    else:
        break