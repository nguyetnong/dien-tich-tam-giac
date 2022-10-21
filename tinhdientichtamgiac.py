import math


a=float(input("nhap vao do dai canh thu nhat:"))
b=float(input("nhap vao do dai canh thu hai:"))
c=float(input("nhap vao do dai canh thu ba:"))

s = (a+b+c)/2
dien_tich = math.sqrt(s*(s-a)*(s-b)*(s-c))
print("dien tich tam giaac la:",dien_tich)