
password = 'mohamed'

chances=5
while chances >=0:
    answer =  input('plz enter your password') 
    if answer == password:
        print ('your password is correct')
        break
        
    else :
        print ('your answer was not correct')
        chances -= 1
