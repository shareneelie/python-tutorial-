"""
#segitiga
def area (alas, tinggi) :
    luas = int(alas)*int(tinggi)/2 
    print(f'luas segitiga adalah {luas}')
def pitagoras(alas, tinggi) : 
    hasil = (alas**2 + tinggi**2)**0.5
    print(f'sisi miring segitiga adalah {hasil}')
a = int(input('masukkan alas segitiga : '))
t = int(input('masukkan tinggi segitiga : '))
area(a, t)
pitagoras(a, t)
"""
#jam kerja 
def total (jam, gaji) : 
    if jam>=40 : 
        akhir = int(gaji) + 150 
    elif jam<40 : 
        akhir = g 
    print(f'uang yang didapat adalah {akhir}')
j = int(input('masukkan jam kerja : '))
g = int(input('masukkan gaji : '))
total(j,g)