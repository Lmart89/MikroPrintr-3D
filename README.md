# MikroPrintr-3D.


MikroPrintr-3D es una placa controladora para impresora 3d, de bajo coste basada en el microcontrolador Arduino Mega 2560 Pro-Micro, una versión compacta del Arduino Mega 2560, manteniendo las mismas prestaciones que la versión estándar. 
 

## Origen del Concepto. 

La inspiración proviene de proyectos similares de placas controladoras de impresión 3d de bajo coste, como Sinaptec AT328, o Morpheus Board.
Sin embargo la desventaja principal de estos proyectos radica en el uso de microcontroladores, aunque de bajo coste, requieren modificaciones específicas en el firmware de Marlin, y aunque están soportadas de manera oficial, no elimina las maniobras de manipulación y tampoco significa que todas las funcionalidades estén soportadas de manera nativa o el uso de una versión limitada de otros firmwares.

Esta necesidad llevo a la creación de una solución más completa así como estándar que permita aprovechar las funcionalidades de Marlin sin requerir mayores modificaciones. una solución que ofrezca simplicidad.

## Características de MikroPrintr-3D.

- MCU: Arduino Mega 2560 Pro-Micro. es una versión compacta del Arduino Mega 2560 y posee las mismas capacidades del Arduino Mega estándar, con la ventaja de un tamaño sumamente reducido. El Soporte de Marlin es totalmente nativo y funcional, por lo que no se requieren modificaciones especiales del Firmware.

- Soporte Estándar de Marlin, sin necesidad de modificaciones especiales para el soporte de Hardware. 
solo se requiere las modificaciones básicas de los archivos de configuración.
La placa está diseñada bajo el estándar de ramps shield.

- Fabricación de bajo coste. Tanto para la elaboración de la PCB, como la adquisición de los componentes activos y pasivos que integran la placa. 

- Tamaño Reducido. cumple con no sobrepasar los 1000 mm2 lo que es igual a un tamaño de fabricación de 100x100 mm. 

- Integración en una sola placa. El diseño sigue el estándar de Ramps 1.4 para las conexiones, de manera que no solamente existe soporte nativo, sino que además la PCB es de fácil fabricación al ser mayormente de una sola capa. si se elabora a mano, se recomienda un método de mejor precisión, o el uso de una cnc, esto debido a las zonas donde las pistas son delgadas y cercas unas de las otras.

- Soporte Estándar para pantallas LCD. La placa permite el uso de la smart reprap controller (lcd 2004) o la smart reprap full graphic controller (lcd 12864), sin requerir el uso del adaptador para el shield ramps, solamente conectando los cables a los pines EXP1 y EXP2 respectivamente que ya vienen integrados en la placa. 
 
- Soporte para Módulo Wifi. la placa ofrece la conexión para añadir un módulo wifi esp8266-01 o esp8266-01s, conocidos como Esp-01. se recomienda la versión Esp-01s, por la gran mejora del consumo de energía, y en ambos casos se requiere un regulador de nivel lógico de 5v a 3.3v para los módulos. se ofrece una PCB para montaje del módulo si prefiere hacerlo personalmente. 

- Fuente de Alimentación de computador como apoyo principal de PSU. al ser de bajo coste ofrecen el soporte perfecto como fuente de alimentación. se implementa una conexión para el encendido de la fuente de manera física, a futuro se implementará via software. la recomendacion es usar una fuente de mínimo 550 watts. con una salida de 12v a 20A (el conector Molex de 4 pines a CPU). 
la otra conexión a 12v funciona a un máximo de 5-6A, ideal para el resto de la placa. 


## Estado Actual del Proyecto.

actualmente se encuentra en fase de prueba, y en constante revisión para mejoras y constante evolución.
actualmente la revisión actual es la 1G. 
Las mejoras y/o modificaciones se publicarán regularmente. 

Si te interesa mi proyecto y deseas colaborar en el desarrollo, puedes contactarme. 

### al hacer uso de los archivos de este repositorio, el usuario asume la propia responsabilidad y riesgo de uso bajo si mismo. 

