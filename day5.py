"""
import time
play = True 
while play :
    try :
        password = input('input password : ')
        if password == 'laugakun' : 
            a = 3
            b = 0
            while a>b : 
                b += 1
                for x in range (0,4) :
                    time.sleep(0.5)
                    c = "Loading" + "." * x
                    print(c)
                    play = False 
        else :
            continue 

    finally :
        def c_intro(dictionary) :
            for key,value in dictionary.items() : 
                print(f'{key} : {value}')
                    
        criminal = {}

        criminal1 = {'nama':'olaf', 'umur':'18' , 'kasus':'mencuri'}
        criminal2 = {'nama':'sven', 'umur':'20' , 'kasus':'membunuh'}
        criminal3 = {'nama':'sum', 'umur':'20' , 'kasus':'mencuri'}
                
        c_intro(criminal1)
        c_intro(criminal2)
        c_intro(criminal3)
"""
#rps 
import random 
x = 0 
y = 0 
while True : 
    a = ['gunting', 'batu', 'kertas'] 
    kunci = random.choice(a)
    menang = ['guntingkertas', 'batugunting', 'kertasbatu']
    kalah = ['kertasgunting', 'guntingbatu','batukertas']
    pilih = input('mau main? gunting/batu/kertas : ')
    print(kunci)
    if pilih == a : 
        print('coba lagi')
        print(f'score {x}, {y}')
    elif pilih + kunci in menang : 
        print('kamu menang!')
        x += 1
        print(f'score {x}, {y}')
    elif pilih + kunci in kalah : 
        y += 1
        print(f'score {x}, {y}')
    else: 
        print('masukkan gunting/batu/kertas')
        

    """
    finally :
        def score(x,y) :
            x = 0 
            y = 0 
            if pilih + a in menang : 
                x += 1
                y += 0
            elif pilih == module : 
                x += 0 
                y += 0
            else :
                x += 0
                y += 0 

        score(x,y)
    """