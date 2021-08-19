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
 
 Tarea 3 (P0E3)
 
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
