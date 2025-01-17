# MCOC2021-P0

# Mi computador principal

* Marca/modelo: Armado
* Tipo: Desktop
* Año adquisición: 2018
* Procesador:
  * Marca/Modelo: Intel Core i3-8100
  * Velocidad Base: 3.60 GHz
  * Velocidad Máxima: 3.60 GHz
  * Numero de núcleos: 4 
  * Numero de hilos: 4
  * Arquitectura: x86_64
  * Set de instrucciones: Intel SSE4.1, Intel SSE4.2, Intel AVX2
* Tamaño de las cachés del procesador
  * L1: 256 KB
  * L2: 1 MB
  * L3: 6 MB
* Memoria 
  * Total: 16 GB
  * Tipo memoria: DDR4
  * Velocidad 2400 MHz 
  * Numero de (SO)DIMM: 2
* Tarjeta Gráfica
  * Marca / Modelo: Amd Radeon Rx 570
  * Memoria dedicada: 4 GB
  * Resolución: 1920 x 1080
* Disco 1: 
  * Marca: Crucial
  * Tipo: SSD
  * Tamaño: 500 GB
  * Particiones: 3
  * Sistema de archivos: NTFS
* Disco 2: 
  * Marca: Western digital
  * Tipo: HDD
  * Tamaño: 1TB
  * Particiones: 1
  * Sistema de archivos: NTFS

  
* Dirección IP (Interna, del router): 192.168.100.1
* Dirección IP (Externa, del ISP): 2800:300:6271:6c70::1
* Proveedor internet: Entel Chile S.A.

PREGUNTA 2

¿Cómo difiere del gráfico del profesor/ayudante?
 R:Se puede observar como el grafico se comporta de manera similar al del ayudante, claramente habrá diferencias ya que no es   el mismo computador y no se probaron con las mismas cantidades de matrices, este comportamiento similar se puede observar en ambos gráficos (uso de memoria y tiempo transcurrido).

¿A qué se pueden deber las diferencias en cada corrida?
 R:Se pueden deber a la potencia de hardware de cada computador, como la memora ram, la cantidad de núcleos y memoria cache del procesador, como también el tamaño de matrices que se probaron, ya que matrices de mayor tamaño necesitaran mayores recursos.

El gráfico de uso de memoria es lineal con el tamaño de matriz, pero el de tiempo transcurrido no lo es ¿porqué puede ser?
 R:Puede ser debido a la cantidad de memoria que deja reservada para continuar haciendo procesos, ya que al terminar de ejecutar una matriz grande al empezar otra matriz tendrá menor memoria para ocupar por un momento.

¿Qué versión de python está usando?
 R:3.9.6
 
¿Qué versión de numpy está usando?
 R:1.21.1

