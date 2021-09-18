import numpy as np, tabulate
from numpy.lib.function_base import append
Data=[];data=[];heading=[]
n=int(input("Number of data points: "))
x=np.zeros(n)
y=np.zeros((n,n))

print("Enter x values")
for i in range(n):
    x[i]=eval(input('x['+str(i)+']= '))

heading.append('x')
heading.append('y')

print("Enter y values")
for i in range(n):
    y[i][0]=eval(input('y['+str(i)+']= '))
    heading.append('Δ'+str(i+1)+'y')

for i in range(1,n):
    for j in range(0,n-i):
        y[j][i]=y[j+1][i-1]-y[j][i-1]



print("Table:")
""" 
for i in range(0,n):
    print('%0.4f' %(x[i]), end='')
    for j in range(0, n-i):
        print('   %0.4f' %(y[i][j]), end='')
    print()
"""

for i in range(0,n):
    data.append(x[i])
    for j in range(0, n-i):
        data.append(y[i][j])
    c=data.copy()
    data.clear()
    Data.append(c)
print(tabulate.tabulate(Data,heading,tablefmt='fancy_grid'))

