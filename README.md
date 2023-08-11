<p align="center">
<img src=https://github.com/Lmart89/MikroPrintr-3D/assets/42391946/adc98b10-5be8-494d-9cd8-6f2932e612d1">
</p>

# MikroPrintr-3D.
## Una placa controladora de impresion 3d, compacta, de bajo coste basada en Arduino.

<p align="center">

   <img src="https://img.shields.io/badge/STATUS-EN%20DESAROLLO-green"> <img src="https://img.shields.io/github/license/Lmart89/Mikroprintr-3D"> <img src="https://img.shields.io/badge/Basado_en-Arduino-blue"> <img src="https://img.shields.io/github/forks/Lmart89/MikroPrintr-3D?color=green">

</p>

## 💡 Origen del Concepto

Mikropintr es el resultado propio de ideas tomadas de proyectos como Sinaptec (https://reprap.org/wiki/SinapTec), Morpheus (https://github.com/pscrespo/Morpheus-STM32) entre otros que ofrecen una solucion compacta y de bajo coste para la construccion de una placa controladora de impresion 3D. sin embargo el gran limitante de estas placas es que requieren modificar el firmware para lograr funcionar aunque no al 100% en muchos casos.
Es asi como MikroPrintr pretende ofrecer una solucion de bajo coste, a la vez de ser 100% compatible con Marlin sin sacrificar ninguna de sus capacidades, todo esto contenido en una placa compacta. para ello se opto por una version reducida de Arduino Mega.

## :heavy_check_mark: Características de MikroPrintr.

- MCU: Arduino Mega 2560 Pro-Micro. Una versión compacta del Arduino Mega 2560 pero con las mismas capacidades.

- Soporte Estándar de Marlin, sin necesidad de modificaciones especiales para el soporte de Hardware. 

- Diseñada bajo el estandar RAMPS 1.4.

- Fabricación de bajo coste. uso de componentes THT (Trough Hole) para fabricacion manual. 

- Tamaño Reducido. 103 mm x 90mm. a 1 sola capa, o producir a dos capas si se desea.

- Soporte Estándar para pantallas LCD. Permite accesorios como la smart reprap controller (lcd 2004) o la smart reprap full graphic controller (lcd 12864). no necesita el adatador para la conexion.
  
- Soporte para Módulo Wifi. la placa ofrece la conexión para añadir un módulo wifi esp8266-01 o esp8266-01s, conocidos como Esp-01. se recomienda la versión Esp-01s, por la gran mejora del consumo de energía, y en ambos casos se requiere un regulador de nivel lógico de 5v a 3.3v para los módulos. se ofrece una PCB para montaje del módulo si prefiere hacerlo personalmente. 

- PSU ATX. diseñada para funcionar con una fuente de pc, que pueda ofrecer por lo menos 20A en una linea de 12v y max. 6A en la linea de +5v y 12v adicionales.

- Proteccion contra corriente y sobrecarga por dos conexiones de fusibles. 


## :chart_with_upwards_trend: Estado del Proyecto.

<img src="https://img.shields.io/badge/STATUS:-%20ACTIVO-green"> <img src="https://img.shields.io/github/last-commit/Lmart89/mikroprintr-3D/main"> <img src="https://img.shields.io/badge/Work%20in%20_Progress-8A2BE2"> 

:construction: Proyecto en construcción :construction:

actualmente se encuentra en fase de prueba, y en constante revisión para mejoras y constante evolución.
La version actual de los archivos es la version 1G. Debido a la posibilidad de contener algunos "bugs", son por el momento versiones de prueba,
y por lo tanto consideradas versiones preliminares o candidatas antes de una liberacion al publico.

Con la elaboracion de las primeras placas elaboradas profesionalmente se esperan poder continuar el siguiente proceso de pruebas. aqui dejo una vista de la pcb fabricada.

![MK2560EM-G v1G-6](https://github.com/Lmart89/MikroPrintr-3D/assets/42391946/b7758e84-6ec3-454d-9e4d-8ec850b0c561) ![pcb1 (2)](https://github.com/Lmart89/MikroPrintr-3D/assets/42391946/c738c8f0-bd2f-444a-a74a-e2b8dbaf5939)







## :books: Recursos adicionales.

he adjuntado a este proyecto algunos modelos de impresoras 3d que pueden ser de interés si estas construyendo tu propia impresora desde 0. he añadido 3 variantes, puedes consultar en los enlaces a sus archivos.

- Me Mini 3d Printer - la mas completa y compleja.
  
 ![featured_preview_ME_-_mini_-_12](https://github.com/Lmart89/MikroPrintr-3D/assets/42391946/46812bdc-8866-457e-95c1-b1a581d16094)

:earth_americas: link oficial. https://www.thingiverse.com/thing:5140212. lastimosamente el sitio oficial con las instrucciones y lista de materiales para su montaje fue eliminado. solo quedan los archivos en Thingiverse y printables.

- Skylab2 - una construccion sencilla y simple, recomendada para empezar. 
para esta version he añadido imagenes con las dimensiones de las piezas en 3D para facilitar laa busqueda de los componentes mecanicos como rodamientos y varillas para el montaje de esta impresora.

![skylab2_1](https://github.com/Lmart89/MikroPrintr-3D/assets/42391946/04487701-f611-479c-83f3-e13e89c8b58e)

:earth_americas: link oficial. https://www.thingiverse.com/thing:4624533.

- Prusa mini- la version mini de la prusa i3, complejidad media.
  <img src="https://img.shields.io/badge/IMPORTANTE-blue"> Requiere la mayoria de sus piezas en ABS. 

![prusa_mini](https://github.com/Lmart89/MikroPrintr-3D/assets/42391946/c5f544c7-e0e4-4b27-9812-66b6006dfd71)


🌎 sitio oficial: https://www.printables.com/es/model/57214-mini-printable-parts/files

los archivos stl de estos modelos se encuentran en la carpeta "printable parts".

## :hammer_and_pick: Proyectos en conjunto. 
De momento estoy trabajando en el desarrollo de un software host propio para manejar la placa.

Si te interesa mi proyecto y deseas colaborar en el desarrollo, puedes contactarme, dejandome un mensaje o un request o solicitud de cambio via github.

Deseo que este proyecto pueda ser de utilidad para ti, maker. con :heart: desde Colombia 🇨🇴 para el mundo 🌎. :smile:

### <h4> :heavy_exclamation_mark: al hacer uso de los archivos publicados en este repositorio, el usuario acepta y asume su propia responsabilidad y riesgo por el uso y/o manipulacion de los archivos ofrecidos en este repositorio. :heavy_exclamation_mark: </h>

