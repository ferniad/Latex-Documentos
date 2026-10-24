##### Lineamientos para la elaboración y presentación de Subcomité de

##### EACP del SIN colombiano Protecciones

# Lineamientos para la elaboración y presentación de EACP del SIN

**colombiano**

|Revisión|Fecha|Descripción|
|---|---|---|
|1|2019-05-17|Este documento incluye la propuesta de los lineamientos a seguir en la elaboración y presentación de informes de Estudios de Ajuste y Coordinación de Protecciones.|
|2|2024-10-18|Este documento incluye la actualización de los lineamientos a seguir en la elaboración y presentación de informes de Estudios de Ajuste y Coordinación de Protecciones.|

## Subcomité de Protecciones

### CONTENIDO

**1 OBJETIVOS............................................................................................................. 5 2 ANTECEDENTES................................................................................................... 5**

**3 ALCANCE................................................................................................................6 4 MARCO REGULATORIO..................................................................................6**

**5 DEFINICIONES....................................................................................................... 7 6 ABREVIATURAS....................................................................................................8**

**7 CONSIDERACIONES.......................................................................................... 10 8 REUNIÓN DE INICIO.......................................................................................... 12**

*8.1 ÁREA DE IMPACTO DEL EACP...................................................................................................... 14*
*8.2 ACTA DE REUNIÓN DE INICIO......................................................................................................... 16*
**9 ELABORACIÓN DEL EACP.............................................................................. 17**

*9.1 CONSIDERACIONES GENERALES DEL DOCUMENTO...............................................................17*
*9.2 ANÁLISIS ELÉCTRICOS...................................................................................................................... 18*
Asignación de la generación en el sistema.............................................................................................19

Determinación de los escenarios operativos.........................................................................................19

*9.3 INSUMOS PARA ELABORAR EL EACP........................................................................................ 20*
Topología......................................................................................................................................................................20

Parámetros eléctricos..........................................................................................................................................20

Sistemas de protecciones.................................................................................................................................20

Diagramas unifilares.............................................................................................................................................. 21

Criterios de ajuste.................................................................................................................................................... 21

*9.4 SIMULACIONES PARA VERIFICAR EL DESEMPEÑO DE LAS PROTECCIONES...................23*
Definición de rutas de coordinación de protecciones.................................................................... 23

Verificaciones por equipo de potencia.....................................................................................................24

Resultados de validaciones vía simulación........................................................................................... 46

**10 ESTRUCTURA DEL DOCUMENTO DE ESTUDIO DE AJUSTE Y COORDINACIÓN DE PROTECCIONES.............................................................. 47**

*10.1 OBJETIVO............................................................................................................................................ 47*
*10.2 ALCANCE......................................................................................................................................... 47*
*10.3 DESCRIPCIÓN DEL PROYECTO O DE LA RED BAJO ESTUDIO......................................... 47*
*10.4 ETAPAS DEL PROYECTO (APLICA PARA ENTRADA DE NUEVOS PROYECTOS).......... 47*
*10.5 UBICACIÓN GEOGRÁFICA.......................................................................................................... 47*
*10.6 ÁREA DE INFLUENCIA.................................................................................................................. 48*
*10.7 PARÁMETROS TÉCNICOS............................................................................................................ 48*
*10.1 CONSIDERACIONES GENERALES..................................................................................................53*
*10.2 ESTUDIO DE FLUJO Y CORTOCIRCUITO..................................................................................53*
Análisis de flujo......................................................................................................................................................... 53

Resultados de cortocircuito............................................................................................................................. 53

*10.3 CARACTERÍSTICAS DE LOS SISTEMAS DE PROTECCIÓN.................................................... 54*
Características de los sistemas de protección a instalar...............................................................54

Características de los sistemas de protección existentes en el área de influencia ..... 55

*10.4 AJUSTES PROPUESTOS PARA LAS PROTECCIONES.............................................................55*
*10.5 CONCLUSIONES Y RECOMENDACIONES............................................................................... 56*
*10.6 REFERENCIAS................................................................................................................................ 56*
*10.7 ANEXOS REQUERIDOS................................................................................................................ 56*
Unifilares.......................................................................................................................................................................56

Criterios de ajuste de protecciones.............................................................................................................56

Memorias cálculo y ajuste de protecciones........................................................................................... 57

Verificación de saturación de los transformadores de corriente............................................. 57

Verificación del desempeño de los esquemas de protección................................................... 57

Anexos adicionales según necesidad........................................................................................................58

**ANEXO 1 (EXTERNO)................................................................................................59 ANEXO 2 (EXTERNO)...............................................................................................59**

# 1 Objetivos

-Describir el alcance de los temas a tratar en la reunión de inicio que se realiza previo a la elaboración de los Estudios de Ajuste y Coordinación de Protecciones (EACP) del Sistema Interconectado Nacional (SIN) colombiano para nuevos proyectos y red existente.

-Estandarizar las verificaciones y formatos de resultados que se deben presentar en los EACP de nuevos proyectos y red existente, según el equipo a conectar al SIN.

-Detallar las consideraciones mínimas y la estructura del documento del EACP.

# 2 Antecedentes

Entre el año 2013 y 2017 se identificó que aproximadamente el 50% de los Estudios de Ajuste y Coordinación de Protecciones (EACP) revisados por el Centro Nacional de Despacho (CND), requirieron más de tres versiones para lograr obtener una versión definitiva. Entre las causas principales se destaca el desconocimiento regulatorio, una incorrecta definición del área de influencia, información desactualizada o errónea en cuanto a esquemas de protecciones, parámetros de elementos y ajustes de protecciones del área de influencia, falta de unificación de criterios para realizar el ajuste y la coordinación de protecciones, falta de coherencia en la información presentada a lo largo del documento y omisión de información relevante para elaborar el estudio.

En el año 2019 se desarrolló la primera versión del documento de lineamientos para elaborar y presentar los EACP, el cual permitió unificar criterios, definir lineamientos, mejorar la calidad de los informes y disminuir los tiempos en la elaboración y revisión de dichos estudios. Asimismo, el Consejo Nacional de Operación (CNO), a través del Comité de Operación (CO) aprobó incluir este documento como un anexo del Acuerdo de Entrada de Nuevos Proyectos 1835 o aquel que lo sustituya o modifique.

En el año 2023, se identificó la necesidad de actualizar el anexo de lineamientos para elaborar los EACP, con el fin de integrar los requerimientos relacionados con los generadores conectados al SDL incluyendo los recursos de generación distribuidos (GD), equipos FACTS y generadores basados en inversores (IBG); además de resolver las causas identificadas de reprocesos en la elaboración y revisión de EACP y promover la mejora en la calidad de los mismos a través del uso efectivo de los lineamientos establecidos y la estandarización de los resultados presentados.

# 3 Alcance

Este documento presenta lineamientos, consideraciones y verificaciones generales a tener en cuenta antes, durante y después de la elaboración de un EACP. Los lineamientos definidos en este documento aplican a cualquier EACP que se realice para un nuevo proyecto o para red existente que se conecte al nivel de tensión 4 o superior y para sistemas de generación con capacidad mayor a 0.25 MW conectados a cualquier nivel de tensión. Lo anterior, dando cumplimiento a los requerimientos y definiciones establecidos en el Marco regulatorio.

# 4 Marco regulatorio

- La resolución CREG 025 de 1995 (CREG 025), o aquella que la modifique o sustituya, define requerimientos para la conexión de equipos que se conecten al STN. El anexo CC4 define los requisitos de protecciones.
- La resolución CREG 070 de 1998 (CREG 070), o aquella que la modifique o sustituya, define requerimientos para la conexión de equipos que se conecten al STR y SDL.
- La resolución CREG 060 de 2019 (CREG 060), o aquella que la modifique o la sustituya, define modificaciones y adiciones transitorias al Reglamento de Operación para permitir la conexión y operación de plantas solares fotovoltaicas y eólicas en el SIN y se dictan otras disposiciones.
- La resolución CREG 200 de 2019 (CREG 200), o aquella que la modifique o la sustituya, define un esquema para permitir que los generadores puedan compartir activos de conexión al SIN.
- La resolución CREG 148 de 2021 (CREG 148), o aquella que la modifique o la sustituya, adiciona transitoriamente un Capítulo al Anexo General del Reglamento de Distribución, adoptado mediante la Resolución CREG 070 de 1998. Este capítulo está relacionado con la integración de plantas eólicas y solares fotovoltaicas (SFV) en los Sistemas de Distribución Locales (SDL) y con capacidad efectiva neta o potencia máxima declarada igual o mayor a 5 MW.
- La resolución CREG 174 de 2021 (CREG 174), o aquella que la modifique o la sustituya, define aspectos operativos y comerciales para permitir la integración de la autogeneración a pequeña escala y de la generación distribuida al Sistema Interconectado Nacional (SIN). También se regulan aspectos de procedimiento de conexión de los autogeneradores a gran escala con potencia máxima declarada menor a 5 MW.

- La resolución CREG 101-011 de 2022 (CREG 101-111), o aquella que la modifique o la sustituya, adiciona transitoriamente un Capítulo al Anexo General del Reglamento de Distribución, adoptado mediante la Resolución CREG 070 de 1998, en aspectos técnicos relacionados con la integración de plantas eólicas y solares fotovoltaicas (SFV) en los Sistemas de Distribución Locales (SDL), y con capacidad efectiva neta o potencia máxima declarada igual o mayor a 1 MW y menor a 5 MW.
- Reglamento Técnico de Instalaciones Eléctrica (RETIE), establece las medidas para garantizar la seguridad de los seres vivos y prevenir prácticas que puedan inducir a error al usuario. Establece los requisitos y ensayos mínimos aplicables a los equipos y productos, fijando los parámetros mínimos de calidad, desempeño y seguridad. Adicionalmente, contiene el procedimiento de evaluación de la conformidad normativa.
- El Acuerdo CNO 1835, o aquel que lo modifique o la sustituya, define los requisitos y el procedimiento para la puesta en operación de proyectos de transmisión que incluyan activos de uso del Sistema de Transmisión Nacional (STN), del Sistema de Transmisión Regional (STR), de usuarios conectados directamente al STN, al STR y de recursos de generación.
- El Acuerdo CNO 1862, o aquel que lo modifique o la sustituya, define los requisitos de protecciones para la conexión de sistemas de generación en el SIN colombiano.
# 5 Definiciones

**1** **Frontera compartida (FC) :** Para sistemas de generación, es el definido en la resolución CREG 200 del 2019, o aquella que la sustituya o modifique.

**Generación distribuida²:** Es la actividad de generar energía eléctrica con una planta con capacidad instalada o nominal de generación menor a 1 MW, y que se encuentra instalada cerca de los centros de consumo, conectada al Sistema de Distribución Local (SDL).

**Promotor:** Persona natural o jurídica que desarrolla un proyecto de transmisión, subtransmisión, generación o autogeneración conectado al SIN.

**Punto de conexión (PC):** El definido en la resolución CREG 038 del 2014, o aquella que la sustituya o modifique.

1 Es un PC al SIN donde se conectan varias plantas o unidades de generación individuales que compartan activos de conexión. CREG 200 de 2019.

Fuente: CREG 174 de 2014, Artículo 3.

|||||Lineamientos para la elaboración y presentación de EACP del SIN colombiano||Subcomité de Protecciones||
|---|---|---|---|---|---|---|---|
|6 ANSI: BT: CD: CND: CNO: 3|Cogenerador: FACTS: 57,5 kV. 220 kV.|Generador Distribuido: generación distribuida. Autogenerador: autogeneración. Cogeneración. Nivel 1 de tensión: Nivel 2 de tensión: Nivel 3 de tensión: Nivel 4 de tensión: menor a 57,5 kV. Abreviaturas|capacidad de transferencia de potencia Sistema de Distribución Local (SDL): Sistema de Transmisión Regional (STR): tensión menor a 220 kV y que no hacen parte del SDL. Sistema de Transmisión Nacional (STN): tensión igual o superior a 220 kV. American National Standards Institute Bahía de transformador Comparación Direccional Centro Nacional de Despacho Consejo Nacional de Operación|3. Sistemas con tensión nominal menor a 1 kV. Transactions on Power Delivery, vol. 12, no. 4, pp. 1848-1853, Oct. 1997.|Usuario que realiza la actividad de autogeneración. El usuario puede ser o no ser propietario de los activos de generación para realizar la actividad de Es aquella persona natural o jurídica que produce energía utilizando un proceso de Cogeneración, y que puede o no, ser el propietario del sistema de Sistemas de transmisión en corriente alterna que incorporan electrónica potencia y otros controladores estáticos para mejorar la flexibilidad del sistema y la Fuente: "Proposed terms and definitions for flexible AC transmission system (FACTS)," in IEEE|Empresa de Servicios Públicos (ESP) que realiza la actividad de Sistemas con tensión nominal mayor o igual a 1 kV y menor de 30 kV. Sistemas con tensión nominal mayor o igual a 30 kV y menor de Sistemas con tensión nominal mayor o igual a 57,5 kV y menor a Compuesto por elementos que operan con tensión Compuesto por elementos que operan con Compuesto por elementos que operan con|de 8|

**CREG:** Comisión de Regulación de Energía y Gas

**DDT:** Disparo directo Transferido

**EACP:** Estudio de Ajuste y Coordinación de Protecciones

**EI:** Extremely Inverse (Extremadamente Inversa)

**ESP:** Esquemas Suplementarios de Protecciones

**FC:** Frontera compartida

**FIDVR:** Fault-Induced Delayed Voltage Recovery (Fenómeno de Recuperación Lenta Inducida de Tensión)

**FPO:** Fecha de Puesta en Operación

**FRT:** Fault Ride Through

**GD:** Generación distribuida

**HVRT:** High Voltage Ride Through

**IBG:** Generación Basada en Inversores

**IEEE:** Institute of Electrical and Electronic Engineers

**In:** Corriente Nominal

**IPOEMP:** Informe de Planeamiento Operativo Eléctrico de Mediano Plazo

**IPB:** Inter-Phase Balancing

**LOR:** Low Overcurrent Ride-Through

**LVRT:** Low Voltage Ride Through

**MB:** Megabyte

**NI:** Normal Inverse (Normalmente Inversa)

**ONAF:** Oil Natural Air Forced (Aceite natural, aire forzado)

**ONAN:** Oil Natural Air Natural (Aceite natural, aire natural)

**OR:** Operador de Red

**PC:** Punto de conexión

**PCH:** Pequeña Central Hidroeléctrica

**P.U.:** Por Unidad **ROCOF:** Rate Of Change Of Frequency (Tasa de cambio de la frecuencia) **SDL:** Sistema de Distribución Local **SIR:** Source Impedance Ratio **SIN:** Sistema Interconectado Nacional

**SSAA:** Servicios Auxiliares

**SSSC:** Static Synchronous Series Compensator

**STATCOM:** Static Synchronous Compensator

**STN:** Sistema de Transmisión Nacional

**STR:** Sistema de Transmisión Regional

**SVC:** Static VAR Compensator

**TC:** Transformador de corriente

**TP:** Transformador de potencial (transformador de tensión)

**UPME:** Unidad de Planeación Minero-Energética

**VI:** Very Inverse (Muy Inversa)

