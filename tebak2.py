"""
import random 
play = True 
while play :
    kunci = random.randint(1, 11) 
    """ """
    print(kunci)
    """
    guess = int(input('please enter your guess (1-10) : '))

    if guess == kunci: 
        print('selamat!')
        coba = input('mau main lagi? (y/n) :')
        if coba == 'y' :
            continue 
        else : 
            break 
    elif guess<kunci : 
        print('tambahin lagi!')
    elif guess>kunci: 
        print('kurangin!')


