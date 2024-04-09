import random

score = 0

arr = ['apple', 'pear', 'orange', 'broccoli']



for question in range(20): #loops through 20 questions
    rand = random.randint(0,3) #random number to be used in the array
    rand_fv = arr[rand] #random fruit to be asked
    print("What fruit is ", rand_fv)
    answer = input("")
    if answer == rand_fv: #checking if answer is correct
        question = question +1 #going on to the next question, if answer is correct
        score = score +1 #adding 1 to the score, because answer is right
    else:
        print('you got it wrong, your score is', score) #if the answer is wrong, it tells
        question = question + 1 #going onto the next question nonetheless