**VRT:** Voltage Ride Through

# 7 Consideraciones

A continuación, presentamos las consideraciones para tener en cuenta en la implementación de las recomendaciones de este documento:

1. Si alguna de las partes involucradas identifica otros aspectos necesarios que no han sido incorporados en este documento, que comprometan la operación segura y confiable del SIN, estos se podrán solicitar en la primera versión del EACP siempre y cuando se presente la debida justificación técnica.
2. Los criterios de ajuste de protecciones aplicables para equipos de generación y equipos de potencia que se conecten al nivel de tensión 4 o superior, estarán basados en los definidos en las guías de ajuste y coordinación de protecciones⁴. Criterios diferentes a los de las guías se deberán consignar en el documento.
3. Las recomendaciones de esquemas para los sistemas de protección de equipos de generación y equipos de potencia que se conecten al nivel de tensión 4 o superior, serán los definidos en la regulación vigente, considerando los recomendados en el documento de Esquemas Normalizados de Protecciones
5 y lo especificado en los pliegos de la convocatoria UPME.

4 “Guías de ajuste y coordinación de protecciones”, en su última versión disponible. 5 “Esquemas normalizados de protección recomendados para nuevos proyectos en el SIN colombiano”, CNO, en su última versión disponible.

4. Para el caso de los generadores conectados a los Sistemas de Distribución Local (SDL), considerar la posible presencia de flujos bidireccionales por otros generadores en la zona de influencia.
5. Para todos los proyectos de generación y equipos de potencia que se conecten al nivel de tensión 4 o superior, se debe calcular, evaluar y recomendar los ajustes de las protecciones del nuevo equipo, del punto de conexión, y para el caso de proyectos de generación, los ajustes del interior del sistema de generación. Además, se debe revisar la integralidad y selectividad de los ajustes de protección de la red existente en la zona de influencia y garantizar que la conexión del nuevo proyecto mantenga o mejore la coordinación de protecciones de la zona de influencia, bajo todos los escenarios de operación evaluados.
6. Para el caso de los proyectos de generadores conectados al SDL, el Operador de Red (OR), encargado de otorgar el punto de conexión, debe suministrar al promotor información relacionada con los criterios y ajustes de protecciones de la red existente del OR, la topología de la red, los parámetros técnicos de los equipos, los equivalentes de red, las contingencias y/o reconfiguraciones topológicas que debe ser evaluadas en el EACP, los proyectos a considerar en el área de influencia y demás información requerida como insumo para la elaboración del EACP.
7. Para el caso de los nuevos generadores basados en inversores, los EACP deben considerar en las simulaciones el modelo del inversor suministrado por el fabricante del equipo. Este modelo debe tener en cuenta el impacto del control en el aporte de corriente de cortocircuito del generador (en magnitud y ángulo), siempre y cuando el desempeño del modelo cumpla con lo especificado en la regulación vigente. En caso contrario, se deberá considerar un modelo genérico que cumpla con lo especificado en la regulación vigente.
8. Para el caso de los FACTS, los EACP deben considerar en las simulaciones el modelo suministrado por el fabricante, siempre y cuando, este corresponda con su promesa de valor y el comportamiento especificado para el equipo en la respectiva convocatoria.

##### 8 Reunión de inicio⁶

Previo a la elaboración de cualquier EACP, es necesario que el promotor del proyecto coordine una reunión de inicio, de carácter virtual, en la cual debe incluir al CND y a todos los agentes involucrados o impactados con el proyecto. El promotor del proyecto debe enviar la presentación a utilizar en la citación de la reunión con el fin de que los asistentes puedan revisarla y hacer recomendaciones que puedan ser corregidas para el día de la reunión. Además, <u>es requerido que a esta reunión asista personal técnico de protecciones</u> en representación de cada una de las partes involucradas. En la reunión de inicio de EACP se deberán tratar o desarrollar los siguientes ítems, teniendo en cuenta que el promotor del proyecto deberá llevar una propuesta consolidada de cada uno de estos puntos:

- Definir el área de influencia o de impacto del proyecto, la cual será considerada dentro de los análisis a realizar en el EACP. En el ítem 8.1 se describen las consideraciones para la definición del área de influencia.
- Presentar los parámetros técnicos de los nuevos equipos que se emplearán para elaborar el EACP. Para la red existente se tomarán los parámetros declarados en la base de datos de parámetros técnicos PARATEC⁷ y en caso de encontrar discrepancias respecto a los datos recopilados por el proyecto, se deberán presentar en la reunión⁸.
- Informar herramienta de simulación para elaborar los estudios de protecciones y fecha de la base de datos utilizada como referencia.
- Presentar diagrama unifilar de protecciones de los equipos de potencia nuevos y los modificados por el proyecto, diagramas o planos eléctricos detallados de las subestaciones nuevas e intervenidas por el proyecto, además de presentar la localización eléctrica del mismo dentro del área de influencia. En caso de que el proyecto se vaya a desarrollar por etapas, se debe presentar el diagrama unifilar de protecciones detallado de cada una de estas.
- Presentar las características de los sistemas de control y protección a implementar en el nuevo proyecto y su área de influencia, en donde se debe incluir, equipos de medida con la relación utilizada y clase, la referencia de las protecciones a utilizar, las funciones de protección disponibles en las mismas y los esquemas de teleprotección a considerar con detalle de su tecnología de
6 Para los proyectos dentro del alcance de la resolución CREG 174 de 2021 o aquella que la modifique o sustituya, se podrá considerar un procedimiento simplificado de acuerdo con lo establecido en dicha resolución. 7 El portal PARATEC se pueden consultar en la página web del CND, a través del perfil privado. 8 Para el caso de proyectos conectados al SDL, los parámetros de los equipos del área de influencia serán suministrados por el operador de red que otorga el punto de conexión.

comunicación. Para el caso de convocatorias UPME se debe verificar que los esquemas de protecciones consideren los requerimientos de los pliegos.

- En caso de que el proyecto se vaya a desarrollar por etapas, indicar detalladamente las etapas de puesta en servicio definidas, incluyendo la fecha estimada de inicio de cada una. Si el intervalo entre las FPO de las etapas del proyecto es superior a 6 meses, se recomienda realizar una reunión de inicio específica para cada etapa.
- Describir los proyectos que entrarán en operación antes o simultáneamente con el proyecto objeto de la reunión, indicando claramente la etapa del proyecto en la que estarían entrando y su impacto topológico.
- Describir posibles reconfiguraciones, mantenimientos mayores o indisponibilidades de protecciones diferenciales de barra que se deban ejecutar en el área de influencia para la implementación y puesta en servicio del nuevo proyecto.
- Analizar las topologías operativas y condiciones especiales que deben ser tenidas en cuenta en la elaboración del EACP. Definir escenarios de generación/demanda que deben ser evaluados en el EACP, según el tipo de proyecto y punto de conexión (PC). También, describir los transformadores de puesta a tierra instalados en la red.
- Presentar las rutas de coordinación de protecciones en red completa y red N-1 de líneas, transformadores y generadores.
- En caso de identificarse necesario usar criterios técnicos particulares para el ajuste y verificación de coordinación de las protecciones del proyecto y su área de influencia, presentar los criterios con su respectiva justificación.
- Definir requisitos de solicitud de información adicional requerida para elaborar el EACP.
- Identificar los esquemas suplementarios de protecciones (ESP)
9 existentes en el área de influencia del proyecto y definir si se deben incluir en los análisis de protecciones. En caso de ser necesario, presentar el detalle de operación de cada uno de ellos.

- En zonas con alta penetración de generación conectada al SDL, se recomienda validar el impacto de fallas críticas a nivel de transmisión sobre las funciones de tensión en el punto de conexión del nuevo generador que se conectará al SDL. En caso de requerirse, esta contingencia será definida en la reunión de inicio del proyecto.
Los ESP se pueden consultar en la página web del XM, a través del portal privado*.*

Por cada reunión de inicio de EACP, se debe elaborar un acta por parte del promotor del proyecto con las principales consideraciones, recomendaciones y compromisos. En el ítem 8.2 se presenta formato del acta.

En caso de identificar verificaciones o solicitudes adicionales al proyecto que no hayan sido acordadas en la reunión de inicio, se deberá socializar en una reunión con el CND y con los agentes involucrados, siempre que las verificaciones adicionales correspondan al alcance del proyecto y estén debidamente justificadas. En caso de que los hallazgos o verificaciones adicionales sean causadas por situaciones preexistentes en la red, estas deberán ser solucionadas en coordinación entre el OR y el promotor del proyecto.

## 8.1 Área de impacto del EACP

Para los tipos de proyectos definidos en el alcance de este documento, se requiere acordar en la reunión de inicio la topología y el segmento de red eléctrica a considerar para cada etapa del EACP. Para la selección del área de influencia, se tomarán como base de referencia dos barras adyacentes a la conexión del nuevo proyecto. Para cada proyecto, se debe analizar y definir si es necesario expandir o contraer esta área de influencia.

Ampliando el alcance al párrafo anterior, en caso de que se modifiquen los ajustes de las protecciones de los elementos ubicados en las fronteras del área de influencia por parte del promotor, por riesgos de descoordinación o mejora de tiempos de despeje de fallas, se deberán realizar las respectivas verificaciones para comprobar que los ajustes recomendados para dichas protecciones coordinen adecuadamente con las protecciones de los elementos adyacentes.

Para la definición y modelado del área de influencia en la herramienta de simulación, se deben tener en cuenta los siguientes elementos:

- Todo generador ubicado al interior y en las cercanías de la red bajo estudio, se debe modelar con su transformador elevador y punto de sincronización a la red. Para transformadores con conexión *“Y-∆*”, con “Y” aterrizada en el lado de alta, según el punto de sincronización del generador, se debe verificar si el generador fuera de servicio mantiene o no su transformador conectado al sistema. En caso de considerar el transformador conectado al sistema, se debe tener en cuenta el aporte de corriente de secuencia cero de este equipo durante fallas asimétricas, con y sin generador en servicio.
- Modelar, considerando el grupo de conexión, impedancia de puesta a tierra y todos los devanados, los transformadores conectados al STN, STR, SDL y los aportes de la generación distribuida desde la red del SDL.
- Modelar los transformadores de puesta a tierra ubicados al interior y en las cercanías de la red bajo estudio.
- Modelar el devanado terciario de los transformadores y autotransformadores con tres devanados.

- Modelar elementos de compensación fijos y variables (FACTS), teniendo en cuenta sus respectivos controles.
- Modelar esquemas suplementarios de protecciones (ESP) existentes.
- Para el caso de proyectos de generadores conectados al SDL: o Modelar la red del SDL de la zona de influencia del proyecto, incluyendo equivalentes en las barras de conexión STR/SDL o interconexiones del SDL relevantes que puedan afectar el nivel de cortocircuito en el punto de conexión del proyecto. o Integrar los generadores en el modelo eléctrico del SDL e incluir los umbrales de las funciones de tensión con el fin de validar en las simulaciones posibles salidas no selectivas de los generadores. o Considerar si la conexión del proyecto al SDL es en T o en barra, de acuerdo con la topología presentada en la Figura 1:
- Cuando la conexión es directa a la barra, se deben modelar todas las bahías conectadas a esta barra.
- Cuando la red es radial, se debe modelar el ramal propio y ramales adyacentes y/o paralelos que impacten.
- Cuando la red es anillada, se deben modelar todos los elementos del anillo, considerando las condiciones operativas de esta porción de la red.

##### Conexión en T Conexión a barra

*Figura 1 Diagrama unifilar para conexión en T y en barra de generaadores conectados al SDL*

## 8.2 Acta de reunión de inicio

A continuación, se presenta un formato sugerido para la realización del acta de reunión de inicio que deberá ser elaborada por el promotor del proyecto y enviada a los participantes. Adicionalmente, en el anexo 1 se presenta la plantilla editable de este formato sugerido.

**PROYECTO:**

**OBJETIVO:**

**FECHA:**

**PARTICIPANTES:**

**Nombre Empresa**

**DESARROLLO:**

**Ítem Observaciones** Describir área de influencia del proyecto Presentar parámetros técnicos del nuevo proyecto Describir etapas del proyecto Enumerar proyectos adicionales o simultáneos a considerar Indicar escenarios de generación/demanda seleccionados

||Lineamientos para la elaboración y presentación de EACP del SIN colombiano||Subcomité de Protecciones|||
|---|---|---|---|---|---|
||El promotor deberá indicar si existen topologías operativas y/o condiciones especiales recurrentes en el área, además de posibles reconfiguraciones, mantenimientos mayores, indisponibilidad de equipos de potencia o sistemas de protección. Enumerar las rutas de coordinación de protecciones definidas para red completa y para la condición de N-1 Describir esquemas de protección propuestos y existentes Definir si hay impactos sobre los ESP en el área de influencia|||||
||Describir estudios adicionales requeridos Indicar si se requiere información técnica adicional Indicar si se requieren criterios técnicos particulares COMPROMISOS:|||||
||Compromiso Responsable||Fecha|||

# 9 Elaboración del EACP

Se deben realizar análisis eléctricos previos para sintonizar los casos de simulación en el modelo eléctrico. Para ellos, se requiere contar con insumos como la topología de la red, los parámetros eléctricos, los esquemas de protecciones, los diagramas unifilares, los criterios de ajuste, entre otros. Estos elementos permiten verificar la coordinación de los ajustes de protección ante diferentes escenarios y tipos de fallas.

En este ítem se detallan y estandarizan las consideraciones generales, los análisis eléctricos, los insumos, las verificaciones, las simulaciones, la presentación de resultados y ajustes para cada equipo de potencia al cual se le realizan las respectivas validaciones.

## 9.1 Consideraciones generales del documento

Se debe verificar que los documentos enviados no tengan restricciones de lectura ni requieran solicitud de permisos para leerlos. Las gráficas presentadas en el documento deben tener calidad suficiente para poder identificar todos los elementos dentro de dicha gráfica, incluyendo letras, tags, ejes, leyendas, curvas, entre otros. Para todos los valores numéricos presentados debe ser claro en qué unidades se encuentran reportados dichos valores, teniendo en cuenta que para los elementos reportados en valores por unidad (p.u.) o porcentaje, se debe indicar la base considerada. De igual forma, tanto tablas como gráficas deben estar debidamente rotuladas y referenciadas dentro del documento.

Se debe verificar la redacción y la ortografía en cada una de las secciones del documento, además de la integralidad de este, asegurando siempre que la información presentada en cada una de las secciones se mantenga coherente a lo largo del documento y que no se presente información contradictoria o diferente para un mismo parámetro en diferentes secciones del documento. Para el caso de documentos con anexos, el documento principal debe incluir en su tabla de contenido el título de cada uno de los

anexos y su versión aplicable, de tal manera que desde la tabla de contenidos sea posible identificar el tema tratado en cada uno de estos y la versión que aplica de cada Anexo para el estudio respectivo.

Se recomienda que, al crearse anexos o documentos de estudios con gran cantidad de imágenes, éstas se inserten en el documento en un formato que maximice su legibilidad y reduzca el peso de los documentos. Se debe tener en cuenta que en general, en las plataformas para cargas de archivos aplicables, los documentos o anexos no deben exceder los 30MB.

