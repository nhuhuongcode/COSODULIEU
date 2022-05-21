import math
class equation:
    clear = "\n" * 100
    print('Nguoi ra de')
    print('Moi ban ra de bai bang cach nhap vao man hinh gia tri a,b,c')
    a = float(input('Nhap vao gia tri a: '))
    b = float(input('Nhap vao gia tri b: '))
    c = float(input('Nhap vao gia tri c: '))
    print (clear)
    print('Nguoi giai')
    print('Hay giai he pt bac hai {0}x^2 + {1}x + {2} = 0'.format(a,b,c))
    print('1. Neu pt vo nghiem, go dap an: x = vn')
    print("2. Neu pt co nghiem la tat ca so thuc R, go dap an: x = r")
    print('3. Neu pt co nghiem duy nhat la x, go dap an: x = (dap an)')
    print("4. Neu pt co hai nghiem, go dap an: x1 = (dap an), x2 = (dap an)")
    yn = "Y"
    while yn == "Y":
        if a == 0 and b == 0 and c != 0 :
            x1 = "vn"
            x = input("x = ")
            if x == x1:
                print("Ban da tra loi dung")
                break
            else:
                print("Ban tra loi sai roi!")
                yn =input("Ban co muon tiep tuc khong? Y or N ?")
                yn = yn.upper()
        elif a == 0 and b == 0 and c ==  0:
            x1 = "r"
            x = input("x = ")
            if x == x1:
                print("Ban da tra loi dung")
                break
            else:
                print("Ban tra loi sai roi!")
                yn = input("Ban co muon tiep tuc khong? Y or N ?")
                yn = yn.upper()
        elif a == 0 and b != 0:
            x2 = float(-c/b)
            x3 = float(input("x= "))
            if x2 == x3:
                print("Ban da tra loi dung")
                break
            else:
                print("Ban tra loi sai roi!")
                yn = input("Ban co muon tiep tuc khong? Y or N ?")
                yn = yn.upper()
        else:
            delta = float(b*b -4*a*c)
            if delta < 0:
                x1 = "vn"
                x = input("x = ")
                if x == x1:
                    print("Ban da tra loi dung")
                    break
                else:
                    print("Ban tra loi sai roi!")
                    yn = input("Ban co muon tiep tuc khong? Y or N ?")
                    yn = yn.upper()
            elif delta == 0:
                x2 = float((-b / (2 * a)))
                x3 = float(input("x= "))
                if  x2 == x3:
                    print("Ban da tra loi dung")
                    break
                else:
                    print("Ban tra loi sai roi!")
                    yn = input("Ban co muon tiep tuc khong? Y or N ?")
                    yn = yn.upper()
            else:
                x2 = float((-b - math.sqrt(delta))/2*a)
                x4 = float((-b + math.sqrt(delta)) / 2 * a)
                x3 = float(input("x1 = "))
                x5 = float(input("x2 = "))
                if x2 == x3 and x4 == x5:
                    print("Ban da tra loi dung")
                    break
                else:
                    print("Ban tra loi sai roi!")
                    yn = input("Ban co muon tiep tuc khong? Y or N ?")
                    yn = yn.upper()






