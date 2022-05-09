import numpy as np
#f(x)=a0*c0<0
#a0=a1
#b1=c0
#f(x)=a0*c0>0
#a1=c0
#b1=b0
#f(x)=an*cn<0
#a0=a1
#b1=c0
#cn+1=an+bn/2

def f(x):
    return (x/3)**2- np.sin(x)-3
a=np.zeros(20)
b=np.zeros(20)
c=np.zeros(20)

for n in range(10):
        if f[a(n)]*f[c(n)]<0:
            a[n+1]=a[n]
            b[n+1]=c[n]
        else:
            a[n+1]=c[n]
            b[n+1]=b[n]
            c[n+1]=(a[n+1]*b[n+1])/2
print (c)