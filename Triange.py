import random
class Tamgiac:
    #class Tamgiac:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    def InRaMH(self):
        print('Cho tam giac co: ');
        print('Canh a la: {0}, Canh b la: {1}, Canh c la: {2}'.format(self.a,self.b,self.c))
        print(" Hoi: Day la tam giac: thuong, can, deu, vuong")
    def LoaiTamGiac(self):
        global tamgiac
        if self.a == self.b and self.b == self.c:
            tamgiac = "deu"
        elif (pow(self.a,2) == pow(self.b,2) + pow(self.c,2)) or (pow(self.a,2) + pow(self.b,2) == pow(self.c,2)) or (pow(self.b,2) == pow(self.a,2) + pow(self.c,2)):
            tamgiac = "vuong"
        elif self.a == self.b or self.b == self.c or self.a == self.c:
            tamgiac = "can"
        else:
            tamgiac = "thuong"
        return tamgiac
    def sosanh(self):
        ketqua = input("Tra loi: Day la tam giac ")
        ketqua = ketqua.lower()
        if ketqua == tamgiac:
            print("Ban da tra loi dung")
        else:
            print("Ban da tra loi sai")
            thulai=input("Ban co muon thu lai? (Y/N)")
            thulai = thulai.upper()
            if thulai == "Y":
                ketqua = input("Tra loi: Day la tam giac ")
                ketqua = ketqua.lower()
            else:
                print("Dap an: Day la tam giac " + tamgiac)
                print("Tro choi ket thuc")
                return
    # class program:
    #     a = random.randint(1,10)
    #     b = random.randint(1,10)
    #     c = random.randint(1,10)
    #
    #     while a + b <= c and b + c <= a and a + c <= b:
    #         a = random.randint(1, 10)
    #         b = random.randint(1, 10)
    #         c = random.randint(1, 10)
    #     doan = Tamgiac(a, b, c)
    #     doan.InRaMH()
    #     doan.LoaiTamGiac()
    #     doan.sosanh()

