from numpy import double, eye, ones, mean, single
from time import perf_counter
from scipy.linalg import inv, solve
#Para trabajar el tipo de dato float o double sacar el # para que funcione esa funcion

#tipo de dato float
def matriz_laplaciano(N, t=single):
       e= eye(N)-eye(N,N,1)
       return t(e+e.T)

#tipo de dato double
#def matriz_laplaciano(N, t=double):
       #e= eye(N)-eye(N,N,1)
       #return t(e+e.T)

Ns=[3,4,10,100,1000,1500,2000,2500,3000,4000,5000,6000]
dts=[]
promt=[]
dtp_3=[]
dtp_4=[]
dtp_10=[]
dtp_100=[]
dtp_1000=[]
dtp_1500=[]
dtp_2000=[]
dtp_2500=[]
dtp_3000=[]
dtp_4000=[]
dtp_5000=[]
dtp_6000=[]



archivo= open("sist_ec_caso_1_single.txt","w")
#archivo= open("sist_ec_caso_1_double.txt","w")

for i in range(10):
       for N in Ns:
              A= matriz_laplaciano(N)
              B= ones(N)

              t1=perf_counter()
              x = inv(A)*B
              t2=perf_counter()
              dt= t2-t1
              if N==3:
                     dtp_3.append(dt)
              elif N==4:
                     dtp_4.append(dt)
              elif N==10:
                     dtp_10.append(dt)
              elif N==100:
                     dtp_100.append(dt)
              elif N==1000:
                     dtp_1000.append(dt)
              elif N==1500:
                     dtp_1500.append(dt)
              elif N==2000:
                     dtp_2000.append(dt)
              elif N==2500:
                     dtp_2500.append(dt)
              elif N==3000:
                     dtp_3000.append(dt)
              elif N==4000:
                     dtp_4000.append(dt)
              elif N==5000:
                     dtp_5000.append(dt)
              elif N==6000:
                     dtp_6000.append(dt)

                   

dts.append(dtp_3)
dts.append(dtp_4)
dts.append(dtp_10)
dts.append(dtp_100)
dts.append(dtp_1000)
dts.append(dtp_1500)
dts.append(dtp_2000)
dts.append(dtp_2500)
dts.append(dtp_3000)
dts.append(dtp_4000)
dts.append(dtp_5000)
dts.append(dtp_6000)


#Sacar promedio de cada matriz
for i in range(len(Ns)):
       prom=mean(dts[i])
       promt.append(prom)
       print (f"N = {Ns[i]} dt = {prom} s ")
       archivo.write(f"{Ns[i]} {prom} \n")     

archivo.close

