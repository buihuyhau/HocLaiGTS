from sympy import *
x = Symbol('x')
import numpy as np
import matplotlib.pyplot as plt
#! INPUT
print("""
Bắt đầu chương trình
Đây là phương pháp chia đôi (đã cho sai số E)
INPUT
f(x) với f(x)=0
khoảng phân li nghiệm (a,b)

Và thêm SaiSoE đã cho
INPUT
""")


def f(x):
    # return 1/(x-1.5)
    return x**3-x-1
# ** là mũ
a = 1
b = 2
SaiSoE = 10
print(f"""
INPUT
{f(x)} , \tvới f(x)=0
khoảng phân li nghiệm (a,b) = ({a},{b})

Và thêm SaiSoE đã cho: SaiSoE = {SaiSoE}
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
print("Kết thúc chương trình")