from numpy import double, eye,mean
from time import perf_counter
import scipy.sparse as sparse
import matplotlib as plt

#tipo de dato double
def matriz_laplaciana(N, t=double):
    e= sparse.eye(N,dtype=double)-sparse.eye(N,N,1,dtype=double)
    return (e+e.T)
    
Ns = [10,100,1000,1500,2000,2500,3000,3500,4000,4500,5000,5500,6000,6500,7000,7500,8000,8500,9000,9500,10000,15000,20000]
dts1 = []
dts2 = []

archivo= open("Matmul_dispersa.txt","w")

for i in range (10):
    for N in Ns:
        t1= perf_counter()
        A= matriz_laplaciana(N)
        B= matriz_laplaciana(N)
        t2 = perf_counter()
        C =A@B
        t3 = perf_counter()

        dt1= t2-t1
        dt2= t3-t2
        dts1.append(dt1)
        dts2.append(dt2)
        print(f"N = {N} dt1 = {dt1} s dt2 = {dt2} s")
        archivo.write(f"{N} {dt1} {dt2} \n")

archivo.close()

