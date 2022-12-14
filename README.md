# Cuarto Laboratorio - Cinemática Directa - Phantom X - ROS :robot: 
 
Cuarto laboratorio de la asignatura Robótica de la Universidad Nacional de Colombia en su sede Bogotá. 
 
## Autores :busts_in_silhouette: 
 



|               Nombre               |GitHub nickname| 
|------------------------------------|---------------| 
|  Nikolai Alexander Caceres Penagos |[nacaceresp](https://github.com/nacaceresp)| 
|     Andrés Felipe Forero Salas     |[fore1806](https://github.com/fore1806)| 
|  Iván Mauricio Hernández Triana    |[elestrategaactual](https://github.com/elestrategaactual)|

## Introducción

El problema cinemático directo es uno de los conceptos fundamentales dentro de la formación de un ingeniero en el campo de la robótica, de esta forma la implementación de estos modelos a un manipulador físico como el Phantom X a través del entorno ROS, determina una posibilidad enorme de apropiamiento del conocimiento por parte de los estudiantes de la utilidad de los modelos de cinematica directa.

## Solución planteada

### Configuración inicial Dynamixel Workbench y entorno ROS

La configuración inicial del entorno software Dynamixel Workbench se realizó siguiendo el repositorio [Robotics - UNAL - LAB3](https://github.com/fegonzalez7/rob_unal_clase3.git) lo que permitió al equipo de trabajo tener un acercamiento inicial al movimiento del manipulador Phantom X, de este proceso, se encontraron diferentes características asociadas a cada una de las articulaciones del manipulador.

![](https://github.com/fore1806/Laboratorio-4-Rob/blob/master/DIAGRAMAS-IMAGENES/DYNAMIXEL/m1.jpeg)

![](https://github.com/fore1806/Laboratorio-4-Rob/blob/master/DIAGRAMAS-IMAGENES/DYNAMIXEL/m2.jpeg)

![](https://github.com/fore1806/Laboratorio-4-Rob/blob/master/DIAGRAMAS-IMAGENES/DYNAMIXEL/m3.jpeg)

![](https://github.com/fore1806/Laboratorio-4-Rob/blob/master/DIAGRAMAS-IMAGENES/DYNAMIXEL/m4.jpeg)

![](https://github.com/fore1806/Laboratorio-4-Rob/blob/master/DIAGRAMAS-IMAGENES/DYNAMIXEL/m5.jpeg)

Dentro de las propiedades importantes que se observan en las imágenes anteriores destaca el rango articular de cada una de las articulaciones.

Posteriormente, se clonó el repositorio de GitHub [dynamixel_one_motor](https://github.com/fegonzalez7/dynamixel_one_motor.git) dentro de la carpeta creada de ***catkin_lab_2_ws*** y se siguieron los pasos especificados en el README, teniendo en cuenta que previo a lanzar el controlador de los motores del Phantom X, hacia falta una línea de comando como se muestra a continuación.

```
    catkin build dynamixel_one_motor
    source devel/setup.bash
    roslaunch dynamixel_one_motor one_controller.launch
```

### Código Solución

Para desarrollar la solución del laboratorio, el equipo de trabajo se basó en el anterior repositorio remoto, comenzando por modificar el archivo [basic.yaml](https://github.com/fegonzalez7/dynamixel_one_motor/blob/master/config/basic.yaml), en el que se debian crear las instancias de las 4 articulaciones restantes del manipulador.

A continuación, el código de solución fue desarrollado en el lenguaje de programación Python. En primer lugar, se programaron las posiciones articulares requeridas por el enunciado del laboratorio, para lo cual se utilizó la libreria numpy.

```python
    import numpy as np
    q0= [0,0,0,0,0]
    q1=np.multiply([-20,20,-20,20,0],np.pi/180)
    q2=np.multiply([30,-30,30,-30,0],np.pi/180)
    q3=np.multiply([-90,15,-55,17,0],np.pi/180)
    q4=np.multiply([-90,45,-55,45,10],np.pi/180)
    q5= np.multiply([0,-110,90,5,0],np.pi/180)    
```

Seguidamente, se desarrolló una especie de interfaz que permitiera al usuario establecer las posiciones articulares a través del teclado de su ordenador.


```python
    key=input()
    if key == 'z' or key == 'Z':
        q=q0
        key = ' '
    elif key == 'x' or key == 'X':
        q=q1
        key = ' '
    elif key == 'c' or key == 'C':
        q=q2
        key = ' '
    elif key == 'v' or key == 'V':
        q=q3
        key = ' '
    elif key == 'b' or key == 'B':
        q=q4
        key = ' '
    elif key == 'n' or key == 'N':
        q=q5
        key = ' '   
```

Finalmente, se debia programar el movimiento de las articulaciones, para lo cual se tomó como base el script [jointPub.py](https://github.com/fegonzalez7/dynamixel_one_motor/blob/master/scripts/jointPub.py), modificándolo para poder enviar señales a los 5 motores. En base al enunciado del laboratorio, en el que se pedia realizar el movimiento de manera secuencial, se debió utilizar la estructura 5 veces, añadiendo el siguiente motor en cada iteración como puede observarse en el script [jointPub.py](https://github.com/fore1806/Laboratorio-4-Rob/blob/master/catkin_lab_2_ws/src/dynamixel_one_motor/scripts/jointPub.py). En este archivo, adicionalmente, se redujo la velocidad del sistema para realizar el movimiento de manera más pausada.

### Cinemática directa 

Con el fin de desarrollar la cinemática directa del Phantom X se procede inicialmente tomando las medidas que permiten encontrar los parámetros DHstd del mismo. A continuación se muestra un esquema ilustrativo con dichas medidas y con la asignan de los marcos de referencia respectivos.

![](https://github.com/fore1806/Laboratorio-4-Rob/blob/master/DIAGRAMAS-IMAGENES/ParametrosDH/ParametrosRobot.png)

Teniendo en cuenta este diagrama, se encuentran los parámetros de articulación y eslabón para el manipulador.

![](https://github.com/fore1806/Laboratorio-4-Rob/blob/master/DIAGRAMAS-IMAGENES/ParametrosDH/ParametrosDH.png)

Con estos parámetros se hallan las matrices de transformación homogéneas para cada uno de los sistemas y finalmente se halla el modelo geométrico directo a partir del modelo interno de la cadena cinemática. Se obtienen entonces la siguiente matriz con sus respectivos parámetros:

![](https://github.com/fore1806/Laboratorio-4-Rob/blob/master/DIAGRAMAS-IMAGENES/ParametrosDH/Matriz1.png)
![](https://github.com/fore1806/Laboratorio-4-Rob/blob/master/DIAGRAMAS-IMAGENES/ParametrosDH/Matriz2.png)

Teniendo en cuenta las configuraciones especificadas se encuentra la posición y orientación del último sistema coordenado respecto al marco {0}. Para la posición HOME, la posición del robot debe ser la siguiente:

![](https://github.com/fore1806/Laboratorio-4-Rob/blob/master/DIAGRAMAS-IMAGENES/Posiciones/Home.jpg)

La cual coincide con lo obtenido en la práctica:

![](https://github.com/fore1806/Laboratorio-4-Rob/blob/master/DIAGRAMAS-IMAGENES/Fotos/q0.jpeg)

En lo que respecta a la posición 1, se debe llegar a la siguiente figura:

![](https://github.com/fore1806/Laboratorio-4-Rob/blob/master/DIAGRAMAS-IMAGENES/Posiciones/Posicion1.jpg)

Lo cual se corrobora en la postura obtenida en el laboratorio:

![](https://github.com/fore1806/Laboratorio-4-Rob/blob/master/DIAGRAMAS-IMAGENES/Fotos/q1.jpeg)

La posición 2 debe ser:

![](https://github.com/fore1806/Laboratorio-4-Rob/blob/master/DIAGRAMAS-IMAGENES/Posiciones/Posicion2.jpg)

Efectivamente es:

![](https://github.com/fore1806/Laboratorio-4-Rob/blob/master/DIAGRAMAS-IMAGENES/Fotos/q2.jpeg)

Ya para la posicion 3 se busca lo siguiente:

![](https://github.com/fore1806/Laboratorio-4-Rob/blob/master/DIAGRAMAS-IMAGENES/Posiciones/Posicion3.jpg)

Se obtiene:

![](https://github.com/fore1806/Laboratorio-4-Rob/blob/master/DIAGRAMAS-IMAGENES/Fotos/q3-1.jpeg)

Para ver de mejor manera esta configuración se muestra la siguiente figura.

![](https://github.com/fore1806/Laboratorio-4-Rob/blob/master/DIAGRAMAS-IMAGENES/Fotos/q3-2.jpeg)

En lo que respecta a la posición 4 se debe llegar a la siguiente figura:

![](https://github.com/fore1806/Laboratorio-4-Rob/blob/master/DIAGRAMAS-IMAGENES/Posiciones/Posicion4.jpg)

Se llega a lo siguiente:

![](https://github.com/fore1806/Laboratorio-4-Rob/blob/master/DIAGRAMAS-IMAGENES/Fotos/q4-1.jpeg)

Adicionalmente, se muestra otra vista del robot en esta pose.

![](https://github.com/fore1806/Laboratorio-4-Rob/blob/master/DIAGRAMAS-IMAGENES/Fotos/q4-2.jpeg)

Finalmente, la posicion de descanso debe ser de la siguiente manera:

![](https://github.com/fore1806/Laboratorio-4-Rob/blob/master/DIAGRAMAS-IMAGENES/Posiciones/Recogida.jpg)

En la práctica se llega a esta posición en la cual el robot permanece estable y en general sin alteraciones en su estructura incluso si a este se le quita su suministro de energia. 

![](https://github.com/fore1806/Laboratorio-4-Rob/blob/master/DIAGRAMAS-IMAGENES/Fotos/q5.jpeg)

### Video de funcionamiento

A continuación, se puede observar el video del funcionamiento del robot, al ingresar cada uno de los comandos especificados.

https://user-images.githubusercontent.com/42379708/195968567-99f284ed-60b2-4692-9420-3c23cdecf806.mp4

### Conclusiones

- Se evidencia la facilidad en la conexión del manipulador Phantom X con el lenguaje de programación Python para el envio de instrucciones.

- Se comprueba la pertinencia del modelo cinemático directo del robot implementado gracias a las herramientas del Toolbox RVC de Peter Corke, al evidenciar la gran correlación con las posturas del manipulador físico.

- Se encuentra gran utilidad en método estándar de Denavit-Hartenberg estándar para representar la postura del robot simplificando el número de parámetros requeridos por cada una de las articulaciones y eslabones del manipulador.
