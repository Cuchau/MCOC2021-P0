from numpy import half, single, double, longdouble, eye
from time import perf_counter
from scipy.linalg import inv 


def matriz_laplaciano(N, t=half):
       e= eye(N)-eye(N,N,1)
       return t(e+e.T)

Ns=[3,4,10,100,1000,2000,3000,4000,5000,6000,7000,8000]
memt=[]
dts=[]

archivo= open("longdouble_caso_3.txt","w")

for i in range(10):
       for N in Ns:
              uso_memoria_total = 0
              A= matriz_laplaciano(N)

              t1=perf_counter()
              A_inv= inv(A,overwrite_a=True)
              t2=perf_counter()
              dt= t2-t1
              dts.append(dt)

              uso_memoria_total= A_inv.nbytes
              memt.append(uso_memoria_total)
              print (f"N = {N} dt = {dt} s mem = {uso_memoria_total} bytes")
              archivo.write(f"{N} {dt} {uso_memoria_total}\n")

archivo.close
