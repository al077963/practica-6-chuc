# 🧱 Práctica 5: Modelado de problemas en Ingeniería Civil

## 🎯 Objetivo

Al finalizar esta práctica, los estudiantes deberán:

-   Comprender el proceso de modelado de un problema real en el contexto
    de la ingeniería civil, desde el análisis hasta la validación de
    resultados.
-   Aplicar estructuras de datos (listas y matrices) para representar
    información topográfica o de costos.
-   Implementar funciones modulares en Python que realicen:
    -   **Análisis:** obtención y validación de datos.
    -   **Diseño:** creación de funciones que resuelvan el problema paso
        a paso.
    -   **Pruebas:** verificación de resultados con datos controlados.
-   Calcular, a partir de estructuras de datos, los costos totales
    directos, indirectos y la utilidad.
-   Integrar y ejecutar un programa que muestre los resultados de forma
    clara y verificable.

------------------------------------------------------------------------

## 🧱 Tema propuesto

**Modelado de costos, presupuestos y administración de un proyecto de
construcción.**

------------------------------------------------------------------------

## 🧩 Marco teórico

En la ingeniería civil, el **presupuesto de obra** es el documento que
integra todos los costos directos e indirectos necesarios para ejecutar
una construcción.\
Un presupuesto bien estructurado considera tres etapas:

1.  **Análisis:** Identificación de los recursos y definición de precios
    unitarios.\
2.  **Diseño:** Agrupación de datos en estructuras lógicas para calcular
    subtotales y utilidad.\
3.  **Validación:** Verificación de resultados y coherencia de los
    cálculos.

Este modelo aplica estructuras de datos como **listas** y
**diccionarios** para almacenar información sobre materiales, cantidades
y precios.\
Se utilizan **funciones modulares** que organizan el flujo del programa:
clasificación de gastos, cálculos parciales y presentación de
resultados.

------------------------------------------------------------------------

## 💻 Desarrollo del modelo computacional

El programa utiliza **Tkinter** como interfaz gráfica.\
El usuario puede seleccionar materiales, ingresar la cantidad y el
precio unitario.\
Cada material tiene una unidad contextual (por ejemplo, litros, sacos,
m³).\
El sistema clasifica automáticamente los conceptos como **costos
directos** o **indirectos**, según el tipo.

### Estructura de datos principal

``` python
{
  "nombre": "Cemento",
  "tipo": "Directo",
  "cantidad": 50,
  "precio_unitario": 180.0,
  "subtotal": 9000.0
}
```

------------------------------------------------------------------------

## ⚙️ Funciones principales

  -----------------------------------------------------------------------
  Función                       Descripción
  ----------------------------- -----------------------------------------
  `determinar_tipo(nombre)`     Clasifica un material como gasto directo
                                o indirecto.

  `agregar_material()`          Obtiene los datos del usuario, calcula
                                subtotales y guarda la información.

  `actualizar_contexto()`       Cambia las etiquetas según el material
                                seleccionado.

  `actualizar_lista()`          Refresca la lista de materiales
                                disponibles.

  `mostrar_resultado()`         Calcula los totales y genera el desglose
                                final.
  -----------------------------------------------------------------------

------------------------------------------------------------------------

## 🪟 Interfaz gráfica

La interfaz está compuesta por: - Menú desplegable (`OptionMenu`) para
seleccionar materiales. - Campos (`Entry`) para ingresar cantidad y
precio. - Botones (`Button`) para agregar materiales y calcular el
presupuesto. - Cuadro de texto (`Text`) para mostrar los resultados
finales.

------------------------------------------------------------------------

## 📊 Resultados esperados

    ========== DESGLOSE ==========

    🔹 GASTOS DIRECTOS:
     - Cemento: 50 x $180.00 = $9,000.00
     - Arena: 5 x $300.00 = $1,500.00
    Total Directos: $10,500.00

    🔸 GASTOS INDIRECTOS:
     - Supervisión: 2 x $800.00 = $1,600.00
    Total Indirectos: $1,600.00

    ========== RESUMEN ==========
    Costos directos:   $10,500.00
    Costos indirectos: $1,600.00
    Utilidad (10%):    $1,210.00
    💵 TOTAL FINAL:    $13,310.00

------------------------------------------------------------------------

## 🧠 Validación del modelo

Se realizaron pruebas con diferentes materiales para verificar: - La
clasificación correcta de cada gasto. - La precisión de los cálculos. -
La actualización automática de los textos según el contexto.

------------------------------------------------------------------------

## 🧾 Conclusión

El modelo demuestra cómo la programación puede aplicarse al **modelado
de problemas reales en ingeniería civil**.\
El uso de Tkinter permitió crear una herramienta visual e intuitiva que
automatiza cálculos y mejora la organización de costos.

------------------------------------------------------------------------

## ⚙️ Ejecución del programa

**Archivo:** `presupuesto_tkinter.py`

**Modo de uso:** 1. Abrir con IDLE o Visual Studio Code.\
2. Ejecutar con: `bash    python presupuesto_tkinter.py` 3. Ingresar los
datos en la ventana y presionar "Calcular Presupuesto".

------------------------------------------------------------------------

## 📚 Fuentes consultadas

-   Python Software Foundation. (2024). *Tkinter Documentation*.
    <https://docs.python.org/3/library/tkinter.html>\
-   Facultad de Ingeniería Civil, UNAM. (2023). *Estimación de Costos en
    la Construcción*.\
-   Instituto Mexicano del Cemento y del Concreto A.C. (IMCYC). (2023).
    *Manual de materiales y costos de construcción*.
