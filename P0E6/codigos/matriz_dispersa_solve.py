from numpy.typing import NBitBase
import scipy.sparse as sp
import scipy.sparse.linalg as lin
from scipy.sparse import lil_matrix
from numpy import double, dtype,ones,eye
from time import perf_counter

def matriz_laplaciana(N, t=double):
    e= sp.eye(N,dtype=double)-sp.eye(N,N,1,dtype=double)
    return (e+e.T)

Ns = [10,100,1000,1500,2000,2500,3000,3500,4000,4500,5000,5500,6000,6500,7000,7500,8000,8500,9000,9500,10000,10500,11000,11500,12000,12500,13000,13500,14000,14500,15000,15500,16000,16500,17000,17500,18000,18500,19000,19500,20000]
dts1 = []
dts2 = []

archivo= open("matriz_dispersa_solv.txt","w")

for i in range (10):
    for N in Ns:
        t1= perf_counter()
        A= matriz_laplaciana(N)
        B= ones(N,dtype=double)
        Acsr=sp.csr_matrix(A)
        t2 = perf_counter()
        x=lin.spsolve(Acsr,B)
        t3 = perf_counter()

        dt1= t2-t1
        dt2= t3-t2
        dts1.append(dt1)
        dts2.append(dt2)
        print(f"N = {N} dt1 = {dt1} s dt2 = {dt2} s")
        archivo.write(f"{N} {dt1} {dt2} \n")

archivo.close()

