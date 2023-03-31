from sympy import *
x = Symbol('x')
import numpy as np
import matplotlib.pyplot as plt
#! INPUT
print("""
Bắt đầu chương trình
Đây là phương pháp chia đôi (đã cho số lần lặp N)
INPUT
f(x) với f(x)=0
khoảng phân li nghiệm (a,b)

Và thêm SoLanLapN đã cho
INPUT
""")


def f(x):
    # return 1/(x-1.5)
    return x**3-x-1
# ** là mũ
a = 1
b = 2
SoLanLapN = 10
print(f"""
INPUT
{f(x)} , \tvới f(x)=0
khoảng phân li nghiệm (a,b) = ({a},{b})

Và thêm SoLanLapN đã cho: SoLanLapN = {SoLanLapN}
INPUT
""")
#! INPUT
#! KIỂM TRA ĐIỀU KIỆN PP
print(f"""
#! Điều kiện của phương pháp chia đôi là:
1. f(x) liên tục trên khoảng phân li nghiệm (a,b)
""")
x_ve_hinh=np.linspace(a,b,1000)
y_ve_hinh=[f(i) for i in x_ve_hinh]
# print(x_ve_hinh)
# print(y_ve_hinh)
plt.plot(x_ve_hinh,y_ve_hinh)

def ox(x):
    return 0

y_ve_hinh=[0 for i in x_ve_hinh]
# print(x_ve_hinh)
# print(y_ve_hinh)
plt.plot(x_ve_hinh,y_ve_hinh)
plt.show()
#! KIỂM TRA ĐIỀU KIỆN PP
#! Tính f(a), f(b) để biết dấu
f_a=f(a)
f_b=f(b)
if(f_a<0):
    sign_a=-1
else:
    sign_a=1
if(f_b<0):
    sign_b=-1
else:
    sign_b=1


print(f"""
Tính f(a), f(b) để biết dấu
f(a) = {f_a} và dấu {sign_a}
f(b) = {f_b} và dấu {sign_b}
""")
if(sign_a*sign_b>0):
    print("Nếu sign_a và sign_b cùng dấu thì lỗi không giải được")
    print("Kết thúc chương trình")
    exit()
#! Tính f(a), f(b) để biết dấu
#! Bắt đầu thuật toán chính
# vì đã cho N 
print(f'Bảng:')
print(f'.{"":_^20}.{"":_^20}.{"":_^20}.{"":_^20}.{"":_^20}.')
print(f'|{" ": ^20}|{sign_a: ^20}|{sign_b: ^20}|{" ": ^20}|{" ": ^20}|')
print(f'|{"":_^20}|{"":_^20}|{"":_^20}|{"":_^20}|{"":_^20}|')
print(f'|{"N": ^20}|{"a": ^20}|{"b": ^20}|{"c": ^20}|{"sign_c": ^20}|')
print(f'|{"":_^20}|{"":_^20}|{"":_^20}|{"":_^20}|{"":_^20}|')
for i in range (SoLanLapN+1):
    c=(a+b)/2
    f_c=f(c)
    if(f_c<0):
        sign_c="-"
    else:
        sign_c="+"
    print(f'|{i: ^20}|{a: ^20}|{b: ^20}|{c: ^20}|{sign_c: ^20}|')
    if(f(c)==0):
        print(f"=> Nghiệm tìm được do trường hợp đặc biệt xn = {c}, e = 0")
        break
    if(f(c)*sign_a>0):
        a=c
    else:
        b=c

print(f'|{"":_^20}|{"":_^20}|{"":_^20}|{"":_^20}|{"":_^20}|')
print(f"=> Nghiệm tìm được x{i} = {c}, e = {(b-a)/2**SoLanLapN}")
#! Bắt đầu thuật toán chính

print("Kết thúc chương trình")