from time import sleep
import matplotlib.pyplot as plt
from numpy.core.fromnumeric import mean

Ns = []
dts1 = []
dts2 = []

archivo= open("matriz_llena_solv.txt", "r")

for line in archivo:
    sep= line.split()
    N=int(sep[0])
    dt1=float(sep[1])
    dt2=float(sep[2])

    Ns.append(N)
    dts1.append(dt1)
    dts2.append(dt2)

archivo.close()

x1=[0,Ns[13]]
y1=[max(dts1),max(dts1)]
x2=[Ns[0],Ns[13]]
y2=[dts1[0],max(dts1)]
x3=[Ns[0],Ns[13]]
y3=[dts1[0]**2,max(dts1)]
x4=[Ns[0],Ns[13]]
y4=[dts1[0]**3,max(dts1)]
x5=[Ns[0],Ns[13]]
y5=[dts1[0]**4,max(dts1)]

plt.figure(1)
#Grafico tiempo de ensamblado
a=plt.subplot(2,1,1)
K=14
for i in range (K):
    plt.loglog(Ns[i*K:(i+1)*K],dts1[i*K:(i+1)*K],marker="o",linestyle="-",color="gray",alpha=0.5)
plt.xticks([10,20,50,100,200,500,1000,2000,5000,10000,20000],[10,20,50,100,200,500,1000,2000,5000,10000,20000])
plt.yticks([0.0001,0.001,0.01,0.1,1,10,60,600],["0.1ms","1ms","10ms","0.1s","1s","10s","1min","10min"])
plt.plot(x1,y1,linestyle="--",color="royalblue", label= "constante")
plt.plot(x2,y2,linestyle="--",color="y",label= "O(N)")
plt.plot(x3,y3,linestyle="--",color="g",label= "O(N^2)")
plt.plot(x4,y4,linestyle="--",color="r",label= "O(N^3)")
plt.plot(x5,y5,linestyle="--",color="m",label= "O(N^4)")
plt.ylim(0.00001,600)

a.axes.xaxis.set_ticklabels([])
a.set_ylabel("Tiempo de ensamblado (s)")
a.set_title("Complejidad computacional matriz llena solve")

x1=[0,Ns[13]]
y1=[max(dts2),max(dts2)]
x2=[Ns[0],Ns[13]]
y2=[dts2[0],max(dts2)]
x3=[Ns[0],Ns[13]]
y3=[dts2[0]**2,max(dts2)]
x4=[Ns[0],Ns[13]]
y4=[dts2[0]**3,max(dts2)]
x5=[Ns[0],Ns[13]]
y5=[dts2[0]**4,max(dts2)]

#Grafico tiempo de solucion
b=plt.subplot(2,1,2)
K=14
for i in range (K):
    plt.loglog(Ns[i*K:(i+1)*K],dts2[i*K:(i+1)*K],marker="o",linestyle="-",color="gray",alpha=0.5)
plt.xticks(rotation=45)
plt.xticks([10,20,50,100,200,500,1000,2000,5000,10000,20000],[10,20,50,100,200,500,1000,2000,5000,10000,20000])
plt.yticks([0.0001,0.001,0.01,0.1,1,10,60,600],["0.1ms","1ms","10ms","0.1s","1s","10s","1min","10min"])
plt.plot(x1,y1,linestyle="--",color="royalblue",label= "constante")
plt.plot(x2,y2,linestyle="--",color="y",label= "O(N)")
plt.plot(x3,y3,linestyle="--",color="g",label= "O(N^2)")
plt.plot(x4,y4,linestyle="--",color="r",label= "O(N^3)")
plt.plot(x5,y5,linestyle="--",color="m",label= "O(N^4)")
plt.ylim(0.00001,600)
b.set_ylabel("Tiempo de solucion (s)")
b.set_xlabel("Tamaño de matriz N")
b.legend(loc="upper left")
plt.tight_layout()
plt.savefig("matriz_llena_solve")
plt.show()