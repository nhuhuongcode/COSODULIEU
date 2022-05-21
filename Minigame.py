import sys
import random
import math
sys.path.append(".")
class main:
    print('XIN CHAO CAC BAN DEN VOI MINIGAME')
    yn = 'Y'
    while yn == 'Y':
        print("\nDe bat dau tro choi moi cac ban nhap lua chon: ")
        print("   1. Nhap 'TOAN' de bat dau tro choi toan ")
        print("   2. Nhap 'TA' de bat dau tro choi tieng Anh ")
        bien = input("\nMoi cac ban nhap lua chon: ")
        bien = bien.upper()
        while bien != 'TOAN' and bien != 'TA':
            bien = input("Moi ban nhap dung lua chon 'TOAN' hoac 'TA'!!!")
            bien = bien.upper()
        if bien == 'TOAN':
            print('Ban muon tro choi nay?')
            print('1.Tro choi tam giac')
            print('2.Tro choi he phuong trinh')
            luachon = int(input('Moi ban nhap lua chon: '))
            while luachon != 1 and luachon != 2:
                luachon = int(input('Xin moi ban nhap dung lua chon 1 hoac 2!!!'))
            if luachon == 2:
                from Equations import equation
                equation()
            elif luachon == 1:
                from Triange import Tamgiac
                a = random.randint(1, 10)
                b = random.randint(1, 10)
                c = random.randint(1, 10)
                while a + b <= c or b + c <= a or a + c <= b:
                    a = random.randint(1, 10)
                    b = random.randint(1, 10)
                    c = random.randint(1, 10)
                doan = Tamgiac(a, b, c)
                doan.InRaMH()
                doan.LoaiTamGiac()
                doan.sosanh()
        elif bien == 'TA':
            print('Ban muon tro choi nay?')
            print('1.Tro choi dich tu')
            print('2.Tro choi xep tu')
            luachon = int(input('Moi ban nhap lua chon: '))
            while luachon != 1 and luachon != 2:
                luachon = int(input('Xin moi ban nhap dung lua chon 1 hoac 2!!!'))
            if luachon == 2:
                from Guessword import guessword
                guessword()
            elif luachon == 1:
                from Translate import translate
                translate()
        yn = input("Ban co muon choi tro khac khong? Y or N ??")
        yn = yn.upper()
        clear ='\n' * 100
        print(clear)
    print('Cam on ban da tham gia tro choi')
main()
