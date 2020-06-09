print('game tebak angka')
play = True 
while play : 
        tebakan = input('masukkan angka tebakkan (1-10)  : ')
        if tebakan > '5' : 
            print('kurangin')
        elif tebakan < '5' : 
            print('tambahin')
        elif tebakan == '5' :
            print('yey benar!')
            again = input('mau main lagi? (y/n) : ')
            if again == 'n' :
                play = False

    