## 9.2 Análisis eléctricos

A partir de los resultados de flujos de carga y análisis de cortocircuito del Informe de Planeamiento Operativo Eléctrico de Mediano Plazo (IPOEMP), se deben definir los escenarios de simulación y establecer las rutas para la verificación de la coordinación de protecciones mediante simulación en el modelo eléctrico del sistema. Estos escenarios base o de generación deben respetar los límites operativos establecidos por la regulación vigente.

Para elaborar un EACP es fundamental contar con un modelado preciso de la red eléctrica o base de datos sintonizada. Esta base de datos deberá reflejar los valores reales de flujos de potencia y corrientes de cortocircuito del SIN. Como referencia el CND dispone, para los agentes del sistema, un modelo de la red eléctrica en el software PowerFactory¹⁰, a partir del nivel de tensión 4, con los parámetros declarados por los agentes en PARATEC al momento de su publicación. Es responsabilidad del promotor del proyecto validar los parámetros de los elementos a energizar y del área de influencia. Para niveles inferiores de tensión se debe coordinar con el OR el suministro de la información técnica correspondiente. El modelo eléctrico del SIN y el IPOEMP se actualizan trimestralmente y están disponibles para su descarga en el Portal WEB de XM¹¹.

Los análisis de los flujos de carga y cortocircuito permiten determinar los escenarios bajo los cuales se elaborará el EACP, así como los niveles mínimos y máximos de cortocircuito trifásico, monofásico, bifásico y bifásico a tierra. Estos niveles se utilizarán para evaluar el desempeño de las diferentes funciones de protección. Por lo general, para elaborar los EACP se consideran escenarios de demanda mínima, media y máxima. Dependiendo del tipo de proyecto, podrán requerirse otros escenarios de simulaciones que serán acordados en la reunión de inicio.

Es responsabilidad del promotor del proyecto acondicionar y verificar el modelo eléctrico de acuerdo con la topología de la red en el momento de la entrada del proyecto, considerando, el área de influencia definida y recomendaciones eléctricas del IPOEMP.

10 Para los EACP elaborados en otro software de simulación, se requiere consultar los valores de flujo de carga y cortocircuito de referencia para sintonizar las simulaciones, estos valores pueden ser consultados al CND o en los informes de la UPME.

La BD y el IPOEMP se pueden consultar en la página web del CND, a través del perfil privado.

Además, cuando los EACP sean elaborados por empresas externas que no son agentes operadores del SIN, es responsabilidad del promotor garantizar la confidencialidad en el suministro de información sobre el modelo eléctrico a terceros.

### Asignación de la generación en el sistema

Las unidades de generación se despachan de tal forma que se cumplan con los criterios de operación establecidos en la resolución CREG 025 de 1995. Además, se selecciona el nodo Slack de tal forma que sea una unidad grande (Preferiblemente mayor o igual a 100 MVA) y que, eléctricamente se encuentre por fuera del área de análisis (idealmente, lo más alejada posible).

### Determinación de los escenarios operativos

Para el caso de generación síncrona se deben realizar simulaciones en dos escenarios: uno con demanda mínima – generación mínima, y otro con demanda máxima – generación máxima. En ambos casos, se debe incluir en el despacho las centrales con unidades síncronas y eólicas.

Para la generación basada en inversores se deben tener en cuenta también escenarios de demanda media – generación máxima, incluyendo en el despacho las centrales solares. En este último caso, si se presenta modificaciones en los ajustes de la red existente en escenario de media, también se deberá validar coordinación en demanda máxima y mínima, sin recurso de generación solar. En los escenarios indicados, generalmente se considera y valida:

- El escenario de mínima demanda, en el que se busca disminuir los flujos por los circuitos a los mínimos probables y se calculan los valores de los cortocircuitos en las barras.
- El escenario de media demanda, en el cual se busca incrementar los flujos por los circuitos a los máximos probables en demanda media al despachar al máximo la generación solar en el área y se calculan los valores de los cortocircuitos en las barras.
- El escenario de máxima demanda, en el cual se busca incrementar los flujos por los circuitos a los máximos probables y se calculan los valores de los cortocircuitos en las barras.
- En los escenarios mencionados anteriormente, se analiza cómo la generación cercana al área en estudio (incluyendo las PCH e IBG) modifica el comportamiento de los flujos y los cortocircuitos, de tal manera que puedan afectar el desempeño de las protecciones.
- Para los cortocircuitos desbalanceados, se deben modelar los transformadores de interconexión entre STR/SDL o STN/SDL de distribución en el área de influencia del EACP que no se encuentren previamente modelados en la base de datos. Esto incluye todos sus devanados, su grupo de conexión, aterrizamiento y, de ser el caso

su impedancia de puesta a tierra. Para el caso de líneas que comparten estructuras, se deben modelar los respectivos acoples mutuos e informarlos en el documento.

## 9.3 Insumos para elaborar el EACP

La información oficial o insumos para elaborar los EACP será la disponible en las bases de datos del CND. En caso de información adicional, se deberá solicitar el detalle requerido a los agentes de la zona de influencia mediante comunicación escrita.

### Topología

En el modelo eléctrico se deben incorporar los nuevos elementos del proyecto, incluyendo los equipos de potencia y las recomendaciones acordadas en la reunión de inicio. Tener en cuenta que existen porciones de red en el SIN que por restricciones operativas requieren que algunos elementos operen normalmente abiertos y para su cierre se hace necesaria la apertura de otro(s) elemento(s) con el fin de evitar sobrecargas, sobrepasar el nivel de cortocircuito de la subestación, diferencias en los grupos horarios de transformadores, entre otras restricciones. En estos casos, se deben considerar al menos dos topologías de operación. Las topologías adicionales analizadas deben obedecer a condiciones operativas reales del sistema.

### Parámetros eléctricos

Cuando se utilice el modelo eléctrico que está disponible para consulta en el sitio web del CND (DIgSILENT- Power Factory), se debe indicar la fecha de la base de datos utilizada para las simulaciones. Para este caso no será necesario reportar en el informe los parámetros técnicos de la red existente, no obstante, el promotor debe verificar con lo reportado en PARATEC. Para este caso se deben modelar los elementos eléctricos que no se encuentran en la base de datos, considerando las recomendaciones indicadas en la reunión de inicio y lo indicado en el numeral 8.1.

Si no se utiliza el modelo eléctrico proporcionado por el CND, se deben presentar los parámetros técnicos de todos los equipos existentes en el área de influencia.

Para los nuevos proyectos, el EACP debe ser elaborado con los parámetros técnicos preliminares declarados por el promotor, obtenidos mediante medición, simulación y/o placa, dependiendo del equipo. Es crucial señalar que, si previo a la energización del nuevo proyecto se identifican diferencias entre los parámetros preliminares y los definitivos, con impactos o modificaciones en los ajustes de protecciones recomendados previamente en el EACP, es responsabilidad del promotor y/o operador del activo actualizar el EACP.

### Sistemas de protecciones

Los sistemas de protección de los nuevos equipos, incluyendo, relés, transformadores de Potencial (TP), transformadores de corriente (TC), interruptores y esquemas de

|||Lineamientos para la elaboración y presentación de EACP del SIN colombiano|Subcomité de Protecciones|
|---|---|---|---|
||los equipos que se instalarán en sitio. Para los sistemas de protección existentes|comunicación, deben ser tenidos en cuenta con las referencias y características reales de Referencia de relés, versión de firmware (en donde sea posible), funciones de protección disponibles, ajustes implementados, TP, TC, esquemas de teleprotección y comunicación, entre otros, se debe tomar la información de protecciones oficial disponible en la base de datos de protecciones (StationWare). Solo en casos excepcionales, como traslapes de proyectos a nivel de su FPO, se podrán usar los ajustes recomendados en otros EACP simultáneos con el objetivo de dar claridad o mantener la coherencia de los ajustes recomendados. Para el caso de proyectos en el SDL los ajustes de protecciones deben ser suministrados por el OR que otorga el punto de conexión.|de la zona de influencia se debe indicar:|
||Diagramas unifilares nuevo proyecto, en los que se identifiquen|Se deben considerar los diagramas unifilares de los sistemas de protección de detalle del disponibles, la ubicación de los interruptores, los TP y TC, la conexión de los núcleos secundarios de los TP y TC hacia los relés, incluyendo sus relaciones y las lógicas de los esquemas de comunicación. Para transformadores nuevos o con modificaciones, de ser posible, incluir diagrama donde se muestre tipo de conexión, nivel de tensión, potencia nominal, impedancia de cortocircuito, detalles del devanado de compensación (si aplica), entre otros. Además, se debe presentar un diagrama unifilar en donde se muestre la ubicación eléctrica del proyecto dentro del área de influencia.|los relés, las funciones de protección|
||Criterios de ajuste|Los criterios de ajustes de protecciones a considerar son los descritos en las guías de ajuste y coordinación de protecciones del CNO. Si se tienen en cuenta criterios diferentes o consideraciones particulares, estos se deberán socializar en la reunión de inicio e incluir en el EACP. Sin embargo, si se utilizan los criterios establecidos en las guías del CNO, no será necesario incluirlos nuevamente en el EACP, indicando la versión de la guía utilizada.||
||Configuración del simulador|||
|•|cuenta: Líneas:|Para la verificación de los ajustes de las protecciones, se debe contar con un software de simulación que tenga librerías de relés con comportamientos lo más cercano posible a su contraparte real. El software debe permitir realizar análisis confiables de desempeño de los relés de protección mediante simulaciones de flujo de carga, cortocircuito y en caso de requerirse, mediante simulaciones de estabilidad transitoria. Para el modelado de los diferentes elementos del área de influencia se debe tener en Para el caso de líneas paralelas o que comparten estructuras con otras líneas, considerar las impedancias de acoplamiento mutuo entre cada una de ellas. En el|21|

caso de líneas con conductor aislado, como es las líneas subterráneas, se debe considerar el modelado detallado del cable.

- <u>Transformadores:</u> Es fundamental modelar todos los devanados del transformador, el grupo de conexión y el aterrizamiento del transformador, teniendo en cuenta las impedancias de puesta a tierra en caso de contar con alguna. Considerar los valores de impedancia de secuencia positiva y secuencia cero para cada uno de los devanados, teniendo en cuenta la base de potencia en la que deben ser ingresadas estas impedancias dependiendo del software de simulación utilizado.
- <u>Generadores síncronos:</u> Modelo detallado de la unidad de generación, asegurando que los parámetros eléctricos de las máquinas sean equivalentes a los reportados por el fabricante del equipo en su respectiva hoja de datos, utilizando la base o las unidades definidas por el software de simulación. Además, considerar la topología y características de la puesta a tierra de la planta generadora reportada en los diagramas unifilares. Para el caso de generadores con frontera compartida, se deben modelar todos los sistemas de generación y elementos conectados al interior de la frontera compartida. Para el caso de simulaciones dinámicas se debe considerar el modelo de los controles de los generadores.
- <u>Generadores basados en inversores:</u> Se debe tener en cuenta que la respuesta de los inversores en cuanto a la entrega de potencia activa, reactiva, tensión, corriente de secuencia positiva y negativa, entre otras, en simulaciones de flujo de carga y cortocircuito, sea coherente con las características especificadas por el fabricante. De igual forma, se debe verificar que el control de los IBG aporte corrientes de cortocircuito según la regulación vigente. Para nuevos proyectos, se deben modelar las líneas colectoras, transformadores de potencia y transformadores Zig-Zag dentro del parque. Para el caso de generadores con frontera compartida, se deben modelar todos los sistemas de generación y elementos conectados al interior de la frontera compartida. Para el caso de generadores IBG conectados en la zona de influencia modelar un equivalente de la planta y considerar aporte de corrientes de cortocircuito según la regulación vigente.
- <u>Condensadores:</u> Se deben modelar cada una de las etapas del banco de condensadores considerando sus características y el tipo de conexión. Los parámetros deben ser ingresados de acuerdo con lo definido por el software de simulación utilizado.
- <u>D-FACTS:</u> Se debe integrar el control detallado del equipo y verificar que su funcionamiento sea coherente con la promesa de valor, las especificaciones del fabricante y los parámetros que serán declarados en la puesta en operación. El modelo debe permitir la ejecución de simulaciones balanceadas y desbalanceadas en estado estacionario y RMS.
Para las simulaciones de cortocircuito, dado el efecto del flujo de carga en variables como tensión y corriente, que influyen en la operación de diversas funciones de protección, se

|||Lineamientos para la elaboración y presentación de EACP del SIN colombiano||Subcomité de Protecciones||
|---|---|---|---|---|---|
|RMS. En|lógicas, modo 9.4|debe usar el método de superposición (completo) que considera voltajes pre falla según el flujo de carga y las corrientes de cortocircuito en combinación con las corrientes del flujo de carga inicial. Para el caso de análisis de estabilidad se deben realizar simulaciones En cuanto al modelo del relé, se deberá verificar que los rangos de ajuste, la resolución de ajuste (paso), el valor en el que comienzan y se aplanan las curvas de sobrecorriente, de operación, características del relé, coincidan con lo indicado en el manual del fabricante. En caso de que no se tenga adecuada certeza de la calidad del modelo del relé en el simulador utilizado, se recomienda generar archivos COMTRADE para diferentes tipos de falla y verificar la correcta actuación de los relés mediante pruebas en sitio. Simulaciones para verificar el desempeño de las protecciones protecciones para todos los escenarios de simulación definidos en la reunión de inicio, tanto para red completa como para las condiciones N-1 mediante las rutas de coordinación previamente definidas, que nuevo proyecto coordinen adecuadamente con las protecciones de la red existente, para diferentes tipos de fallas, topologías y escenarios. Para el caso de bahías con relés que cuenten con diferentes características de operación, como es el caso de relés de diferente fabricante, se deben realizar las respectivas validaciones considerando ambos relés. Definición de rutas de coordinación de protecciones|modo de polarización y selección de fases, entre otras cada etapa del proyecto se debe realizar la evaluación del desempeño de las|acordadas. Además,|validar las protecciones del|
|12|sistemas enmallados direcciones. direccionales.|Para verificar el adecuado desempeño de los sistemas estudio, se deben definir e indicar en el EACP las rutas de coordinación que permitan verificar la correcta coordinación y operación selectiva de las protecciones del proyecto y su área de influencia. Las rutas definidas deben validar todas las posibles combinaciones de operación de protección principal del elemento fallado protecciones de los elementos adyacentes, para cada uno de los elementos del área de influencia. En la Figura 2, se presenta un ejemplo de rutas para validar la coordinación de protecciones ante falla en la línea S/E_A-S/E_B¹² las rutas de coordinación Para el ejemplo presentado se considera que todos los elementos de protección son|deben ser|de protecciones del área de y el. Se debe tener en cuenta que, para evaluadas|respaldo de las en ambas 23|

