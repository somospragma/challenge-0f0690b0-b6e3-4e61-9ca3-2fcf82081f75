# Desarrollo de función Lambda para procesamiento de eventos

En el contexto de una plataforma de banca digital, se requiere desarrollar una función Lambda que procese eventos de transacciones y gestione tareas de manera serverless. La función debe ser capaz de recibir eventos, procesarlos y almacenar los resultados en una base de datos NoSQL. El objetivo es asegurar que las transacciones se registren correctamente y se gestionen de forma eficiente.

## Informacion General

| Campo | Valor |
|-------|-------|
| **Tema** | AWS Lambda serverless |
| **Nivel** | junior-l2 |
| **Tipo** | practical |
| **Tiempo estimado** | 3-4 horas |

## Fases del Reto

### Fase 0: Configuración del Proyecto

**Objetivo:** Obtener el proyecto base funcional enviando el Código Base a un asistente de IA, que lo analizará, corregirá errores y generará un ZIP listo para usar.

**Tiempo estimado:** 15-30 minutos

**Instrucciones:**

- Asegúrate de tener instalado para ejecutar el proyecto: Un IDE o editor de código.
- Copia todo el contenido del campo **Código Base** de este reto — incluyendo el texto de instrucciones que aparece al inicio.
- Abre un asistente de IA (Claude en claude.ai, ChatGPT o Gemini — se recomienda Claude), pega el contenido copiado en el chat y envíalo.
- El asistente analizará los archivos, corregirá errores y generará un archivo ZIP descargable. Descárgalo y extráelo en la carpeta donde quieras trabajar.
- Verifica que el proyecto arranca sin errores.

**Entregable:** El proyecto compila/arranca sin errores.

<details>
<summary>Pistas de conocimiento</summary>

- Copia el Código Base completo incluyendo el texto de instrucciones al inicio — esas instrucciones le indican al asistente exactamente qué hacer con los archivos.
- Si el asistente no genera el ZIP automáticamente al terminar el análisis, escríbele: "genera el ZIP ahora".
- Si el proyecto tiene errores al arrancar, comparte el mensaje de error con el mismo asistente para que lo corrija.

</details>

### Fase 1: Definición de la función Lambda

**Objetivo:** Establecer los requisitos básicos de la función Lambda y su integración con la base de datos NoSQL.

**Tiempo estimado:** 1 hora

**Instrucciones:**

- Identificar los eventos que la función Lambda debe procesar.
- Definir los datos que se deben almacenar en la base de datos NoSQL.

**Entregable:** Descripción detallada de los eventos y datos a almacenar.

<details>
<summary>Pistas de conocimiento</summary>

- Considera los tipos de eventos que son comunes en transacciones bancarias.
- Piensa en la estructura de datos necesaria para almacenar la información de manera eficiente.

</details>

### Fase 2: Implementación de la lógica de procesamiento

**Objetivo:** Desarrollar la lógica para procesar los eventos y almacenar los resultados en la base de datos NoSQL.

**Tiempo estimado:** 2 horas

**Instrucciones:**

- Implementar la función Lambda para procesar los eventos identificados en la fase anterior.
- Asegurar que los datos se almacenen correctamente en la base de datos NoSQL.

**Entregable:** Función Lambda implementada y conectada a la base de datos NoSQL.

<details>
<summary>Pistas de conocimiento</summary>

- Considera cómo manejar posibles errores durante el procesamiento de eventos.
- Piensa en la eficiencia del almacenamiento de datos.

</details>

## Dimensiones Evaluadas

- **queEs**: ¿Qué es una función Lambda y cuál es su propósito en este contexto?
- **paraQueSirve**: ¿Para qué sirve la función Lambda en el procesamiento de eventos bancarios?
- **comoSeUsa**: ¿Cómo se implementa y conecta una función Lambda a una base de datos NoSQL?
- **erroresComunes**: ¿Cuáles son los errores comunes que pueden ocurrir durante el procesamiento de eventos y cómo se manejan?

## Criterios de Evaluacion

- Identificación correcta de eventos a procesar.
- Definición adecuada de la estructura de datos para almacenamiento.
- Implementación funcional de la lógica de procesamiento.
- Manejo de errores durante el procesamiento de eventos.
- Conexión exitosa de la función Lambda a la base de datos NoSQL.

---

*Reto generado automaticamente por Challenge Generator - Pragma*
