from time import sleep
import matplotlib.pyplot as plt

Ns_1 = []
Ns_2 = []
Ns_3 = []
Ns_4 = []
Ns_5 = []
Ns_6 = []
Ns_7 = []
Ns_8 = []
Ns_9 = []
dts_1 = []
dts_2 = []
dts_3 = []
dts_4 = []
dts_5 = []
dts_6 = []
dts_7 = []
dts_8 = []
dts_9 = []

#Para abrir cada archivo se cambia el nombre en open
archivo1= open("vec_val_caso_3_a_double.txt", "r")
archivo2= open("vec_val_caso_3_b_double.txt", "r")
archivo3= open("vec_val_caso_3_a_single.txt", "r")
archivo4= open("vec_val_caso_3_a_single.txt", "r")



for line in archivo1:
    sep=line.split()
    N=int(sep[0])
    dt=float(sep[1])
    Ns_1.append(N)
    dts_1.append(dt)

for line in archivo2:
    sep=line.split()
    N=int(sep[0])
    dt=float(sep[1])
    Ns_2.append(N)
    dts_2.append(dt)

for line in archivo3:
    sep=line.split()
    N=int(sep[0])
    dt=float(sep[1])
    Ns_3.append(N)
    dts_3.append(dt)

for line in archivo4:
    sep=line.split()
    N=int(sep[0])
    dt=float(sep[1])
    Ns_4.append(N)
    dts_4.append(dt)


archivo1.close()
archivo2.close()
archivo3.close()
archivo4.close()


plt.plot(Ns_1,dts_1,label="caso 3-a,double",marker="o")
plt.plot(Ns_2,dts_2,label="caso 3-b,double",marker="o")
plt.plot(Ns_3,dts_3,label="caso 3-a,single",marker="o")
plt.plot(Ns_4,dts_4,label="caso 3-b,single",marker="o")

plt.loglog()
plt.xticks([10,20,50,100,200,500,1000,2000,5000,6500],[10,20,50,100,200,500,1000,2000,5000,6500])
plt.yticks([0.0001,0.001,0.01,0.1,1,10,60,600],["0.1ms","1ms","10ms","0.1s","1s","10s","1min","10min"])
plt.xlabel("Tamaño matriz N")
plt.ylabel("Tiempo[s]")
plt.title("comparacion eigh double vs single")
plt.legend()
plt.show()