||||Lineamientos para la elaboración y presentación de EACP del SIN colombiano||Subcomité de Protecciones|
|---|---|---|---|---|---|
||||Verificaciones por equipo de potencia|Figura 2 Diagrama unifilar con rutas de coordinación de protecciones.||
|los de fases.|Líneas de transmisión:|los respaldos remotos adyacentes.||A continuación, se describen para cada equipo de potencia los tipos de verificaciones que se deben de realizar e incluir en el EACP. El objetivo es identificar, mediante simulación, el máximo valor de resistencia de falla que los sistemas de protección están en capacidad de detectar y confirmar la selectividad entre las protecciones del elemento protegido y Para verificar la coordinación entre funciones de sobrecorriente, se deben presentar las curvas correspondientes a diferentes fallas en el sistema e indicar el valor de corriente de falla y el tiempo de operación de la protección, discriminando entre los relés de tierra y||
|problemas esquemas|de alcance o coordinación.|o lógicas|La Tabla 1 presenta las verificaciones de coordinación de protecciones para líneas. coordinación de presentar diagramas de coordinación tiempo – distancia.|En caso de identificar alguna limitación para detectar fallas con y sin impedancia y/o protecciones, se podrán considerando criterios especiales, la apertura secuencial de interruptores y/o proponer asistidas de protección para dar solución a estos En caso de que el software de simulación lo permita, para la validación de coordinación conjunta de las funciones distancia y sobrecorriente entre líneas, se recomienda|hacer verificaciones problemas de 24|

*Tabla 1. Verificación de ajuste y coordinación de protecciones de líneas*

**Verificación**

||Notas|
|---|---|
|Esquemas de protección suficientes para las características técnicas de la línea|a, l|
|Evaluación de la función ANSI 87L|b, l|
|Evaluación de la función ANSI 21|c|
|Evaluación de la función ANSI 67/67N/67TD|d|
|Análisis de detección de direccionalidad de la función ANSI 67N|e, l|
|Evaluación de sensibilidad de esquemas de teleprotección|g|
|Evaluación de la función ANSI 59|f|
|Validación de la coordinación para condición N-1|h|
|Validación condiciones de recierre automático (ANSI 79) y sincronismo (ANSI 25)|i|
|Evaluación de la función de cierre en falla (SOTF)|j|
|Evaluación de la función de discrepancia de polos|k|

##### Notas:

a. Consultar el documento de *esquemas normalizados de protecciones*, además de lo especificado en los pliegos de la convocatoria UPME con los requisitos técnicos de los esquemas, según parámetros técnicos y condiciones operativas de la nueva línea (como SIR, entre otras).
b. Simular y graficar fallas entre fases de tipo bifásicas (2F) y trifásicas (3F) en el punto medio y los extremos del elemento protegido y los elementos adyacentes de 0 Ω y 10 Ω, fallas a tierra del tipo monofásicas (1F) y bifásicas a tierra (2FT) (para el caso de fallas 2FT, se considera que dicha impedancia se encuentra entre cada fase y tierra) con impedancias de 0 Ω, 10 Ω y 50 Ω. En caso de no detectar fallas de al menos 50 Ω indicar hasta que impedancia de falla opera la protección. Se debe confirmar que la protección opera para fallas internas y bloquea para falas externas.
c. Se deben realizar simulaciones y graficar los correspondientes diagramas R-X para fallas en la línea propia y líneas adyacentes. Estas simulaciones deben considerar fallas al 1%, 50% y 99% de la línea. Para fallas 3F, 2F y 2FT, se deben considerar resistencias de falla de 0 Ω, 5 Ω y 10 Ω. Para fallas 1F, se deben considerar resistencias de fallas de 0 Ω, 5 Ω, 10 Ω, 20 Ω y 30 Ω. Además, se debe validar:
- <u>Zona 1</u>: la detección de fallas de 5 Ω al 50% de la línea y que no detecte fallas en el extremo remoto de la línea. En caso de líneas paralelas, evaluar el alcance de la zona 1 con la línea paralela desenergizada y aterrizada en ambos extremos (ver Figura 3). Si se identifica un riesgo de sobrealcance de zona 1, ya sea en condiciones normales de operación o en mantenimiento, se debe consultar el capítulo de líneas de las *guías de protecciones*.

*Figura 3 Circuito fuera de servicio y puesto a tierra en ambos extremos*

- <u>Zonas 2:</u> la detección de fallas de 5 Ω en el extremo remoto de la línea¹³ y de fallas de por lo menos 20 Ω al 50% de la línea con la activación del esquema POTT. Además, verificar que no existan traslapes de las zonas 2 para fallas con y sin impedancia en la línea propia y en líneas adyacentes. También se debe asegurar que no detecten fallas en otros niveles de tensión de la subestación remota; así como, verificar coordinación con la función de sobrecorriente de tiempo definido (ANSI 50) de los transformadores de la subestación remota. Finalmente, verificar coordinación con la etapa 2 de la función ANSI 50BF de la subestación remota¹⁴. Para el caso de líneas paralelas verificar que no se presente subalcance debido al acoplamiento mutuo de las líneas.
- Zonas 3: Verificar que no detecte fallas en otros niveles de tensión, en caso de hacerlo, se debe asegurar que coordine adecuadamente ante fallas en otros niveles de tensión de la subestación remota. Además, verificar la coordinación con los tiempos de operación de los relés de sobrecorriente de fases de los circuitos adyacentes al extremo remoto, cuando sea aplicable). Finalmente, verificar que no existan traslapes de zonas 3 para fallas con y sin impedancia, tanto en la línea propia como en las líneas adyacentes.
- <u>Zona reversa</u>: validar que no opere ante fallas en otros niveles de tensión de la subestación local. En caso de ajustar la zona 4 para bloqueo de esquemas de teleprotección y lógicas de inversión de corriente, que el alcance de la zona 4 vea fallas calculadas en un punto límite de la zona 2 del extremo remoto. En caso de ajustar la zona 4 para respaldo de la diferencial de barras, que no presente un alcance superior a las zonas 1 o a las protecciones instantáneas de las líneas adyacentes.
- <u>Alcance resistivo:</u> Si se requiere aumentar el alcance resistivo para ampliar el rango de detección de fallas por encima de los porcentajes típicos y definidos en las *guías de protecciones,* se deberá realizar un análisis con el fin de comprobar que la función distancia no operará ante condiciones de
13 En caso de no identificar fallas con impedancia en el extremo remoto con la zona 2, validar si la zona 3 logra detectar fallas para este mismo alcance.

Aplica para subestaciones con acople y/o interruptor y medio.

sobrecarga permitida de la línea. Si se identifican riesgo, se pueden proponer soluciones como recorte de zona de carga (load encroachment).

- Factores de compensación homopolar de acuerdo con los parámetros de la línea, considerando la influencia de las impedancias mutuas para el caso de líneas paralelas.
- Si el software lo permite, para las validaciones de ajustes de equipos existentes donde se recomiende hacer un cambio de ajuste, se recomienda tener en una misma gráfica de simulación la característica de ajuste original y la característica de ajuste nuevo. En caso de que el software no permita mostrar dos características de relés en una misma gráfica, presentar en el documento las dos gráficas de forma paralela.
d. Simular y presentar las validaciones de coordinación para fallas en la línea propia y líneas adyacentes. Estas simulaciones deben considerar fallas al 1%, 50% (opcional para STN) y 99% de la línea. Para fallas trifásicas (3F) y bifásicas (2F), monofásicas (1F) y bifásicas a tierra (2FT) se deben considerar resistencias de falla de al menos 3 resistencias de fallas desde 0 Ω hasta la máxima impedancia que pueda detectar la función. Además, se debe validar que:
- Las curvas de coordinación de protecciones estén por debajo de la curva de daño del conductor.
- Arranque de función ANSI 67 mayor a la capacidad de emergencia de la línea o de los equipos serie que protegen (caso topología línea- transformador). Excepcionalmente este valor podrá estar por debajo del valor de emergencia con justificación y análisis técnico.
- Arranque de la función ANSI 67N mayor al valor de desbalance máximo en la operación más el error esperado del TC.
- Coordinación de sobrecorriente de fases y tierras con protecciones de líneas y transformadores de la subestación remota.
- Coordinación de sobrecorriente de fases y de tierras entre protecciones de transformadores locales y las protecciones propias de la línea, ante fallas a tierra en el extremo local de la línea.
e. Se debe validar en el EACP la correcta detección de la dirección de las fallas realizadas, para fallas a tierra internas y externas a la línea, en dirección hacia adelante y atrás, con y sin impedancia, utilizando los algoritmos de polarización por secuencia cero o por secuencia negativa y los parámetros específicos de cada uno de estos algoritmos (umbrales de tensión, corriente y ángulo de operación). Los análisis de direccionalidad se deben realizar ante diferentes escenarios de operación, considerando contingencias N-1 y la apertura monopolar de línea paralela o adyacente, con el fin de verificar la correcta discriminación de la direccionalidad de la falla. A partir de estos resultados, se debe definir el método que presente una mejor operación o tasa de éxitos para ambos extremos de la

línea. Además, tener en cuenta que el método de polarización a implementar debe ser el mismo para ambos extremos.

f. Se debe validar que los arranques y tiempos de operación definidos se encuentren por debajo de la máxima soportabilidad de los descargadores de sobretensión y demás elementos de la subestación. Validar coordinación con esta misma función en elementos como bancos de capacitores, líneas paralelas y generadores. Validar la posible existencia de esquemas suplementarios en la zona.
g. Verificar el alcance máximo de detección de fallas con impedancia con la operación de los esquemas de teleprotección POTT y Comparación Direccional (CD). Considerar lógica de bloqueo por inversión de corriente, especialmente para casos de líneas paralelas o anilladas.
h. Evaluar la coordinación de protecciones ante N-1 de los elementos del área de influencia.
i. El análisis de los recierres depende de la topología, nivel de tensión del punto de conexión y generadores conectados en la barra:
- <u>STN y STR:</u> En nodos con generación verificar el impacto de recierre trifásico y cierre en falla sobre los sistemas de generación. Se debe evitar que se hagan recierres en nodos con generadores y en transformadores con conexión de manera radial. En el caso de los generadores síncronos verificar la aceleración del rotor. Para líneas en dónde se identifique posibilidad de tener variación de tensión o de ángulo por fuera de los umbrales típicos, graficar mediante simulaciones dinámicas las variables de tensión, frecuencia y ángulo, para validar que cumplan las condiciones definidas en la función ANSI 25 y validar las condiciones sistémicas luego del cierre del interruptor. En el caso de generadores IBG, verificar el impacto sobre la curva de control de Fault Ride Through (FRT). Para líneas en dónde se identifique posibilidad de generar huecos de tensión sucesivos por recierres en falla, verificar que el hueco de tensión causado por los recierres no implique desconexión de plantas por causa de tensiones por fuera de la curva FRT. En caso de identificar posibles desconexiones de las plantas, se deberán tomar medidas que mitiguen riesgos de salidas de dichas plantas.
- <u>SDL:</u> El recierre se debe coordinar con el OR, evitando que se haga un recierre durante condiciones en donde plantas de generación aguas abajo se encuentran conectadas. Se recomienda que el recierre de la protección del OR sea con verificación de tensión cuando se encuentren generadores conectados aguas abajo. En caso de no ser posible la verificación de tensión previa al recierre, se recomienda implementar alguna estrategia que permita ejecutar el recierre en condiciones seguras o en caso de no ser posible, no implementarlo según se acuerde con el OR. Se debe verificar que la función ANSI 79, de la protección del OR, considere el tiempo máximo de apertura del sistema de generación en el punto de

||||Lineamientos para la elaboración y presentación de EACP del SIN colombiano|Subcomité de Protecciones|||
|---|---|---|---|---|---|---|
|j. k. l.|transformadores. transformador|Transformadores: Análisis de energización Evaluación de la función ANSI 87T|de operación de la protección anti-isla. y que el arranque sea mayor a la corriente nominal de la línea. funciones de sobrecorriente de tierras de las líneas adyacentes. En caso de identificar o los mismos tiempos de operación en las bahías de alta y baja tensión. Verificación Esquemas de protección suficientes para las características técnicas del Evaluación de la función ANSI 51/51N/50 Validación de coordinación para condición N-1 Evaluación del esquema de protección en el devanado de compensación|conexión para fallas en el propio circuito con y sin impedancia. Además, que el tiempo del recierre del circuito que alimenta el punto de conexión del generador sea mayor al tiempo máximo de la apertura del equipo de corte del sistema de generación, incluyendo validación y coordinación del tiempo Verificar que la función opere ante fallas de 5 Ohm en el extremo remoto de la línea Se debe validar la correcta coordinación de esta función con las funciones de recierre y de sobrecorriente de tierras. Es decir, verificar que esta función opere después que los tiempos del recierre monofásico de la línea y opere antes de las Aplica para proyectos con líneas nuevas o modificadas, en caso de identificar la afectación a los ajustes actuales causada por un proyecto en el área de influencia o en caso de identificar riesgos para la operación segura y confiable del SIN. En la Tabla 2 se presentan las validaciones de ajuste y coordinación de protecciones para problemas de coordinación de protecciones entre las bahías de alta y baja tensión del transformador, y que este no cuente con alimentación de carga en el terciario, se podrá evaluar implementar márgenes estrechos Tabla 2. Verificación de ajuste y coordinación de transformadores|Notas m, s n, s o, s p q r, s||
|Notas: n.|m.|Consultar el|nuevo transformador.|pliego de requisitos de la convocatoria UPME con técnicos de los esquemas, según parámetros técnicos y condiciones operativas del Se requiere realizar este análisis para transformadores con capacidades iguales o superiores a 60 MVA en redes de nivel 4 o superior. Los estudios de energización se deben realizar en simulación EMT y los resultados deben incluir la evaluación de los impactos de los armónicos de la energización en el transformador propio y en los transformadores paralelos, y de las corrientes de secuencia cero de las líneas de trasmisión que se conectan a la misma barra. Con los resultados obtenidos de las|los requisitos|29|

simulaciones en EMT, analizar las corrientes simpáticas y verificar si se requiere reajustar las protecciones de los equipos de área de influencia ante riesgo de operación indeseada de las mismas.

o. Para relés diferenciales de transformador simular y graficar fallas 1F y 3F en el elemento protegido de 0 Ω y 10 Ω, así como fallas 1F de 50 Ω. Además, se deben simular fallas 1F y 3F externas de 0 Ω. En caso de que la protección no detecte fallas de al menos 50 Ω, se debe indicar hasta que impedancia de falla opera la protección.
p. Para relés sobrecorriente en transformadores simular y graficar
- las curvas de coordinación para fallas en sus diferentes niveles de tensión (baja-media y alta- media y alta-baja), en combinación con el tipo de falla 2FT y 3F con resistencia de fallas de 0 Ω, 5 Ω y 10 Ω, y para fallas 1F hasta 30 Ω. Además, se debe verificar:

- Curvas de coordinación de protecciones estén por debajo de la curva de daño del transformador.
- Arranque de función ANSI 51 mayor a la capacidad de sobrecarga del transformador.
- Arranque de función de ANSI 51N mayor al error de medición esperado del TC.
- Arranque de la función ANSI 50 no detecte fallas en otros niveles de tensión, que no opere ante la corriente inrush (de energización) esperada y que coordine con las protecciones de elementos adyacentes.
- Coordinación de funciones de sobrecorriente de fases y tierra entre protecciones del transformador y extremos remotos de líneas, ante fallas en bujes de alta del transformador y de fallas en la barra del lado de baja tensión del transformador.
- Coordinación de funciones de sobrecorriente de tierra entre protecciones del devanado de alta tensión del transformador y los extremos locales de las líneas, ante barridos de fallas a tierra externas (en las líneas) al 1% y 50% por retornos de secuencia cero a través de la conexión a tierra de los transformadores (ver Figura 4).

