from numpy import double, eye, ones
from time import perf_counter
from scipy.linalg import inv, solve
#Para trabajar el tipo de dato float o double sacar el # para que funcione esa funcion

#tipo de dato float
def matriz_laplaciano(N, t=double):
       e= eye(N)-eye(N,N,1)
       return t(e+e.T)

Ns=[10,100,1000,1500,2000,2500,3000,3500,4000,4500,5000,5500,6000,6500]
dts1=[]
dts2=[]

archivo= open("matriz_llena_solv.txt","w")

for i in range(10):
       for N in Ns:
              t1=perf_counter()
              A= matriz_laplaciano(N)
              B= ones(N)
              t2=perf_counter()
              x=solve(A,B,assume_a='pos')
              t3=perf_counter()

              dt1= t2-t1
              dt2= t3-t2
              dts1.append(dt1)
              dts2.append(dt2)
              print(f"N = {N} dt1 = {dt1} s dt2 = {dt2} s")
              archivo.write(f"{N} {dt1} {dt2} \n")

archivo.close()

