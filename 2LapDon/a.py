import matplotlib.pyplot as plt
import numpy as np
from sympy import *
x = Symbol('x')
#! INPUT
print("""
Bắt đầu chương trình
Đây là phương pháp lặp đơn
INPUT
f(x) với f(x)=0
khoảng phân li nghiệm (a,b)

Và thêm SaiSoE đã cho
INPUT
""")


def Phi(x):
# ** là mũ
    # return 1/(x-1.5)
    return -1/3*x**3


a = -2
b = 2
SaiSoE = 10
print(f"""
INPUT
{Phi(x)} , \tvới f(x)=0
khoảng phân li nghiệm (a,b) = ({a},{b})

Và thêm SaiSoE đã cho: SaiSoE = {SaiSoE}
INPUT
""")
#! INPUT
#! KIỂM TRA ĐIỀU KIỆN PP
print(f"""
#! Điều kiện của phương pháp lặp đơn là:
1. Hàm Phi(x) co <=> 0<q<1 (q=MAX_đạo hàm Phi(x))
""")
dao_ham_Phi= diff(Phi(x),x)
print(dao_ham_Phi)
x_ve_hinh=np.linspace(a,b,1000)
y_ve_hinh=[dao_ham_Phi.subs(x,i) for i in x_ve_hinh]
q=max(y_ve_hinh)
print(f"q = {q}\n Xét 0<q<1 => ",end=" ")
if(0<q and q<1):
    print(f"Đúng")
else:
    print(f"Sai")
plt.plot(x_ve_hinh,y_ve_hinh)
plt.show()

#! KIỂM TRA ĐIỀU KIỆN PP

print("Kết thúc chương trình")