*Figura 4 Retornos de corrientes de secuencia cero por la conexión a tierra*

- Coordinación de funciones de sobrecorriente de fases y de tierra entre protecciones del transformador por el lado de baja tensión y extremos locales de las líneas, ante barridos de fallas externas (en las líneas) al 1% y 50%.
q. Evaluar coordinación de protecciones ante N-1 de los elementos del área de influencia, de acuerdo con lo acordado en la reunión de inicio. Para transformadores paralelos considerar la N-1 del transformador paralelo que pueda generar el mayor impacto en la coordinación.
r. Para relés del devanado de compensación describir funciones de protecciones habilitadas para despejar fallas en dicho devanado, ejecutar falla 3F y 1F (si hay corriente a tierra) e indicar el tiempo máximo de despeje de fallas y verificar coordinación con los demás devanados del transformador. En el caso de transformadores con devanados secundario o terciario conectados en delta, incluir verificación de despeje fallas asimétricas ocurridas en la delta; para TC ubicados al interior de la delta incluir la medida de corriente calculada al interior y por fuera de la delta, y verificar que las funciones de sobrecorriente de la delta no operen ante fallas externas en los niveles de tensión de los devanados conectados en Y. Incluir diagrama unifilar detallado del devanado de compensación de los transformadores, incluyendo esquemas de protección disponibles, ubicación de los TC y, en caso de que aplique, cargas conectadas, transformador de zigzag, entre otros.
s. Aplica para proyectos con transformadores nuevos, en caso de identificar la afectación a los ajustes actuales causada por un proyecto en el área de influencia o en caso de identificar riesgos para la operación segura y confiable del SIN.
#### Barras

En la Tabla 3 se presentan las validaciones de ajuste de protecciones para barras y funciones falla interruptor disponibles en las protecciones ANSI 87B.

*Tabla 3. Verificación de ajuste de protecciones de barras*

**Verificación Notas**

Análisis de saturación de los TC relacionados con la función 87B *t* Evaluación de la función ANSI 87B *u*

||Lineamientos para la elaboración y presentación de EACP del SIN colombiano|Subcomité de Protecciones|||||
|---|---|---|---|---|---|---|
||Verificación Análisis ante indisponibilidad de función ANSI 87B Descarte de zonas muertas Evaluar función ANSI 50BF para cada una de las bahías Evaluar tiempo crítico de despeje de falla Evaluar función 50/51 del acople|||Notas v w x y z|||
|Notas: 15 16 17|t. Se debe realizar el análisis de saturación teniendo en cuenta las características técnicas de los TC y su cableado, de acuerdo con las especificaciones del fabricante y lo implementado en sitio. De manera general, se debe seguir el procedimiento y las recomendaciones consignadas en el estándar “IEEE Guide for the Application of Current Transformers Used for Protective Relaying Purposes” equivalente “IEC Technical Report 61869-100 Instrument transformers - Part 100: Guidance for application of current transformers in power system protection¹⁶ u. Para relés diferenciales de barras se simulan fallas 2FT protegido de 0 Ω y 10 Ω y 1F hasta de 50 Ω, y fallas 1F y 3F externas de 0 Ω. Además, se debe verificar: • Definir y señalar las zonas de operación subestación. • Definir y evaluar ajustes de la zona de chequeo. • Detectar fallas de al menos 50 Ω. En caso de no detectar fallas de al menos 50 Ω indicar hasta que impedancia de falla opera la protección. • Se debe confirmar que la protección opera para fallas internas y bloquea para fallas externas. v. Estos análisis de deben presentar en un anexo indisponibilidad de la función 87B, se debe protección existentes y de respaldo, tanto locales como remotos despejen fallas 3F hasta de 5 Ω en la barra de interés, manteniendo la estabilidad¹⁷ En este análisis, de ser necesario, se deben evaluar alternativas de reajuste de protecciones para disminuir al máximo posible el tiempo de despeje de fallas por “IEEE Guide for the Application of Current Transformers Used for Protective Relaying Purposes”, IEEE C37.110-2023, o aquel que lo modifique o sustituya. “IEC Technical Report Instrument transformers - Part 100: Guidance for application of current transformers in power system protection”, IEC 61869-100 2017, o aquel que lo modifique o sustituya. Estabilidad angular, de tensión, de frecuencia y de interacción entre controles o condiciones de resonancia entre equipos del sistema de potencia. Estos análisis requieren actividades coordinadas entre XM y agentes.|y 3F en el diagrama unifilar de la del documento. verificar que los esquemas de del SIN.|15|o en su ”. en el elemento Ante|la 32||

operación de funciones de respaldo ante la indisponibilidad de la protección ANSI 87B, entre las alternativas, se propone¹⁸:

##### <u>Para Bahías de Línea:</u>

- Evaluar habilitar la zona reversa¹⁹ de la función distancia como protección de respaldo en la barra local. Esta acción requiere validación de los alcances resistivos (R) e inductivos (X) para detectar fallas hasta de 5 Ω en la barra local y traslape únicamente con la zona 1 de la función distancia de las líneas que salen de la barra. Se debe evaluar la coordinación con las protecciones de área de influencia para determinar los mejores ajustes de esta zona reversa.
- Evaluar reajustes a la zona 2 de las funciones distancia como protección de respaldo de los extremos remotos. Se debe evaluar la coordinación con las protecciones de área de influencia para determinar los mejores ajustes; la temporización mínima es 250 ms.
- Evaluar la posibilidad de implementar en la barra local esquemas especiales de protección como disparos transferidos, *Reverse InterLocking, etc.*
##### <u>Para Bahías de transformadores:</u>

- Evaluar disminuir dial y/o modificar curva de NI a VI/EI para las funciones ANSI 51 de la Bahía de Transformador (BT) de la barra local, con previa verificación de la selectividad y detección de fallas hasta de 5 Ω en la barra local y coordinación con las protecciones adyacentes (bahías de línea y bahía de baja del transformador).
- Evaluar habilitar la función ANSI 50 en las bahías de transformador de la barra local, manteniendo la selectividad en el despeje de fallas.
- Revisar la posibilidad de implementar la función ANSI 21 en las bahías de transformadores de la barra local. Esta función permite habilitar respaldo hacia adelante y atrás del transformador.
- Evaluar la posibilidad de implementar en la barra local esquemas o lógicas especiales de protección, con habilitación de disparos transferidos a todos los interruptores de la barra en caso de falla.
Adicional a los reajustes descritos, se debe validar la temporización de la función ANSI 50BF en la barra local, con el tiempo de operación de la función distancia según el tipo de configuración de barra donde se va a presentar la indisponibilidad

18En las reuniones 178, 179 y 180 del subcomité de protecciones se evaluaron y definieron las alternativas de reajuste de las protecciones ante indisponibilidad de la protección ANSI 87B. 19 Se recomienda habilitar la función reversa en una zona disponible e independiente de las existentes en el relé y que estén siendo usadas para el esquema de teleprotección.

de la protección ANSI 87B, puesto que algunas funciones normalmente se coordinan para tener la posibilidad de despejar la falla de forma más oportuna y selectiva en la barra de interés. A continuación, algunas consideraciones para la coordinación de protecciones:

1) Si la SE es configuración barra sencilla, con una sola protección ANSI 87B, se debe evaluar el impacto de la operación de la protección ANSI 50BF y que su operación no represente la desconexión de bahías adicionales al competir el ajuste de la Etapa 2 del 50BF, con los tiempos de las funciones de protección de respaldo remotos o locales que actuarían ante indisponibilidad de la ANSI 87B.
2) Si la SE es configuración doble barra o barra sencilla seccionada, con una sola protección ANSI 87B para ambas barras, lo más recomendable será distribuir los campos para operar en dos barras sencillas. Las propuestas de ajustes deben prever esta reconfiguración y consultar al CND si se tendrá una reconfiguración definida para operar ante esta indisponibilidad (ver nota 1 para barra sencilla).
3) Si la SE es de configuración Interruptor y medio, se recomienda que cada barra tenga una protección ANSI 87B independiente para cada barra. Es decir, siempre se tendrá al menos una barra con protección ANSI 87B, por tanto, este análisis no es requerido, ya que para este caso lo mejor es solicitar la barra desenergizada. Sin embargo, en el caso particular donde este tipo de configuración tenga una sola ANSI 87B para la protección de ambas barras, el análisis si aplicará.
Con los ajustes y tiempos de despeje de fallas por protecciones de respaldo, el CND evaluará la viabilidad de la indisponibilidad manteniendo la confiabilidad y estabilidad del sistema. En caso de que el CND determiné que los tiempos de despeje de fallas por protecciones de respaldo sean insuficientes para la operación segura del sistema, será necesario establecer actividades coordinadas entre el promotor del proyecto, XM y demás agentes para encontrar soluciones que permitan la viabilidad de los trabajos (Ej. ESP, esquemas especiales de protecciones u otras acciones).

w. Confirmar si existen o no zonas muertas, considerando la ubicación de los equipos de medida y corte de acuerdo con los diagramas unifilares de detalle. En caso de identificar materialización de una zona muerta se deben definir esquemas que protejan dichas zonas.
x. Se debe verificar que exista coordinación de la etapa 2 de esta función con las zonas 2 de las protecciones de los extremos remotos. Aplica para subestaciones con acople o interruptor y medio.
y. El tiempo de operación de la etapa 2 de la función ANSI 50 BF debe ser menor al tiempo crítico de despeje de falla calculado ante fallas en la subestación protegida.

z. El arranque de las funciones de sobrecorriente del acople debe estar por encima de la máxima corriente declarada del mismo y que coordinen con las protecciones de los elementos adyacentes.
##### Generadores síncronos²⁰:

En la Tabla 4 se presentan las validaciones de coordinación de protecciones para generadores. En EACP relacionados con plantas de generación, incluir la matriz de disparo de los equipos de protección de los generadores, indicando si es disparo parcial o total de las unidades. Además, para todo generador se deberá evaluar su tiempo critico de despeje de fallas con el fin de ajustar adecuadamente las funciones ANSI 78, ANSI 40 y 50BF.

*Tabla 4. Verificación de coordinación de generadores sincronos*

|Verificación|Notas|
|---|---|
|Definición del método de protección del tramo de línea o cable que conecta la casa de máquinas con la subestación|aa|
|Esquemas de protección suficientes para las características técnicas del generador|bb, oo|
|Evaluación de la función ANSI 87G/87TG|cc, oo|
|Evaluación de la función ANSI 21G|dd|
|Evaluación de la función ANSI 51V|ee|
|Evaluación de funciones ANSI 50/51/51N|ff|
|Evaluación de la función ANSI 78|gg, oo|
|Evaluación de la función ANSI 24|hh, oo|
|Evaluación de la función ANSI 40|ii, oo|
|Evaluación de la función ANSI 46|jj, oo|
|Evaluación de impacto ante recierres de líneas en el área de influencia|i|
|Evaluación de funciones ANSI 59|kk|
|Evaluación de funciones ANSI 27|ll|
|Evaluación de la función ANSI 25|mm|
|Evaluación del esquema anti-isla|nn|

##### Notas:

aa. En caso de existir, se deben definir los esquemas para proteger los tramos de línea o de cable que conectan la casa de máquinas con la subestación.

bb. Consultar los requisitos definidos en el acuerdo CNO 1862 o aquel que lo modifique o sustituya, considerando características como la potencia del generador y nivel de tensión al que se conecta.

20 También aplica para autogeneradores síncronos a pequeña y gran escala conectados al STN, STR y SDL.

cc. Para la función diferencial de generador o de grupo transformador-generador, simular y graficar fallas 2FT y 3F en el elemento protegido de 0 Ω y 10 Ω, además de fallas 1F y 3F externas de 0 Ω. En caso de no detectar fallas de al menos 50 Ω indicar hasta que impedancia de falla opera la protección. Se debe confirmar que la protección opera para fallas internas y bloquea para fallas externas.

dd. Para la función distancia de generadores se deben simular y graficar diferentes fallas internas y externas a la central generadora. Se deben realizar las siguientes validaciones:

- Verificación de operación de la zona 1 ante una falla 3F, 2FT, 2F y 1F²¹ de 0 Ω en bornes del generador.
- Verificación de operación de la zona 2 ante una falla 3F, 2FT, 2F y 1F de 0 Ω en bornes del devanado de alta tensión del transformador elevador.
- Verificación de operación de la zona 2 ante falla 3F y 2FT de 0 Ω al 1% y al 99% de la línea de conexión con la red desde la central.
- Verificación de no operación de la función ante fallas 1F, 2F, 2FT y 3F francas en líneas adyacentes y en la subestación remota al punto de conexión.
ee. Se recomienda seleccionar únicamente una opción entre la función distancia (ANSI 21G) y la función sobrecorriente con restricción de tensión (ANSI 51V).

- En caso de habilitar función ANSI 51V, presentar la verificación de coordinación de las funciones de sobrecorriente de las líneas de transmisión (ANSI 67/67N) y de los transformadores de generación (ANSI 51/51N), con la función de sobrecorriente con restricción de tensión (ANSI 51V) de los generadores. Para este caso se deben ejecutar fallas 1F, 2F, 2FT y 3F francas y con impedancia en líneas adyacentes, y validar que exista un margen de coordinación con las protecciones adyacentes a la central de generación de al menos 500 ms.
ff. Validar que las funciones ANSI 51/51N del punto de conexión y del sistema de generación detecte fallas al interior del sistema de generación y coordine con las protecciones del alimentador principal, bahías de transformación de la subestación local y extremos remotos de líneas adyacentes. En caso de que se conecte a la barra de una subestación de distribución, validar la coordinación con todas las bahías de transformador y los extremos remotos en sistemas anillados.

21 La detección de fallas 1F de la función ANSI 21G, ante fallas en el mismo nivel de tensión en bornes del generador, dependerá del aterrizamiento del sistema de generación.

gg. Para pérdida de sincronismo de generadores se deben simular y graficar diferentes fallas dentro del sistema de generación y externas a la central, considerando las siguientes validaciones:

- Verificación de estabilidad de la función ante una falla 3F de 0 Ω al 1%, 50% y 99% de la línea de conexión con la red desde la central, considerando el despeje de la falla por las protecciones principales y de respaldo de la línea (oscilación estable).
- Verificación de estabilidad de la función ante una falla 3F de 0 Ω en bornes del generador y en bujes del devanado de alta tensión del transformador de potencia, considerando el despeje de la falla por las protecciones principales y de respaldo (oscilación estable).
- Verificación de estabilidad de la función ante una falla 3F franca al 1% y al 99% en el circuito adyacente más corto (o con tiempo de operación más lento), despejadas por las protecciones disponibles del circuito y verificar que la función ANSI 78 no opere, siempre que la condición del generador sea estable. En caso de identificarse pérdida de estabilidad del generador ante las fallas evaluadas en este numeral y despejadas por las protecciones disponibles en el circuito, se debe evaluar la posibilidad de disminuir los tiempos de despeje de fallas de los circuitos adyacentes al sistema de generación.
- Verificación de pérdida de sincronismo para una falla 3F de 0 Ω no despejada en tiempos principales y de respaldo de la línea (oscilación inestable).
- Verificación de coordinación con la función ANSI 40 ante pérdida de campo (oscilación inestable). Para esta validación ejecutar una falla 3F en bornes del generador despejada por encima del tiempo crítico de despeje de falla y verificar que para esta condición de pérdida de estabilidad exista selectividad entre las funciones ANSI 78 y ANSI 40; es decir, que opere primero la función ANSI 78 y luego opere la función ANSI 40.
hh. La característica de la protección debe proteger la curva de soportabilidad de sobreexcitación del generador y del transformador elevador al cual se encuentra conectado.

