from numpy import double,eye
from time import perf_counter
from scipy.linalg import inv 

def matriz_laplaciana(N, t=double):
       e= eye(N)-eye(N,N,1)
       return t(e+e.T)

Ns=[10,100,1000,1500,2000,2500,3000,3500,4000,4500,5000,5500]
dts1=[]
dts2=[]

archivo= open("matriz_llena_inv.txt","w")

for i in range(10):
       for N in Ns:
              t1=perf_counter()
              A= matriz_laplaciana(N)
              t2=perf_counter()
              A_inv= inv(A,overwrite_a=False)
              t3=perf_counter()
              
              dt1= t2-t1
              dt2= t3-t2
              dts1.append(dt1)
              dts2.append(dt2)
              print(f"N = {N} dt1 = {dt1} s dt2 = {dt2} s")
              archivo.write(f"{N} {dt1} {dt2} \n")

archivo.close()