print ("welcome to our fken game ")
print ( " this is the number gessing game")
print (" u won't gess it because u are noob and have a bad little nightmares ")
print ("u have only 4 chances to complete this fken mission")
print ('plz write it fast becase i got bored from you ')

import random
random_number = random.randint(0,100)

chances=5
while chances >=0:
    answer = int( input('plz enter your guess') )
    if answer > random_number:
        print ('your answer was higher than expected')
        chances -= 1
    elif answer < random_number :
        print ('your answer was lower than expected')
        chances -= 1
    else :
        print('correct')
        break
    