ii. Se deben simular y graficar diferentes fallas dentro del sistema de generación y externas a la central, con el fin de probar la sensibilidad de la protección ante condiciones de cortocircuito y su estabilidad ante diferentes escenarios operativos; teniendo en cuenta las diferentes condiciones topológicas posibles según el número de unidades de la central y del tipo de conexión al sistema eléctrico de potencia. Se debe evaluar que esta función no opere dentro de la curva de capacidad del generador, que coordine con los limitadores del regulador de tensión y que opere para pérdida de campo del generador con y sin carga para los siguientes casos:

- Verificación de operación de perdida de excitación con generador despachado al 100% de su potencia nominal.
- Verificación de operación de perdida de excitación con generador despachado al 25% de la potencia nominal.
- Verificación de estabilidad de la función ante una falla 3F de 0 Ω al 1%, 50% y 99% de la línea de conexión con la red desde la central, considerando el despeje de la falla por las protecciones principales de la línea (oscilación estable).
- Verificación de estabilidad de la función ante una falla 3F de 0 Ω en bujes del devanado de alta tensión del transformador de potencia, considerando el despeje de la falla por las protecciones de respaldo (oscilación estable).
- Verificación de pérdida de sincronismo para una falla 3F de 0 Ω en bornes del generador despejada por debajo y por encima del tiempo critico de despeje de fallas para validar condición de oscilación estable e inestable, respectivamente.
- El tiempo de operación debe coordinar con los tiempos de los limitadores del control de tensión.
jj. Se debe validar que el arranque seleccionado considere el máximo soporte térmico ante secuencia negativa del generador (I2t) y la máxima corriente de secuencia negativa permisible de acuerdo con el tipo de generador (polos salientes, rotor cilíndrico o condensador síncrono) y sus características (potencia, devanado de amortiguamiento, refrigeración). Se debe validar que esta función coordine y permita la operación de funciones como distancia, sobrecorriente residual y falla de interruptor ante condiciones como fallas asimétricas en los circuitos adyacentes, desbalances de corrientes en el sistema, tiempos muertos de recierres monopolares y condiciones de polo abierto. Se debe validar que la característica de la función proteja adecuadamente la curva de soportabilidad de la máquina.

kk. Validar que los valores ajustados se encuentren por debajo de los valores de soportabilidad de tensión del generador, y que no causen disparos indeseados ante eventos transitorios, oscilaciones normales en la red y fenómenos como el de recuperación lenta inducida de tensión (FIDVR).

ll. Ejecutar fallas 1F, 2F, 2FT y 3F externas y validar que no opere (o coordine) con los demás elementos de protección en la red, es decir, validar que no opere ante huecos de tensión ocasionados por fallas externas o eventos transitorios.

mm.Incluir los ajustes de tensión, frecuencia y ángulo de verificación de sincronismo para el cierre del interruptor en el punto de conexión y punto de sincronización de la planta con la red.

|||Lineamientos para la elaboración y presentación de EACP del SIN colombiano|Subcomité de Protecciones||||
|---|---|---|---|---|---|---|
||Notas: 22|nn. Para el caso de permitir la formación de islas planeadas se debe validar que para esta condición de operación aislada exista protecciones o, en su defecto, proponer un segundo considere esta condición operativa. oo. Aplica para proyectos con generadores nuevos, en caso de identificar la afectación a los ajustes actuales causada por un proyecto en el área de influencia o en caso de identificar riesgos para la operación segura y confiable del SIN. 22 Generadores basados en inversores (IBG) : En la Tabla 5 se presentan las verificaciones generadores basados en inversores. Tabla 5. Verificación de coordinación de generadores IBG Verificación Evaluación de funciones ANSI 50/51/51N Evaluación de impacto ante recierres activos de líneas en el área de influencia Evaluación de funciones ANSI 27 Evaluación de funciones ANSI 59 Evaluación de funciones 59N Evaluación del esquema de protección anti-isla pp. Ejecutar fallas 1F, 2F, 2FT y 3F internas y validar que la función ANSI 50/51/51N del punto de conexión y del sistema de generación detecte fallas al interior del sistema de generación y coordine con conecte a la barra de una subestación de distribución, validar la coordinación con todas las bahías de transformador y los extremos remotos en sistemas anillados. Ejecutar fallas cercanas a la salida de los alimentadores derivados de la barra principal de la planta de generación despejadas en tiempos que eviten que los demás inversores en los otros alimentadores crucen la curva LVRT y se pierda toda la generación de la planta por falla en uno solo de ellos. qq. Se debe verificar que exista coordinación entre la cesación de entrega de potencia de los inversores y el disparo de interruptores o desconexión física del sistema de generación por operación de las protecciones. Es decir, ante situación de cruce de las curvas VRT (HVRT o LVRT), primero deben entrar en modo bypass los inversores y luego ocurrir el disparo físico en el punto de conexión También aplica para autogeneradores basados en inversores a pequeña y gran escala conectados al STN, STR y SDL|una adecuada grupo de ajustes que de coordinación de protecciones para los elementos adyacentes. En caso de que se por IBG, y verificar que estas fallas sean|coordinación de Notas pp i rr, qq ss, qq tt uu por operación de las 39|||

funciones de protección, maximizando la oportunidad de reingreso de los inversores.

rr. En caso de ver la necesidad de habilitar la función ANSI 27 a nivel del punto de conexión o de inversor, se debe:

- Verificar que el ajuste de esta función en el sistema de generación y punto de conexión esté por fuera de las curvas límites LVRT definidas por las resoluciones CREG 060, CREG 148, CREG 101-011, (según aplique de acuerdo con las características del proyecto) o aquella que las modifique o sustituya. Teniendo en cuenta que este ajuste se debe validar visto desde el punto de conexión.
- En caso de habilitar la función a nivel de inversor, se debe validar que coordine con esta misma función en el punto de conexión, es decir, que el arranque y tiempo de operación de la función ANSI 27 a nivel de inversor sea mayor que la implementada en el punto de conexión y demás activos externos al mismo; con el fin de brindar soporte ante fallas en el área de influencia y que no se desconecten si no es necesario ante la ocurrencia de eventos externos. Se debe considerar la medida de la tensión a nivel de inversor, teniendo en cuenta la caída de tensión ocasionada por los elementos existentes entre el punto de conexión y el inversor. Ejecutar fallas 1F, 2F, 2FT y 3F externas y validar que esta función coordine con los demás elementos de protección de los elementos adyacentes, es decir, que no opere (o coordine) ante huecos de tensión ocasionados por fallas externas, con el fin de que estos generadores permitan brindar soporte de potencia ante fallas en el área de influencia sin desconectarse si no es necesario. La medida puede ser monofásica o fase segregada.
ss. En caso de habilitar la función ANSI 59 a nivel de punto de conexión o de inversor, se debe:

- Verificar que la función ANSI 59 del sistema de generación en el punto de conexión coordine con la curva HVRT; es decir, estar por fuera de las curvas límites definidas por las resoluciones CREG 060, CREG 148, CREG 101-011 (según aplique de acuerdo con las características del proyecto) o aquella que las modifique o sustituya.
- En caso de habilitar la función a nivel de inversor, se debe validar que coordine con esta misma función en el punto de conexión, es decir, que el arranque y tiempo de operación de la función ANSI 59 a nivel de inversor sea mayor que la implementada en el punto de conexión y demás activos externos al mismo, respetando siempre la soportabilidad de tensión de los equipos de acuerdo con lo declarado por el fabricante; con el fin de brindar soporte ante fallas en el área de influencia y que no se desconecten si no es

necesario ante la ocurrencia de eventos externos. Se debe considerar la medida de la tensión a nivel de inversor, teniendo en cuenta la caída de tensión ocasionada por los elementos existentes entre el punto de conexión y el inversor.

tt. Ejecutar fallas 1F externas y validar que la función ANSI 59N del sistema de generación en el punto de conexión coordine con las protecciones de otros equipos de protección, es decir, que primero operen las protecciones de los activos donde está la falla. Además, se debe validar:

- El valor de umbral definido para la tensión 3V0 ante fallas a tierra en la red.
- Ejecutar fallas 1F, 2F, 2FT y 3F internas, y validar que la función ANSI 59N opere para la condición esperada en redes aisladas.
uu. En caso de que el esquema anti-isla a utilizar sea del tipo ROCOF se debe tener en cuenta el valor de ajuste mínimo de ROCOF definido por el CND según el acuerdo CNO 1862 o aquel que lo modifique o sustituya. Cuando el respaldo por anti-isla sea por realimentación positiva, se debe indicar en el EACP que se cumple con los certificados solicitados en el acuerdo de protecciones.

En caso de proponer habilitar una lógica anti-isla tipo intertrip, se debe verificar que el esquema concebido incluya todas las posibles condiciones de formación de isla definidos con el OR.

#### Generadores conectados al SDL:

Se deben tener en cuenta todas las validaciones mencionadas anteriormente según el tipo de generador (síncrono o basado en inversores), además, adicionar:

- En zonas con alta penetración de generación conectada al SDL, se recomienda validar el impacto de fallas 3F y 2F francas a nivel de transmisión en la zona de influencia sobre las funciones de sobre y baja tensión en el punto de conexión. En caso de requerirse, esta contingencia será definida en la reunión de inicio del proyecto y en caso de ser necesario se deberá ampliar el área de influencia.
- En zonas con alta penetración de generadores conectados al SDL, en las cuales la generación interna sea mayor o igual a la demanda y exista exportación de potencia desde el SDL al STR o cambio en nivel de cortocircuito en el STR mayor al 5%, validar impacto sobre las funciones distancia en las líneas de conexión del STR.
- Para la función ANSI 51/51N ejecutar fallas 1F, 2FT y 3F, internas y externas y validar que: o Las funciones ANSI 51/51N de la cabecera del circuito detecten fallas en el
ramal y opere para fallas en los elementos protegidos, considerando el efecto del aporte de la corriente de los generadores a la falla (Blinding effect).

o Las funciones ANSI 51/51N de las protecciones de los circuitos de distribución coordinen ante fallas en los elementos externos y especialmente ante fallas en elementos “aguas arriba”, teniendo en cuenta el flujo de corrientes bidireccionales en la red de distribución ocasionados por los aportes de corriente de la generación distribuida (sympathetic tripping).

- El EACP debe incluir la coordinación de tiempos de recierre y anti-isla²³ definidos entre el OR y promotor del proyecto, además, considerar el número de intentos de recierre con sus respectivos tiempos de operación, los cuales deberán ser suministrados por el OR al promotor del proyecto como dato de entrada para la elaboración del estudio de protecciones. o Si se tiene re-energización automática, se deberán incluir los ajustes de
magnitud de tensión y tiempo, teniendo en cuenta que estos deben coordinar con los tiempos de operación de disparo físico de las funciones ANSI 27 y ANSI

59. Se debe garantizar que el generador verifique condiciones seguras de conexión a la red, de tal manera que no se permita el cierre del interruptor cuando el circuito del OR esté desenergizado. Esta re-energización debe ser coordinada con el OR que otorga el punto de conexión.
o En caso de disponer de Energy-check (determina ausencia de tensión en el lado del generador) para validar el cierre seguro del generador también se debe incluir el ajuste de tensión por fase.

- En caso de habilitar la función ANSI 27 a nivel del punto de conexión o de inversor, se debe: o Ejecutar fallas 1F internas en el circuito de conexión y validar que la función
ANSI 27 del punto de conexión coordine con las protecciones de sobrecorriente (o principales) del circuito propio.

o Para el caso de sistemas de generación con conexión en “T” (ver Figura 1), ejecutar fallas 1F en el circuito en T y validar que la función ANSI 27 del punto de conexión opere para fallas a tierra en este circuito. En caso de no detectar fallas a tierra, se deberá considerar alguna de las siguientes alternativas: evaluar esquema de protección basado en la función ANSI 51V, ANSI 21, ANSI 59N y/o evaluar apertura secuencial con el interruptor de la cabecera del alimentador, entre otras opciones.

23 Incluir los resultados del estudio de conexión, el cual contiene los casos de posible formación de islas no controlados, y describir detalladamente el tipo de esquema anti-isla principal y respaldo y la justificación técnica de la viabilidad de la implementación de esta.

#### Generadores con frontera compartida:

Se deben tener en cuenta todas las validaciones mencionadas anteriormente según el tipo de generador (síncrono o basado en inversores), además, se adicionan los ítems consignados en la Tabla 6.

*Tabla 6. Verificación de coordinación de generadores con frontera compartida (FC)*

**Verificación Notas** Validación de coordinación para condición N-1 *vv*

##### Notas:

vv. Verificar que ante una contingencia o falla (N-1) de cualquier elemento o unidad de generación de la frontera compartida no se presenten eventos en cascada de los generadores y la red de conexión compartida que hacen parte de esta. Es decir, dentro de la frontera compartida se debe mantener la selectividad de los sistemas de protección.

#### Reactores:

En la Tabla 7 se presentan las validaciones de coordinación de protecciones para reactores

*Tabla 7. Verificación de coordinación de reactores*

##### Verificación

||Notas|
|---|---|
|Evaluación de la función ANSI 87R/87N|ww|
|Evaluación de las funciones ANSI 51/51N/50|xx|
|Evaluación de la función ANSI 50BF|yy|
|Evaluación de la función ANSI 46|zz|

##### Notas:

ww. Para la función diferencial de reactor y de reactor de neutro (si aplica), simular y graficar fallas 1F y 3F en el elemento protegido de 0 Ω, 10 Ω y 1F de 50 Ω, y fallas 1F y 3F externas de 0 Ω (para la diferencial del reactor de neutro solo considerar las fallas desbalanceadas). En caso de no detectar fallas de al menos 50 Ω indicar hasta que impedancia de falla opera la protección. Se debe confirmar que la protección opera para fallas internas y bloquea para fallas externas. - xx. Para relés de sobrecorriente en reactores de fases y neutro simular y graficar las curvas de coordinación para fallas 2F, 2FT y 3F con resistencia de fallas de 0 Ω, 5 Ω y 10 Ω y para fallas 1F hasta 30 Ω. Además, se debe validar:

- Arranque de la función ANSI 51 mayor a la capacidad de sobrecarga del reactor.
- Arranque de la función ANSI 50 no detecta fallas externas.

