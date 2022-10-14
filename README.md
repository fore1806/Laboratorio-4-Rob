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

En cuanto a la cinemática directa se procede hallando las matrices de transformación homogenea para cada articulación.

