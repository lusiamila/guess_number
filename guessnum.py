def inputyesno():

    choice = input('yes/no: ')
    while choice not in ['yes','no']:
        choice = input('Please input yes/no: ')
    return choice


def recursive(low,high):
    if low <= high:
        midl = (low + high)//2
        
        print(f'I think it is number {midl} Did I guess?')
        a = inputyesno()
        
        if a == 'yes':
            print('I guess! I guess! :D ')
            return midl
                    
        else:
            print('Is my number higher?')
            b = inputyesno()
                    
            if b == 'yes':
                high = midl - 1
                return recursive(low,high)
                    
            else:
                low = midl + 1
                return recursive(low,high)
    else:
        print('I think you forgot your number\nDo you want to play again?')
        gameagain = inputyesno()

        if gameagain == 'yes':
            print('ok')
            choose_game()
        
        if gameagain == 'no':
            print('ok,bye! see you at the bay')

def choose_game():
    
    low = 0
    high = 10
    
    print(f'I will try to guess your number\nChoose a number between 0 and {high}\nAre you ready?')
    
    
    choice = inputyesno()

    if choice == 'yes':
        print('ok')
        
        recursive(low,high)

        
    if choice == 'no':
        print('ok,bye')
        

                    
choose_game()