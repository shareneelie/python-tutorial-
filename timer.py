"""
import time 
"""
"""
while True :

    try :
    pilih = input('pakai timer? (ya/tidak) : ')
        if pilih == 'ya' :
            detik = int(input('masukkan detik : '))
            menit = int(input('masukkan menit : '))
            jam = int(input('masukkan jam : '))
            waktu = detik + menit*60 + jam*3600 
            for x in range(waktu+1):
                    time.sleep(1)
                    print(waktu-x)
            print ('waktu habis')
        elif pilih == 'tidak' : 
            print('ok')  
    except ValueError : 
        print('harus masukkan angka')
"""

a = 3
b = 0
while a>b : 
    b += 1
    for x in range (0,4) :
        c = "Loading" + "." * x
        print(c)
        