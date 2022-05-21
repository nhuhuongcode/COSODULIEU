import random
class translate:
    vi = ["May tinh", "Giao vien", "but chi", "sach", "con chuot", "mon toan",
                            "ban be", "mai toc", "trai chanh", "truong hoc", "tinh nguyen vien",
                            "dien thoai thong minh", "lop hoc", "he thong", "xe may", "con song",
                            "truc tuyen", "khach hang", "ngoi sao", "bau troi"]
    en = ["computer", "teacher", "pencil", "book", "mouse", "math",
                            "friend", "hair", "lemon", "school", "volunteer",
                            "smarth phone", "class", "system", "motorbike", "river",
                            "online", "customer", "star", "sky"]
    yn = "Y"
    c = d = 0
    while  yn == "Y":
        i = random.randint(1,len(vi))
        print("Hay dich tu "+vi[i]+" sang tieng Anh nhe")
        da = input("Dap an cua ban la: ")
        da = da.lower()
        if da == en[i] :
            print("Dap an cua ban hoan toan chinh xac!")
            d = d+1
        else:
            print("Dap an cua ban sai roi!")
            print("Dap an chinh xac la: "+ en[i])
        c = c+1
        yn = input("Ban co muon tiep tuc khong?? Y or N ?")
        yn = yn.upper()
    print("Ban tra loi dung {0}/{1} cau".format(d,c))