Durante la ejecución de su código ¿se utiliza más de un procesador? Muestre una imagen (screenshot) de su uso de procesador durante alguna corrida para confirmar. 
 R: Como se puede ver se están usando los 4 núcleos del procesador
 
 ![image](https://user-images.githubusercontent.com/88348645/128414845-eb59632c-f5e4-4eb4-af60-307d25af9d1c.png)
 
 
 ![image](https://user-images.githubusercontent.com/88348645/128416213-c4afa072-7d8e-4a88-9216-aaa80c392212.png)
 
 # Tarea 3 (P0E3)
 
 Durante la corrida de los diferentes programas se observo el uso del procesador y memoria que se utilizaban, mientras corrian los programas en los distintos casos se pudo percibir que tenian un patron, el cual era que mientras mas chica era el tamaño de las matrices, menos procesador y memoria se utilizaban, en cambio cuando el tamaño de las matrices crecian el uso de cpu y memoria aumentaban como se muestra en las siguientes imagenes.
 
 ![single](https://user-images.githubusercontent.com/88348645/129987950-30c94d85-42f1-452e-be56-1dd9a0f61126.png)
 
 ![single2](https://user-images.githubusercontent.com/88348645/129987958-87b816c2-e395-430c-ba24-0cf023a6a39c.png)

Tambien se puede ver como los 4 nucleos del procesador trabajan al mismo tiempo y con practicamente la misma intensidad, esto es debido a que se dividen entre los 4 la tarea de realizar el codigo, realizando calculos simultaneamente, otro aspecto que influye es la memoria cache del procesador, ya que aqui es donde almacena los datos e instrucciones que mas esta utilizando en el momento, por lo cual si mi procesador tuviera mas nucleos y memoria cache, el codigo podria realizarse con mayor rapidez .

La unica matriz que no se invirtio fue al usar numpy con el tipo de dato half, todos los demas casos tuvieron matrices invertidas.
Al observar los graficos, se llego a la conclusion que al invertir la matriz tanto con numpy o scipy tienen un rendimiento muy similar, ya que ambos estan cerca de los 10 segundos, donde el caso de scipy.linalg.inv con overwrite_a=True llegaba al menor tiempo, aunque la diferencia es casi nula.

![longdouble_caso_1](https://user-images.githubusercontent.com/88348645/129989567-b00d7643-46db-43ea-acf4-495ff6cf6df9.png)
![longdouble_caso_2](https://user-images.githubusercontent.com/88348645/129989573-d7e4f5c5-e9e5-42ea-a5e4-97c2b9efc0d5.png)
![longdouble_caso_3](https://user-images.githubusercontent.com/88348645/129989576-0e3720f6-5379-41f3-ba2b-6c1d5b57bc35.png)
 
esto ocurre para los 4 tipos de datos, pero con longdouble es mas perceptible.

# Tarea 4 (P0e4)

En el caso de solve para los datos tipo single se ve para la mayoría de los casos una pequeña mejora en el tiempo, esto puede ser a que los datos tipo single tienen un tamaño menor a los double

![caso solve con tipos de datos double](https://user-images.githubusercontent.com/88348645/130308369-8a6b0512-8781-4f1a-9bb5-75a8947e8e59.png)

![caso solve con tipos de datos single](https://user-images.githubusercontent.com/88348645/130308370-3ca36741-c0fe-408c-b478-b7456c2c4397.png)


Pero en ambos tipos de datos se cumple que al ocupar el caso 3 (assume_a= “pos”) se tiene el menor tiempo de ejecución, por lo que es el mas optimo y en este caso el tiempo de ejecución de los datos singles es menor al final.

![comparacion solve double vs single](https://user-images.githubusercontent.com/88348645/130308373-54b12195-dd60-4b38-8269-6759cdeb3dd8.png)


En el caso de eigh pasa algo similar que en solve con los datos de tipo double y single, ya que single vuelve a tener menores tiempo de ejecución

![caso eigh con tipo de datos double](https://user-images.githubusercontent.com/88348645/130308374-27feb10b-db3f-4984-8691-838ce3ed881e.png)

![caso eigh con tipo de datos single](https://user-images.githubusercontent.com/88348645/130308376-8cd11761-15e8-4ca5-bfa3-6270b96266ab.png)


En ambos casos, el caso 3a y 3b (overwrite_a=False y overwrite_a=True) dan los menores tiempo de espera siendo prácticamente iguales, esto puede deberse en que en estos procesos se lleva muchos más procesos que en el solve, por lo que los tipos de datos no deben influir mucho.

![comparacion eigh double vs single](https://user-images.githubusercontent.com/88348645/130308383-bebd682c-916b-42ef-9803-56391ca4a21c.png)

En el caso de uso de cpu era bastante desigual para solve y eigh, esto puede deberse a la rapidez con la que resolvia las matrices, siendo solve la que más cpu ocupo, esto puede deberse a que se resolvieron matrices de mayor tamaño que en el caso de eigh, esto simplemente se debio a que en el caso de eigh al sobrepasar matrices de tamaño 3000 este se demoraba más de 2 minutos, pero al bajar a 2700 baja considerablemente su tiempo, llegando a tiempos cercanos al minuto con diez segundo.

![cpu_solve_1](https://user-images.githubusercontent.com/88348645/130308454-a22dd626-dd88-4e59-b095-abbfebeff1a3.png)
![cpu_eigh_1](https://user-images.githubusercontent.com/88348645/130308456-8d3f2cfe-4a1e-4725-9629-9d87e6c7adf1.png)

# Tarea 5(P0E5)

```
#tipo de dato double, matriz laplaciana dispersa
def matriz_laplaciana(N, t=double):
    e= sparse.eye(N,dtype=double)-sparse.eye(N,N,1,dtype=double)
    return (e+e.T)
#tipo de dato double, matriz laplaciana llena
def matriz_laplaciana(N, t=double):
    e= eye(N)-eye(N,N,1)
    return t(e+e.T)    
```
Se puede observar como la matriz llena al tener que guardar los ceros de la matriz, ósea tener que guardar más información es más lenta al momento de ensamblar las matrices, como al momento de resolver la multiplicación de matrices laplacianos, por esto mismo en el caso de la matriz llena se realizaron cálculos con tamaño de matrices menores a la de matrices dispersa, ya que se demoraban unos 2 minutos aproximadamente en resolver las 10 corridas, en cambio al realizar los cálculos con la matriz dispersa se pudo llegar a tamaño de matrices de 20000 sin problemas, esto posiblemente debido a que no necesitaba utilizar mucha memoria del procesador, ya que solo guarda los valores que no son ceros de la matriz, estos son una cantidad de datos muy chicas comparadas con la cantidad de ceros que si tendría que guardar. En el caso de la multiplicación de matrices sucede lo mismo, es más eficiente el caso de la matriz dispersa que la matriz llena.

#matriz llena
![grafico_mat_llena](https://user-images.githubusercontent.com/88348645/131186197-2662c48c-5389-4f0c-8514-319ac5a6c581.png)

#matriz dispersa
![grafico_mat_dispersa](https://user-images.githubusercontent.com/88348645/131186245-4797115c-be95-435f-9efe-e76bb469616a.png)

# Tarea 6(P0E6)

```
#tipo de dato double, matriz laplaciana llena
def matriz_laplaciano(N, t=double):
       e= eye(N)-eye(N,N,1)
       return t(e+e.T)
#tipo de dato double, matriz laplaciana dispersa     
def matriz_laplaciana(N, t=double):
    e= sp.eye(N,dtype=double)-sp.eye(N,N,1,dtype=double)
    return (e+e.T)
```

Para el caso de solve la matriz llena tiene mayor tiempo de ensamblado y de solución que la matriz dispersa, siendo que la matriz llena llega a tamaño de matrices N de 6500, en cambio la matriz dispersa llega a un tamaño de 20000 sin problemas, con tiempos de ensamblado y solución muy inferiores a los de matrices llenas, manteniendo sus tiempos de solución bastante constantes sim importar el aumento del tamaño de las matrices, en cambio para matrices llenas los tiempo de ensamblado y solución tienden a aumentar con el aumento del tamaño de las matrices.

![matriz_llena_solve](https://user-images.githubusercontent.com/88348645/132042575-aba07c60-d40f-457d-b1ce-89f241129d25.png)
![matriz_llena_inv](https://user-images.githubusercontent.com/88348645/132042580-e3d14daf-5cf6-4e6d-99f7-ebcdcb3b8f3d.png)


Para el caso de inv sucede algo curioso, ya que el tiempo de ensamblado de la matriz llena es mayor al de las matrices dispersas, pero en el tiempo de solución se parecen bastante, incluso las matrices llenas lograron llegar a un N de 5500, en cambio las matrices dispersas solo llegaron a 5000 en el límite de tiempo de 2 minutos, esto se puede deber a que al llegar a un numero de N=100 las matrices llenas disminuyen su tiempo de solución y ensamblaje, después vuelve aumentar con el aumento del tamaño de las matrices, en cambio con las matrices dispersas al llegar a 100 se mantiene constante el tiempo de solución, pero luego sigue aumentando con el aumento del tamaño de las matrices, el tiempo de ensamblaje se mantiene mayormente constante sin importar el tamaño de las matrices. 

![matriz_llena_inv](https://user-images.githubusercontent.com/88348645/132042604-10bec12b-4ede-4abf-bf8d-786f32ab13be.png)
![matriz_dispersa_inv](https://user-images.githubusercontent.com/88348645/132042610-dd5969bd-5772-45e4-b650-c2fcd16c2cea.png)


Por ultimo las corridas para todos los casos son muy estables, por lo que se pudo observar una de cada 10 corridas tiene algún cambio mayor, pero en la mayoría se mantienen bastante cerca y con pocos cambios

    