||||||Lineamientos para la elaboración y presentación de EACP del SIN colombiano|Subcomité de Protecciones|||
|---|---|---|---|---|---|---|---|---|
|yy. zz.|En la Tabla 8|• Condensadores:|TC. bancos de condensadores.|Evaluación de la función ANSI 59 Evaluación de la función ANSI 27|desbalance esperada en el sistema. condensadores. Se debe tener en cuenta que los criterios de ajustes Tabla 8. Verificación de coordinación de condensadores Verificación Evaluación de las funciones ANSI 51/51N/50 Evaluación de función de desbalance de neutro ANSI 60C|Arranque de la función ANSI 51N mayor al error de medición esperado del En caso de que el reactor de neutro cuente con interruptor se deberán calcular y presentar los ajustes de la función falla interruptor. Además, se deberá indicar cuáles son los interruptores que deben abrir ante la operación de la función. Validar que el arranque de la función ANSI 46 sea mayor a la máxima corriente de se presentan las validaciones de coordinación de protecciones para validaciones realizadas deben considerar las características y el tipo de conexión de los|Notas aaa bbb ccc ddd|utilizados y las|
|Notas:|bbb. los ddd.|• • •|elementos||aaa. Para funciones de sobrecorriente en bancos de capacitores simular y graficar y 10 Ω y para fallas 1F hasta 30 Ω. Además, se debe validar: banco de capacitores. operación normal de la red. adyacentes, teniendo sobretensiones temporales en el área de influencia.|curvas de coordinación para fallas 2F, 2FT y 3F con resistencia de fallas de 0 Ω, 5 Ω Arranque de la función ANSI 51 mayor a la capacidad de sobrecarga del Arranque de la función ANSI 50 no detecta fallas externas y mayor a la corriente inrush (de energización) del banco de condensadores. Arranque de la función ANSI 51N mayor al error de medición esperado del TC y la máxima corriente de desbalance esperada ante condiciones de La función ANSI 59 debe coordinar con las funciones de sobretensión de en cuenta las ccc. El tiempo de retardo de la función ANSI 27 debe ser lo suficientemente alto para no operar durante situaciones transitorias que puedan ocurrir en el sistema. Para la función ANSI 60C se deben tener en cuenta las recomendaciones del fabricante. Esta debe coordinar con los fusibles de los condensadores. Verificar|características|- las de 44|

||||Lineamientos para la elaboración y presentación de EACP del SIN colombiano|||Subcomité de Protecciones|||
|---|---|---|---|---|---|---|---|---|
||influencia. D-FACTS²⁴ : adecuadamente|y que protección de la línea propia y adyacentes. equipo en el modelo RMS|coordinación de protecciones para D-FACTS. coordinación de protecciones se parte del principio de que el la corriente de activación del by-pass, se deberán determinar los para la operación segura y confiable del SIN²⁵ integre el modelo real del equipo suministrado por el fabricante equipo en el modelo de cortocircuito completo|que esta función no opere ante corrientes inrush, fallas o maniobras en el área de Se deben tener en cuenta todas las validaciones mencionadas anteriormente para las líneas de transmisión. Adicionalmente, en la Tabla 9 se presentan las validaciones de Las recomendaciones dependen si la función LOR es monofásica o trifásica. proyectos realizados en el área de influencia, en caso de que los niveles de cortocircuito de las fallas realizadas superen el umbral definido por el equipo y el bypass sea trifásico, se podrán considerar los dispositivos en modo bypass. Para el caso en que la corriente de cortocircuito para fallas 3F, 2F y 2FT de hasta 10 Ω y 1F de hasta 30 Ω no supere el valor de considerando un valor fijo de impedancia del equipo (análisis de cortocircuito y/o RMS según aplique). En caso de by-pass monofásico, se deberá evaluar el impacto de este en el área de influencia. Se podrán solicitar análisis adicionales en caso de identificar riesgos. Tabla 9. Verificación de coordinación de FACTS Verificación Definición del escenario que considere los equipos en modo inyección e Evaluación del desempeño del equipo para fallas internas y externas al Evaluación del desempeño del equipo para fallas internas y externa al|la instalación de los D-FACTS no afecta los esquemas de|Para los requisitos de la validación de|by-pass funciona análisis a realizar Notas eee, fff ggg hhh, iii|Para|
|Notas: 24 25|||colombiano, las consideraciones de este ítem se refieren a este tipo de D-FACTS. los FACTS se podrán solicitar simulaciones RMS para verificación detallada.|eee. Para el caso del valor de la impedancia este dato será usado como referencia y podrá ser modificado sin que esto represente una nueva revisión del EACP. Además, debe integrarse al aplicativo de simulación el control real de fabricante, Considerando el incremento en el número de las conexiones masivas de SSSC al sistema En caso de que se identifiquen riesgos en el desempeño de las protecciones en la operación de||.||45|

el cual debe permitir simulaciones balanceadas y desbalanceadas en estado estable y RMS.

fff. Considerar las recomendaciones y los resultados del análisis eléctrico para obtener un escenario que permita la inyección de los D-FACTS en condiciones de estado estable.

ggg. Presentar una tabla para fallas 2F, 2FT y 3F con resistencia de fallas de 0 Ω, 5 Ω y 10 Ω y para fallas 1F hasta 30 Ω e incluir para cada caso el valor de corriente de línea y secuencia cero a través del D-FACTS y el valor de la impedancia, la operación del by-Pass y LOR.

hhh. Presentar una tabla para fallas 1F hasta 30 Ω e incluir para cada caso el valor de corriente de línea y secuencia cero a través del D-FACTS y el valor de la impedancia, la operación del by-Pass y LOR y la operación de la comparación direccional.

iii. Aplica para proyectos con D-FACTS nuevos o modificados, en caso de identificar la afectación a los ajustes actuales causada por un proyecto en el área de influencia o en caso de identificar riesgos para la operación segura y confiable del SIN.

#### Esquemas suplementarios de protección:

Cuando en el área de influencia se encuentran implementados esquemas suplementarios, es preciso verificar que sus ajustes no se traslapen o interfieran con los ajustes calculados para las protecciones del área. En caso de identificarse descoordinación entre las protecciones y el esquema, y que no se puedan administrar en el EACP, se deberán revisar conjuntamente las soluciones entre el CND, agente propietario del esquema y el promotor del proyecto.

- Integralidad de los ESP (Respaldo Local): Para aquellos casos en que los ESP disponibles no permitan lograr una operación selectiva, por ejemplo, de las funciones de sobrecorriente, verificar la integralidad de las funciones de protección de forma que el elemento fallado sea aislado por cualquier función de sus propias protecciones antes que por protecciones de respaldo de otros elementos.
### Resultados de validaciones vía simulación

Para cada escenario de simulación se deben validar todas las rutas de coordinación definidas y verificar el desempeño de las protecciones según los lineamientos presentados en el ítem 9.4; es decir, la verificación de la operación de las protecciones se realiza mediante una combinación de los escenarios de simulación, rutas seleccionadas y diferentes tipos de fallas.

Los resultados de las validaciones vía simulación deben mostrar la coordinación de forma gráfica y pueden ser complementadas mediante tablas de evaluación coordinación en los anexos, estas deben incluir las protecciones del elemento fallado y las protecciones

de los elementos adyacentes que deben operar con sus respectivas funciones de protección de respaldo 26.

# 10 Estructura del documento de estudio de ajuste y coordinación de protecciones

El EACP debe presentarse en secciones o capítulos que permitan identificar claramente el objeto, alcance, parámetros de entrada, metodología, criterios de ajuste aplicados, ajustes de protecciones, validaciones vía simulación y demás consideraciones realizadas para su elaboración. El documento debe contener los ítems descritos a continuación, en el siguiente orden.

## 10.1 Objetivo

Describir el propósito del EACP indicando el nombre oficial del proyecto, equipos nuevos, reconfigurados o impactados por el EACP.

## 10.2 Alcance

Describir el alcance acorde con el área de influencia del EACP, especificando los equipos de protección que serán objeto de ajuste/revisión y coordinación.

## 10.3 Descripción del proyecto o de la red bajo estudio

Describir el proyecto o la red bajo estudio, incluyendo como mínimo la siguiente información:

## 10.4 Etapas del proyecto (Aplica para entrada de nuevos proyectos)

Describir cada una de las etapas y la fecha esperada de ejecución o entrada en operación de cada etapa. Se deben incluir diagramas de la topología de cada etapa.

## 10.5 Ubicación geográfica

Incluir ubicación geográfica del proyecto. Únicamente para el caso de subestaciones nuevas, incluir coordenadas de latitud y longitud.

26 *Se sugiere considerar los formatos definidos en el numeral 8.4 del documento “Technical* *Brochure: Network protection performance audits -Reference: 800 - 2020.” Publicado por el* *CIGRE.*

## 10.6 Área de influencia

Presentar diagrama unifilar en donde se incluya para el área de influencia del EACP todas las líneas, transformadores de potencia y distribución, generadores (especificar el tipo de generador²⁷), reactores y condensadores, SVC, STATCOM, bancos de baterías de soporte de potencia, existentes y nuevos. Adicionalmente, especificar los tramos de línea de transmisión que comparten torre y los enlaces en doble circuito. Se deberán informar los agentes impactados que se identifican en el área de influencia.

## 10.7 Parámetros técnicos

Para los nuevos proyectos, se deben presentar los parámetros para cada nuevo equipo de potencia en una tabla por cada tipo de equipo. Según alcance y características del EACP se deberán acordar cuales tablas aplican. Para cada uno de estos equipos se debe informar si todos los valores reportados corresponden a los valores de placa del elemento otorgados por el fabricante o si algún parámetro corresponde a un valor estimado. A continuación, se describe las tablas propuestas para los principales equipos relacionados:

#### Parámetros de líneas

Indicar los parámetros de tramos aéreos y/o subterráneos (ver Tabla 10). Para los tramos de línea que comparten torre o las líneas en doble circuito, incluir una tabla adicional con la información de impedancias mutuas de secuencia cero y, en casos de configuraciones asimétricas de las fases, las impedancias mutuas de secuencia positiva, halladas mediante programas de cálculo de parámetros (ver Tabla 11).

Tabla 10. Parámetros técnicos de líneas

|Línea|Longitud [km]|R 1 [Ω/km]|X 1 [Ω/km]|R 0 [Ω/km]|X 0 [Ω/km]|B 0 [Ω/km]|B 1 [Ω/km]|Corriente Nominal [A]|Corriente de Emergencia [A] (*)|
|---|---|---|---|---|---|---|---|---|---|
|S/E_A-S/E_B 1 kV||||||||||
|S/E_A-S/E_B n kV||||||||||

(*) “*Valor máximo de corriente que la línea y sus elementos asociados (bajantes de conexión con los pararrayos* *y los transformadores de potencial, trampas de onda, transformadores de corriente, interruptores y* *seccionadores) puede soportar por un periodo de tiempo de 30 minutos.”*
27 *Todo tipo de generador: hidráulico, térmico, biomasa, eólico, solares, entre otros, incluyendo los* *de niveles de tensión inferior a 4.*

Tabla 11. Impedancias mutuas de líneas

|Línea 1|Tensión [kV]|Tramo [km]|Estructuras|Línea 2 (*)|Longitud [km]|R 0M [Ω]|X 0M [Ω]|B 0M [Ω]|
|---|---|---|---|---|---|---|---|---|
|S/E_A-S/E_B 1 kV||Tramo 1 Tramo 2 Tramo 3||S/E_A-S/E_C 1 kV S/E_A-S/E_D 1 kV|||||
|S/E_A-S/E_B n kV||Total|||||||

*(*) En caso de que alguno de los tramos se comparta con varias líneas se deben indicar las diferentes líneas* *relacionadas con dicho tramo.* *(**) Se recomienda incluir el diagrama unifilar del área de influencia en donde se evidencien los tramos en los* *que se comparten las estructuras.*
#### Parámetros de transformadores

En las Tabla 12 y Tabla 13 se presentan los parámetros técnicos de los equipos de transformación. Las impedancias de cortocircuito del transformador deben ser reportadas con base en la menor potencia de la respectiva relación entre devanados, es decir, la impedancia ZHL se debe reportar en base a la menor potencia entre los devanados de alta (H) y baja tensión (L), mientras que la impedancia ZML debe ser reportada en base a la menor potencia entre los devanados de media (M) y baja tensión (L).

Tabla 12. Parámetros técnicos de transformadores de potencia

|Transformador (2)|SH/M/L [MVA] (3)|V[kV] H/M/L|ZHL [%]|Z HM [%]|Z ML [%]|ZHL sec 0 [%]|ZHM sec 0 [%]|ZML sec 0 [%]|Sobrecarga 30 min [%]|Grupo de conexión (4)|
|---|---|---|---|---|---|---|---|---|---|---|
|TRF1 S/E A|||||||||||
|TRFn S/E B|||||||||||

Tabla 13. Parámetros técnicos de transformadores zig-zag o de puesta a tierra

|Transformador|S contínua [MVA]|S falla [MVA]|V alta [kV]|V Baja (1)[kV]|Z Cto. [s]Cto.|Impedancia Homopolar por fase [Ω]|Icc por el neutro [A]|Duración del cto [s]|
|---|---|---|---|---|---|---|---|---|
|TRF1 S/E_A kV|||||||||
|TRFn S/E_B kV|||||||||

*(1) Aplica si tiene devanado de servicios auxiliares.*
#### Parámetros de generadores

En la Tabla 14, la Tabla 15 y la Tabla 16 se presentan los parámetros técnicos requeridos para los equipos de generación. Para el caso de los generadores basados en inversores, presentar los límites de soportabilidad de sobre y baja tensión del inversor, en donde se consignen los límites de tensión y el tiempo que podría soportar el inversor de acuerdo con lo definido por el fabricante.

Tabla 14. Parámetros técnicos de generadores²⁸

**Planta generación** **Unidad de** **Parámetro Valor**

Potencia nominal, [MVA] Tensión nominal, [kV] Corriente nominal, [A] Factor de potencia, [pu] Reactancia Xd saturada, [pu] Reactancia Xq saturada, [pu] **U1** Reactancia Xd’ saturada, [pu] Reactancia Xq’ saturada, [pu] Reactancia Xd” saturada, [pu] Reactancia Xq” saturada, [pu] **Planta A** Inercia, [s] Tipo de puesta a tierra (2) Impedancia de la puesta a tierra [Ω] Potencia nominal, [MVA] Tensión nominal, [kV] Corriente nominal, [A] **U2** Factor de potencia, [pu] Reactancia Xd saturada [pu] Reactancia Xq saturada [pu] Reactancia Xd’ saturada [pu]

28 La información indicada en la Tabla 14 aplica para EACP de centrales de generación síncronas. Para cada EACP se deberá analizar la necesidad de considerar todos los parámetros propuestos. Por ejemplo, para EACP de líneas solo se requieren los datos de potencia, tensión y corriente nominal de los sistemas de generación en el área de influencia.

|Planta|Unidad de generación|Parámetro|Valor|
|---|---|---|---|
|||Reactancia Xq’ saturada [pu] Reactancia Xd” saturada [pu] Reactancia Xq” saturada [pu] Inercia [s] Tipo de puesta a tierra (2) Impedancia de la puesta a tierra [Ω]||
||Un|||
|Planta B||||
|Planta n||||

