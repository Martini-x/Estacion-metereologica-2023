# Anteproyecto: Estacion metereologica   |    Sanchez|Acosta

### Indice 


- [Descripcion del proyecto](#descripcion-del-proyecto)
- [Descripcion de la problematica](#descripcion-de-la-problematica)
- [Caracterisiticas del sistema](#caracterisiticas-del-sistema)
- [Estado del arte / Antecedentes](#estado-del-arte--antecedentes)
- [Estudio de factibilidad](#estudio-de-factibilidad)
- [Diagrama de bloques](#diagrama-de-bloques)
- [Analisis de gastos](#analisis-de-gastos)
- [Planificacion y distribucion de tareas](#planificacion-y-distribucion-de-tareas)


---
## Descripcion del proyecto

### *Descripcion de la problematica:

- Una pequeña estación meteorológica podría solucionar diversas problemáticas relacionadas con la recopilación de datos climáticos y el monitoreo de las condiciones atmosféricas en una ubicación específica. Algunas de las problemáticas que podría abordar son:

  - Predicción del clima local

  - Alertas tempranas de fenómenos meteorológicos extremos

  - Monitoreo de la calidad del aire

  - Investigación científica local

  - Agricultura y gestión del agua

  - Eficiencia energética

  - Seguridad en el transporte

En resumen, una pequeña estación meteorológica puede solucionar problemáticas relacionadas con la falta de datos climáticos precisos y en tiempo real, y puede tener una amplia gama de aplicaciones en diversas áreas, desde la planificación diaria hasta la toma de decisiones críticas en sectores como la agricultura, la investigación científica y la seguridad.

---

### *Caracterisiticas del sistema:
- Una pequeña estación meteorológica generalmente está diseñada para recopilar datos básicos sobre las condiciones climáticas en una ubicación específica. A continuación, se presentan algunas características comunes de una pequeña estación meteorológica:

  - Sensores e instrumentos

  - Transmisión de datos

  - Registro y almacenamiento de datos

  - Alimentación energética
  
  - Durabilidad y protección

  - Interfaz de usuario

  - Conectividad y compatibilidad


- Existen varias mejoras que se podrían implementar en una pequeña estación meteorológica para ampliar su funcionalidad y precisión. Algunas de estas mejoras podrían incluir:

    - Sensores adicionales
    - Comunicación mejorada
    - Integración con sistemas de automatización

    - Interfaz de usuario avanzada

    - Integración con sistemas de alerta temprana

    - Acceso a datos históricos y almacenamiento en la nube

Estas mejoras podrían hacer que la pequeña estación meteorológica sea aún más versátil y valiosa para una variedad de aplicaciones, desde la toma de decisiones en la agricultura y la investigación científica hasta el monitoreo ambiental y la planificación urbana.

---

### *Estado del arte / Antecedentes:

- Durante la busqueda de documentacion para el proyecto, ademas de la busqueda de caracterisiticas, componentes y tecnologias, se buscó estaciones metereologicas ya creadas, se trató de enfocar la busqueda en proyectos a nivel comercial/profesional para informarnos sobre las tecnologias usadas y en proyectos academicos para ver como se aplican dichas tecnologias a un nivel mas amateur.

  - Proyecto comercial: En el mercado existen una infinidad de propuestas de estaciones metereologicas, varian en precios, prestaciones, precision, conectividad, registro, etc. sin embargo existen dos que se asimilan mas a las expectativas sobre el proyecto a realizar.
  
    *[Daza DZWT1081](http://www.sisteco-web.com.ar/products/14-estacion-meteorologica-daza-dzwt1081-wireless.html): Esta estacion permite medir temperatura, humedad, direccion y velocidad del viento, precipitacion, dichas mediciones se muestran mediante un display (Este proyecto abarca los items obligatorios)

    *[Daza DZWH2900](http://www.sisteco-web.com.ar/products/813-estacion-meteorologica-daza-dzwh2900-color-wifi-lux-uv-viento-lluvia-usb.html): Este modelo tiene las mismas prestaciones que el anterior, pero ademas tiene indice UV, alertas para los parametros, previsiones, regsitros, botonera, y conexion wifi para transmision de datos. (Este proyecto abarca los items obligatorios y opcionales)


  - [Proyecto amateur](https://youtu.be/LJszEpV9P0M): Este proyecto tiene algunas de las prestaciones que ofrece una estacion comercial, incluye medicion de temperatura, humedad, direccion y velocidad del viento, precipitacion, indice uv, display y conexion wifi para transmision de datos. Esta seria la expectativa del proyecto a presentar a fin de año.

---

### *Estudio de factibilidad:

  Como ya se vio en la investigacion de los antecedentes de la estacion metereologica existen muchas funciones que se pueden aplicar, pero en el proyecto se van a tomar como esenciales la implementacion de los siguientes items:
  
  -Microcontrolador: Se usara el ESP32 por su buena capacidad de procesamiento, cantidad de perifericos, cantidad de puertos, cantidad de puertos GPIO y mas iportante en este proyecto, comunicacion wifi y bluetooth.
  - Sensores:
    - Temperatura
    - Humedad
    - Precipitacion
    - Direccion del viento
    - Velocidad del viento
    - Presion atmosferica
    - Indice UV
  * Los sensores usados se explican en el diagrama de bloques
  
  - Muestra de Datos mediante display OLED
  - Muestra de datos mediante aplicacipn y pagina web (WIFI)
---

### *Diagrama de bloques:
![Diagrama de bloques](images/Diagrama-en-blanco.png)

- Sensores:
  - Temperatura y Humedad: Estas dos variables seran medidas por un mismo sensor en tiempo real. (Htu21d)
  - Precipitacion: Para esta variable se usara un sistema en el cual se ira midiendo la precipitacion de a 2ml, el sistema sera parecido a un "sube y baja", y cada vez que se realice un cambio de movimiento, mediante un iman acoplado a la estructura y a un sensor de efecto hall, se iran contando la cantidad de veces que esto sucede. (A3144)
  - Radiacion solar: Este sensor medira el nivel de radiacion uv en tiempo real, en base a esta medicion se mostrara, ademas del valor, la escala correspondiente de raciacion. (Guva-s12s)
  - Direccion del viento: Esta variable sera sensada con una veleta, para saber la posicion de la veleta se probara con sensores de efecto o con una serie de disco B&W pintados con distintas divisiones indicando distintas posiciones, para saber si el disco en cierta posicion es blanco o negro se usaran sensores infrarrojos. (Efecto hall: A3144) (Infrarrojo: Lm393)
  - Velocidad del viento: Esta variable sera sensada con un anemometro, la velocidad se medira por la cantidad de vueta que se den en un lapso de tiempo, se usara un sensior de efecto hall para saber cuando se dio una vuelta. (A3144)
  - Presion atmosferica: Este sensor medira la presion atmosferica en tiempo real. (BMP280)
 
- Procesamiento y almacenamiento: Todos los datos recibidos por los sensores seran procesados por el microcontrolador ESP32, y opcionalmente guardados en una unidad de almacenamiento. Estos datos seran mostrador por display y una aplicacion y/o pagina web.

- Entrega de datos: La entrega de datos que saldran, una vez procesados por el microcontrolador, seran mostrados por una pequeña pantalla OLED y por una pagina web o aplicacion, en estas dos ultimas se hara uso de la tecnologia WI-FI del micro para que sea posible la transmision de datos de manera inalambrica.

- Interaccion: Este apartado es opcional, pero se tiene pensado que mediante una botonera, el usuario, viendo en la pantalla OLED, pueda navegar entre menues para poder mas y de manera mas comoda la informacion.
---

### *Analisis de gastos:

<div align="center">

 Cant |                       Item                      | Precio
:----:|-------------------------------------------------|---------
 1    |          ESP32 - Wi-Fi & Bluetooth MCU          |  10 U$D*
 2 a 6|      Sensor Efecto Hall A3144                   | 1.5 U$D*
 1    |        Sensor Intensidad Luz Ultravioleta       | 6.5 U$D*
 1    |   Sensor Digital De Humedad Temperatura Htu21d  | 3.5 U$D*
 1    |        Sensor Presion Temperatura Bmp280        |   3 U$D*
 1    |           Conversor De Nivel 5v 3.3v 8ch        | 2.5 U$D*
 3    |         Sensor Optico Velocidad                 | 1.5 U$D*
 1    |       Display OLED                              | 7.5 U$D*
 1    |                  Bateria                        |  10 U$D*
 1    |       Modulo de carga                           | 1.5 U$D*
 1    |   Regulador a 5V                                | 1.8 U$D*
Total |                                                 |  60 U$D*
</div>

---

### *Planificacion y distribucion de tareas:

![Diagrama de bloques simplificado](images/Diagrama-de-Gantt-básico.png)
**Etapas:**
- Prueba de componentes: En esta etapa se van a realizar pruebas de todos los componentes, sensores, alimentacion, comunicacion wifi, etc. En este proceso se va a probar simulando condiciones reales de trabajo, ademas de comenzar a trabar y dominar el nuevo entorno de trabajo con el ESP32.
- Diagramas electronicos: En esta etapa se van a realizar diagramas detallados de todas las conexion del circuito, los cuales seran utiles a la hora de comenzar a trabar con todos los componentes conectados y trabando en conjunto.
- Placas: En este proceso se va a diseñar y crear el shield, en este mismo van a estar las salidas a los sensores, ademas de estar las resistencias para algunos de estos.
- Funcionamiento en conjunto y muestra por display: En esta etapa se van a poner sobre el programa "definitivo" todos los demas programas de prueba previamente creados, se van a adaptar para que puedan trabajar todos de manera uniforme y armoniosa, ademas se mostratan los datos sensados en el display.
- Implementacion de comunicacion: En esta etapa, ya con el programa "definitivo" terminado, se va a implementar la comunicacion mediante wifi para poder visualizar los datos ya sea desde una pagina web o una aplicacion movil.
- Carcasa (Diseño e impresion): En esta estapa se va a diseñar e imprimir en 3D la carcasa de la estacion metereologica, dentro de la misma estara toda la circuiteria y algunos de los sensores utilizados. La carcasa debera cumplir con cierta de resistencia y durabilidad para poder resistir las condiciones adversas de la interperie, ademas debera ser permeable a condiciones desfavorables para el funcionamiento de la estacion, como lo son suciedad, agua, hojas, etc.
- Pruebas: En esta etapa se prevee ya tener todo el proyecto casi terminado para poder realizar todas las pruebas necesarias para garantizar el optimo funcionamiento de la estacion.
- Resolucion de problemas: En esta etapa, en base a la pruebas realizadas en la etapa anterior, se realizaran todas la resoluciones de los problemas que seguramente surjan. En caso de que las problematicas sean pocas o nulas y exista tiempo de sobra, se tratara de trabajar en las implementaciones futuras pensadas.
- Presentacion y documentacion: En esta etapa, mas allá de que a lo largo de todo el proyecto se documenta, se hara enfasis en crear toda la documentacion del proyecto, incluyendo caracteristicas, problematicas, resoluciones, procesos, observacion y todo lo que se crea necesario de documentar. Una vez terminado el informe, se seguira con la presentacion del proyecto, que sera como un pequeño vistazo del informe pero de manera mas amena para garantizar el entendimiento del proyecto de manera considerada.
---

