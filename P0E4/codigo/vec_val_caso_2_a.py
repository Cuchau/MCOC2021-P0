from numpy import double, eye, ones, mean,single
from time import perf_counter
from scipy.linalg import inv, solve, eigh
#Para trabajar el tipo de dato float o double sacar el # para que funcione esa funcion

#tipo de dato float
def matriz_laplaciano(N, t=single):
       e= eye(N)-eye(N,N,1)
       return t(e+e.T)

#tipo de dato double
#def matriz_laplaciano(N, t=double):
       #e= eye(N)-eye(N,N,1)
       #return t(e+e.T)

Ns=[3,4,10,50,100,500,1000,1500]
dts=[]
promt=[]
dtp_3=[]
dtp_4=[]
dtp_10=[]
dtp_50=[]
dtp_100=[]
dtp_500=[]
dtp_1000=[]
dtp_1500=[]





archivo= open("vec_val_caso_2_a_single.txt","w")
#archivo= open("vec_val_caso_2_a_double.txt","w")

for i in range(10):
       for N in Ns:
              A= matriz_laplaciano(N)
              # w valores propios, h vectores propios
              t1=perf_counter()
              w,h= eigh(A,driver="ev",overwrite_a=False)
              t2=perf_counter()
              dt= t2-t1
              if N==3:
                     dtp_3.append(dt)
              elif N==4:
                     dtp_4.append(dt)
              elif N==10:
                     dtp_10.append(dt)
              elif N==50:
                     dtp_50.append(dt)
              elif N==100:
                     dtp_100.append(dt)
              elif N==500:
                     dtp_500.append(dt)
              elif N==1000:
                     dtp_1000.append(dt)
              elif N==1500:
                     dtp_1500.append(dt)


 


                   
dts.append(dtp_3)
dts.append(dtp_4)
dts.append(dtp_10)
dts.append(dtp_50)
dts.append(dtp_100)
dts.append(dtp_500)
dts.append(dtp_1000)
dts.append(dtp_1500)






#Sacar promedio de cada matriz
for i in range(len(Ns)):
       prom=mean(dts[i])
       promt.append(prom)
       print (f"N = {Ns[i]} dt = {prom} s ")
       archivo.write(f"{Ns[i]} {prom} \n")     

archivo.close

