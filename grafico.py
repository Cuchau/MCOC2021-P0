from time import sleep
import matplotlib.pyplot as plt

Ns = []
dts = []
memt = []

archivo= open("rendimiento.txt", "r")


for line in archivo:
    sep= line.split()
    N=int(sep[0])
    dt=float(sep[1])
    mem=int(sep[2])
        
    Ns.append(N)
    dts.append(dt)
    memt.append(mem)


archivo.close()

plt.figure(1)
a=plt.subplot(2,1,1)
K=10
for i in range (K):
    plt.loglog(Ns[i*K:(i+1)*K],dts[i*K:(i+1)*K],marker="o",linestyle="-")

plt.grid()
plt.xticks([10,20,50,100,200,500,1000,2000,5000,10000,20000],[10,20,50,100,200,500,1000,2000,5000,10000,20000])
plt.yticks([0.0001,0.001,0.01,0.1,1,10,60,600],["0.1ms","1ms","10ms","0.1s","1s","10s","1min","10min"])
a.axes.xaxis.set_ticklabels([])
a.set_ylabel("Tiempo transcurrido (s)")
a.set_title("Rendimiento A@B")


b=plt.subplot(2,1,2)
plt.loglog(Ns,memt,marker="o")
plt.plot(0,16)
plt.grid()
plt.xticks(rotation=45)
plt.xticks([10,20,50,100,200,500,1000,2000,5000,10000,20000],[10,20,50,100,200,500,1000,2000,5000,10000,20000])
plt.yticks([1000,10000,100000,(1e6),(1e7),(1e8),(1e9),(1e10)],["1KB","10KB","100KB","1MB","10MB","100MB","1GB","10GB"])
plt.axhline(y=1.6e10, color="k", linestyle="--")
b.set_ylabel("Uso de memoria (s)")
b.set_xlabel("Tamaño de matriz N")

plt.savefig(".jpg")
plt.tight_layout()
plt.show()