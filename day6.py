class Persegi : 
    def __init__ (self) : 
        self.panjang = input('masukkan panjang = ')
        self.lebar = input('masukkan lebar = ')
    
    def area(self) : 
        return int(self.panjang)*int(self.lebar)

persegip = Persegi()
print(persegip.area())
