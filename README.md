# ⚡ RC Circuit Analysis with ESP32 + Numerical Simulation

Este proyecto integra **electrónica, ecuaciones diferenciales y desarrollo full stack** para analizar el comportamiento de un **circuito RC** mediante:

- 📡 Datos experimentales capturados con un ESP32  
- 🧮 Simulación numérica usando el método de Euler  
- 🌐 Visualización en una aplicación web (Next.js)  
- 🧠 Backend en Django para procesamiento y almacenamiento  

---

## 🧩 Descripción del Proyecto

El objetivo principal es **comparar el comportamiento real de un circuito RC** con su **modelo matemático teórico**, utilizando herramientas modernas de desarrollo.

El sistema completo consta de:

- 🔌 Un circuito RC físico
- 📟 Un ESP32 que mide el voltaje del capacitor en función del tiempo
- 🐍 Un backend en Django que recibe y almacena los datos
- ⚛️ Un frontend en Next.js que grafica y compara:
  - Datos experimentales
  - Datos simulados

---

## ⚡ Teoría: Circuito RC

Un circuito RC está compuesto por:

- Una resistencia \( R \)
- Un capacitor \( C \)

Cuando el capacitor se descarga, su comportamiento está gobernado por la **Ley de Voltajes de Kirchhoff**:

$$
RC \frac{dv(t)}{dt} + v(t) = 0
$$

---

### 📘 Solución analítica

La solución de esta ecuación diferencial es:

$$
v(t) = V_0 e^{-\frac{t}{RC}}
$$

Donde:

$$
- \( V_0 \): voltaje inicial
- \( \tau = RC \): constante de tiempo
$$
---

## 🧮 Método de Euler (Simulación)

Para simular la ecuación diferencial, utilizamos el **método de Euler**, que aproxima la solución de forma iterativa:

$$
v_{n+1} = v_n + h \cdot \left(-\frac{1}{RC} v_n\right)
$$

Donde:

$$
- \( h \): tamaño de paso
- \( v_n \): valor actual
- \( v_{n+1} \): siguiente valor aproximado
$$

Este método permite generar una aproximación numérica de la curva exponencial.

---

## 📡 Datos Experimentales

El ESP32:

- Lee el voltaje del capacitor usando ADC
- Registra el tiempo en milisegundos
- Envía los datos como:

```json
[
  { "t": 0.001, "v": 3.04 },
  { "t": 0.031, "v": 2.95 }
]
