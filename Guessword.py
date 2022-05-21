import random
class guessword:
    yn = "Y"
    c = e = 0
    clear = '\n'* 100
    while yn == "Y":
        print("Nguoi ra de:")
        a = input("Nhap tu tieng anh co nghia: ")
        a = a.upper()
        print(clear)
        print("Nguoi choi:")
        i = random.randint(0,len(a)-1)
        Lu = [0]*len(a)
        d = 0
        Lu[d] = i
        while d < len(a) :
            i = random.randint(0,len(a)-1)
            n = 0
            while n < len(Lu):
                if i != Lu[n]:
                    n = n+1
                else:
                    n = 0
                    i = random.randint(0,len(a)-1)
                if n == len(a) - 1:
                    break
            Lu[d] = i
            print(a[i],end = '')
            d = d+1
        z = input("\nDap an cua ban la: ")
        z = z.upper()
        if z != a:
            print("Dap an cua ban khong chinh xac!")
            print("Dap an chinh xac la: "+a)
        else:
            print("Dap an cua ban hoan toan chinh xac!")
            e = e+1
        c = c+1
        yn = input("Ban co muon tiep tuc khong ? Y or N ??")
        yn = yn.upper()
    print("Ban da tra loi dung {0}/{1} cau hoi".format(e,c))