*(1) Incluir una tabla similar a la* Tabla 12 *para especificar los parámetros técnicos de los transformadores* *de servicios auxiliares de generación.*
*(2) Aplica para transformador zig-zag, transformador de puesta a tierra, entre otros.*
Tabla 15. Parámetros técnicos de inversor generador eólico

|Inversores (1)|Modelo y fabricante|Tipo de máquina|S nominal [MVA]|P activa nominal [MVA]|VAC [kV]|VDC [kV]|I máx Cto. Cto. [KA]|
|---|---|---|---|---|---|---|---|
|Inversor 1||||||||
|Inversor n||||||||

*(1) Si los inversores son de iguales características solo presentar la información técnica de un inversor e* *indicar número de inversores.*
Tabla 16. Parámetros técnicos de inversor PV

|Inversores (1)|Modelo y fabricante|S [MVA] nominal|P activa nominal [MW]|VAC [kV]|VDC [kV]|Cto. I máx [KA]Cto.|
|---|---|---|---|---|---|---|
|Inversor 1|||||||
|Inversor n|||||||

*(1) Si los inversores son de iguales características solo presentar la información técnica de un inversor e* *indicar número de inversores.*
##### Parámetros de equipos de compensación

En la Tabla 17, la Tabla 18 y la Tabla 19 se presentan las tablas modelo para el reporte de los parámetros técnicos de los equipos de compensación estáticos y dinámicos más comunes en el sistema.

Tabla 17. Parámetros técnicos de reactores

**Capacidad** **Tipo de** **Tipo de** **Reactor (1) por paso conexión** **puesta a**

|Reactor (1)|por paso|conexión|puesta a|
|---|---|---|---|
|Reactor 1 S/E_A kV|[Mvar]||tierra|

<u>Reactor 2 S/E_B kV</u>

*(1) Especificar tipo de reactor: Neutro, Línea, Barra, Terciario, entre otros.* Tabla 18. Parámetros técnicos de capacitores

|Condensador|Capacidad por paso [Mvar]|Tipo de conexión|Capacitor [µF]|Tipo de puesta a tierra|
|---|---|---|---|---|
|Capacitor 1 S/E_A kV|||||
|Capacitor n S/E_B kV|||||

Tabla 19. Parámetros técnicos de SSSC

|Función|Parámetro|Valor|
|---|---|---|
|Generales|Nombre del proyecto Modelo del equipo a instalar Número de válvulas instalar por fase Modo de operación válvula Umbral baja corriente operación [kA]||
|Protección By- Pass|Activa (Si/No) Umbral de ajuste [kA] Excluyente con el LOR [Si/No] Operación tripolar [Si/No] Activación IPB [Si/No] Tiempo de activación del IPB [s] Tiempo de restablecimiento [s]||
|Protección LOR|Activa (Si/No) Umbral de ajuste [kA] Excluyente con la protección By-Pass (Si/No) Operación tripolar (Si/No) Activación IPB (Si/No) Tiempo de activación del IPB [s] Tiempo de restablecimiento [s]||

## 10.1 Consideraciones generales

En este ítem se deben listar y detallar las siguientes consideraciones:

- Indicar la versión y el software utilizado para las simulaciones, además de la base de datos inicial considerada como referencia.
- Informar en caso de haber considerado proyectos que todavía no se encuentran en operación.
- Incluir consideraciones específicas de modelado, escenarios operativos, casos de estudio, entre otros.
- Cualquier supuesto, aproximación o consideración específica importante deberá ser consignada en esta sección.
## 10.2 Estudio de flujo y cortocircuito

### Análisis de flujo

Describir las unidades despachadas con sus MW y límites de importación (caso costa). Además, para red completa validar que las tensiones y flujos de potencia deben estar dentro de los limites operativos esperados, esta información puede ser presentada mediante tablas.

### Resultados de cortocircuito

Mediante tablas, para cada etapa del proyecto presentar los resultados de cortocircuito franco (0 Ω) para fallas monofásicas, bifásicas a tierra, bifásicas y trifásicas sólidas en las barras de la red bajo estudio, para demanda mínima, demanda máxima y demanda media (únicamente para proyectos impactados por generación solar). Para PowerFactory se considera el método completo, para otros softwares de simulación, el cortocircuito debe considerar las tensiones y corrientes del flujo de carga (método de superposición).

Tabla 20. Resultados de cortocircuito en demanda máxima

|Barra|Icc demanda máxima sin proyecto [KA]|Icc demanda máxima con proyecto [KA]|Variación Icc demanda máxima con/sin proyecto [%]||||||||||||||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
||1F|2FT|2F|3F|1F|2FT|2F|3F|1F|2FT|2F|3F|||||||
|S/E_A kV S/E_B kV|Ikss|3I0|Ikss|3I0|Ikss|Ikss|Ikss|3I0|Ikss|3I0|Ikss|Ikss|Ikss|3I0|Ikss|3I0|Ikss|Ikss|

Tabla 21. Resultados de cortocircuito en demanda mínima

||||Icc demanda mínima sin proyecto [KA]|||||||Icc demanda mínima con proyecto [KA]|||||Variación Icc demanda mínima con/sin proyecto [%]||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Barra|1F||2FT||2F|3F|1F||2FT||2F|3F|1F||2FT||2F|3F|
|S/E_A kV S/E_B kV|Ikss|3I0|Ikss|3I0|Ikss|Ikss|Ikss|3I0|Ikss|3I0|Ikss|Ikss|Ikss|3I0|Ikss|3I0|Ikss|Ikss|

Tabla 22. Resultados de cortocircuito en demanda media

||||Icc demanda media sin proyecto [KA]|||||||Icc demanda media con proyecto [KA]|||||Variación Icc demanda media con/sin proyecto [%]||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Barra|1F||2FT||2F|3F|1F||2FT||2F|3F|1F||2FT||2F|3F|
|S/E_A kV S/E_B kV|Ikss|3I0|Ikss|3I0|Ikss|Ikss|Ikss|3I0|Ikss|3I0|Ikss|Ikss|Ikss|3I0|Ikss|3I0|Ikss|Ikss|

## 10.3 Características de los sistemas de protección

### Características de los sistemas de protección a instalar

Describir de forma general los nuevos elementos que conforman el sistema de protecciones a instalar. En la Tabla 23 se presenta el formato para el reporte de dicha información. Adicionalmente, se debe incluir la tabla con la matriz de disparo de los nuevos relés del proyecto.

Tabla 23. Sistemas de protección a instalar

**Ref.** **Teleproteccio** **TC (3) TP (3)** **Bahía/ Equipo Funciones es habilitadasn** **Tipo de** **Relación/ Relación/** **Elemento /Relé habilitadas** **recierre**

**(4)** **Núcleos**
**Clase** **Núcleos**

**(1)**
**[A/A]**

**(2)** **[kV/V]**
BL S/E_A-S/E_B kV BT TRFn S/E_A kV BG Un Planta kV Unidad n Planta A Barra n S/E_A kV Reactor n S/E_A kV Capacitor n S/E_A kV

*(1) Se deben indicar las funciones de teleprotección activas en el relé, POTT, PUTT, Comparación* *direccional (67NCD), entre otras.*
*(2) Clase: Indicar la precisión, tipo de núcleo, factor límite de precisión y VA nominales.*
*(3) Indicar si después de la verificación de transformadores de instrumentación existen restricciones con* *alguno de estos equipos.*
*(4) Indicar si la línea cuenta con recierre automático y el tipo de recierre utilizado (monopolar o tripolar)*
### Características de los sistemas de protección existentes en el área de influencia

Incluir una tabla con las características generales de los sistemas de protección existentes en el área de influencia. Esta información deberá ser reportada utilizando el formato presentado en la Tabla 23.

#### Ajuste de protecciones de elementos existentes

Para facilitar la visualización de los ajustes de protecciones existentes en el área de influencia del EACP, en el Anexo 2 (Externo) se presenta un archivo editable con las tablas para presentar dicha información. Es importante aclarar que los parámetros sugeridos para cada una de las funciones de protección no necesariamente apliquen en todos los casos, estos se deberán adaptar según la referencia del relé o las características del equipo de protección.

Para protección de líneas, considerar si se cuenta con esquemas de teleprotección, tales como: esquemas de comunicación en protecciones diferenciales, esquemas POTT, esquema de comparación direccional (CD), esquemas de disparo directo transferido (DDT), esquemas de fuente débil, recierre y sus características, entre otros.

## 10.4 Ajustes propuestos para las protecciones

Para cada etapa del proyecto, presentar en tablas los ajustes finales en valores primarios de cada uno de los equipos de protección involucrados en el proyecto. En caso de que los agentes del área de influencia o el CND lo solicite, los cambios de ajustes deberán aparecer en color rojo y al lado en color negro entre paréntesis el ajuste existente antes de la recomendación de modificación. Estos cambios propuestos deben estar debidamente justificados y validados mediante simulaciones presentados en el documento del estudio, indicando para cada cambio de ajuste existente la razón de la modificación del ajuste.

En el Anexo 2 (Externo), se presentan las tablas modelos para presentar los ajustes de protecciones propuestos tanto para los equipos existentes como para los equipos nuevos que van a ser instalados en el nuevo proyecto. Se sugiere incluir una tabla o párrafo en el documento principal que resuma únicamente los parámetros modificados en el área de influencia (se debe verificar siempre la integralidad de la información y que la información de esta tabla resumen sea coherente con la información presentada en el Anexo 2, para esto se recomienda que todas las tablas estén relacionadas de manera automática con un archivo principal de Excel).

|||Lineamientos para la elaboración y presentación de EACP del SIN colombiano||Subcomité de Protecciones||
|---|---|---|---|---|---|
|• • • •|página web del CNO. lógicas, entre otros. estudio de protecciones. 10.6 Referencias elaboración del estudio. 10.7 Anexos requeridos Unifilares Presentar los unifilares Criterios de ajuste de protecciones coordinación de protecciones del SIN”|Se debe asegurar que se esté consultando la última versión del archivo disponible en la 10.5 Conclusiones y recomendaciones Presentar las conclusiones del estudio y las recomendaciones respectivas, dejando claras los hallazgos y/o riesgos en la coordinación de protecciones para el nuevo proyecto como para la red existente impactada. En este punto, indicar las acciones acometidas para dar solución a las limitaciones identificadas, tales como: reajustes, implementación de Para el caso que no sea posible solucionar con el estudio la limitación en la coordinación de protecciones, el CND definirá con los agentes involucrados el plan de acción y seguimiento requeridos previo a la entrada del proyecto. Incluir las condiciones operativas especiales en el área de influencia para obtener una adecuada coordinación de protecciones. Incluir toda información que se considere relevante durante la elaboración del Incluir una conclusión con el desempeño de las protecciones disponibles en el punto de conexión, según los resultados de las simulaciones realizadas; en caso de ser necesario, se deberán dejar escritos las limitantes del esquema de protección y las recomendaciones de nuevas implementaciones. Referenciar todos los documentos, estándares, etc. detallados de los transformadores de instrumentación. También adjuntar otros unifilares que el agente considere necesario para dar claridad al estudio. Presentar los criterios usados para el ajuste de las protecciones y citar los documentos o referencias bibliográficas en los que basan los mismos. En este ítem se recomienda siempre, en lo posible, utilizar los criterios definidos en las|esquemas de|que fueron utilizadas para la protección para elaborar los EACP, citando la versión utilizada.|del EACP y “guías para el ajuste y 56|

En caso de utilizar los criterios definidos en dichas guías no será necesario consignarlos en el documento, sin embargo, en caso de utilizar algún criterio diferente o adicional, describirlo en este punto e indicar la causa que origina que se tengan consideraciones especiales para el ajuste del relé de protección.

### Memorias cálculo y ajuste de protecciones

Para cada etapa del proyecto, presentar los ajustes de protecciones y los cálculos de cada una de las funciones de protección que fueron modificadas o para las que se recomendaron nuevos ajustes En caso de que alguna de las funciones consignadas en la memoria de cálculo implique condiciones de activación y bloqueo, se deberán describir las lógicas o ecuaciones a implementar, incluyendo sus respectivas temporizaciones y señales de entrada.

### Verificación de saturación de los transformadores de corriente

Verificar si los transformadores de corriente soportan el máximo nivel de cortocircuito obtenido en el ítem 10.2 sin saturarse. Para las protecciones diferenciales de barra y de línea verificar que no exista saturación en los transformadores de corriente del nuevo proyecto; en caso de presentarse saturación se deben proponer acciones correctivas para administrar el riesgo, con su debida justificación técnica, mientras se toman acciones correctivas definitivas. En este ítem aplicar la metodología descrita en las en el estándar “IEEE Guide for the Application of Current Transformers Used for Protective Relaying Purposes” o en su equivalente “IEC Technical Report 61869-100 Instrument transformers

- Part 100: Guidance for application of current transformers in power system protection” y verificar que no se presente saturación de transformadores de corriente en el escenario de máximo cortocircuito. Para la verificación de la protección diferencial de barras, se deben incluir las curvas de magnetización de los TC proporcionadas por fabricante (V, Iexc), resistencia interna del TC y la impedancia secundaria del relé. En caso de no disponer de las curvas, el valor de tensión de codo se podrá obtener a partir de las características de TC equivalentes.
### Verificación del desempeño de los esquemas de protección

Indicar los requerimientos y consideraciones para tener en cuenta en la verificación del desempeño de los sistemas de protección. En el ítem 9.4 se indican los lineamientos y consideraciones requeridas para validar los ajustes y coordinación de los equipos de protección impactados por el proyecto.

En donde aplique, se sugiere complementar las gráficas de validaciones vía simulación presentadas mediante un anexo adicional que contenga las tablas de evaluación de coordinación en donde se muestren los tiempos de operación de protecciones y su respectiva coordinación con elementos adyacentes para los diferentes tipos de fallas en diferentes elementos del área de influencia.

||Lineamientos para la elaboración y presentación de EACP del SIN colombiano|Subcomité de Protecciones|
|---|---|---|
||Anexos adicionales según necesidad||
|como: • • • • • • • •|Análisis de indisponibilidad de la 87B. despachadas centralmente. Curvas de capacidad de equipos. Resultados de flujo de cargas. Resultados de cortocircuito. Estudio de energización de transformadores. Otros estudios especiales requeridos.|En los casos en que el agente y el CND lo consideren necesario, incluir otros anexos, tales Verificación del tiempo crítico de despeje de fallas: Aplica para proyectos de generación o para proyectos que impacten directamente plantas de generación Placas características de equipos: Adjuntar la placa de transformadores de potencia, zig-zag, generadores, reactores y equipos de medida (TC y TP). 58|

# Anexo 1 (Externo)

Plantilla en formato .docx para diligenciamiento del Acta de reuniones de inicio.

# Anexo 2 (Externo)

Plantilla en formato .xlsx con tablas formato para el reporte de ajuste de protecciones.

En el anexo 2, se muestran tablas modelos para presentar los ajustes de las funciones de protecciones para líneas, transformadores, generadores, condensadores y reactores. Las tablas presentadas son un modelo de referencia de los parámetros típicos que se requieren para ajustar dichas funciones de protección. En caso de requerirse información adicional para alguna de las funciones, según tipo de relé, esta deberá ser agregada en su tabla respectiva incluyendo una nota que indique la modificación de la plantilla original.
