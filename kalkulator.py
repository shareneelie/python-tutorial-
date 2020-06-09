#kalk
num1 = input('masukkan angka pertama : ')
num2 = input('masukkan angka kedua : ')
print('angka 1 untuk tambah')
print('angka 2 untuk kurang')
print('angka 3 untuk kali')
print('angka 4 untuk bagi')
angkapilihan = input('masukkan angka pilihan : ')
if angkapilihan == '1' : 
    #code for plus
    operation1 = float(num1)+float(num2)
    print('hasilnya adalah : ', operation1)
elif angkapilihan == '2' : 
    #code for min
    operation2 = float(num1)-float(num2)
    print('hasilnya adalah : ', operation2)
elif angkapilihan == '3' : 
    #code for multip
    operation3 = float(num1)*float(num2)
    print('hasilnya adalah : ', operation3)
elif angkapilihan == '4' : 
    #code for div
    operation4 = float(num1)/float(num2)
    print('hasilnya adalah : ', operation4)
else :
    print('error')