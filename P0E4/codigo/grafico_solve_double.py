from time import sleep
import matplotlib.pyplot as plt

Ns_1 = []
Ns_2 = []
Ns_3 = []
Ns_4 = []
Ns_5 = []
Ns_6 = []
Ns_7 = []
dts_1 = []
dts_2 = []
dts_3 = []
dts_4 = []
dts_5 = []
dts_6 = []
dts_7 = []

#Para abrir cada archivo se cambia el nombre en open
archivo1= open("sist_ec_caso_1_double.txt", "r")
archivo2= open("sist_ec_caso_2_double.txt", "r")
archivo3= open("sist_ec_caso_3_double.txt", "r")
archivo4= open("sist_ec_caso_4_double.txt", "r")
archivo5= open("sist_ec_caso_5_double.txt", "r")
archivo6= open("sist_ec_caso_6_double.txt", "r")
archivo7= open("sist_ec_caso_7_double.txt", "r")


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

for line in archivo5:
    sep=line.split()
    N=int(sep[0])
    dt=float(sep[1])
    Ns_5.append(N)
    dts_5.append(dt)

for line in archivo6:
    sep=line.split()
    N=int(sep[0])
    dt=float(sep[1])
    Ns_6.append(N)
    dts_6.append(dt)

for line in archivo7:
    sep=line.split()
    N=int(sep[0])
    dt=float(sep[1])
    Ns_7.append(N)
    dts_7.append(dt)

archivo1.close()
archivo2.close()
archivo3.close()
archivo4.close()
archivo5.close()
archivo6.close()
archivo7.close()


plt.plot(Ns_1,dts_1,label="caso 1",marker="o")
plt.plot(Ns_1,dts_2,label="caso 2",marker="o")
plt.plot(Ns_1,dts_3,label="caso 3",marker="o")
plt.plot(Ns_1,dts_4,label="caso 4",marker="o")
plt.plot(Ns_1,dts_5,label="caso 5",marker="o")
plt.plot(Ns_1,dts_6,label="caso 6",marker="o")
plt.plot(Ns_1,dts_7,label="caso 7",marker="o")
plt.loglog()
plt.xticks([10,20,50,100,200,500,1000,2000,5000,6500],[10,20,50,100,200,500,1000,2000,5000,6500])
plt.yticks([0.0001,0.001,0.01,0.1,1,10,60,600],["0.1ms","1ms","10ms","0.1s","1s","10s","1min","10min"])
plt.xlabel("Tamaño matriz N")
plt.ylabel("Tiempo[s]")
plt.title("Caso solve con tipo de datos double")
plt.legend()
plt.show()