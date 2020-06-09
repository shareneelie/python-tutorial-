def siswa_intro(dictionary) :
    for key,value in dictionary.items() : 
        print(f'{key} : {value}')

siswa = { }

play = True 
while play : 
    nama = input('masukkan nama : ')
    umur = input('masukkan umur : ')
    pekerjaan = input('masukkan pekerjaan : ') 
    siswa = {'nama':nama , 'umur':umur , 'pekerjaan': pekerjaan}
    another = input('tambahkan siswa? (y/n) : ')
    if another == 'n' : 
        play = False 

siswa_intro(siswa)