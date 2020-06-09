flowerr = []
class Bunga : 
    def __init__ (self, namab, kelopakb, hargab) : 
        self.nama = namab
        self.kelopak = kelopakb
        self.harga = hargab
    def flower (self) : 
        return f'bunga {self.nama}, jumlah kelopak {self.kelopak}, harganya {self.harga}'
play = True 
while play : 
    pilih = input('masukkan (y/n) : ')
    if pilih == 'y' : 
        namab = input('nama bunga :')
        kelopakb = int(input('jumlah kelopak : '))
        hargab = float(input('harga bunga : '))
        bungaa = Bunga(namab, kelopakb, hargab)
        flowerr.append(bungaa.flower())
    elif pilih == 'n' : 
        for x in flowerr :
            print(x)
        break 
    else : 
        play = False 