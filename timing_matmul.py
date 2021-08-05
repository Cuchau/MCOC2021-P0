from numpy import zeros
from time import perf_counter
import matplotlib as plt

N = 3
Ns = [10,100,1000,2000,3000,4000,5000,6000,7000,8000]
dts = []
memt = []
archivo= open("rendimiento.txt","w")

for i in range (10):
    for N in Ns:
        uso_memoria_total = 0
        A = zeros((N,N))+1
        B = zeros((N,N))+2
        
        t1 = perf_counter()
        C =A@B
        t2 = perf_counter()

        uso_memoria_total= A.nbytes + B.nbytes + C.nbytes
        dt= t2-t1
        dts.append(dt)
        memt.append(uso_memoria_total)
        print(f"N = {N} dt = {dt} s mem = {uso_memoria_total} bytes")
        archivo.write(f"{N} {dt} {uso_memoria_total}\n")
    
archivo.close()

