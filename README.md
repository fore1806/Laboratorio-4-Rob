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
