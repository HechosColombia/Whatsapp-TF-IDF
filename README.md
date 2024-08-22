# Whatsapp-TF-IDF
# WhatsApp Chat Analysis and Recommendation System

## Introduction / Introducción

This project provides a detailed analysis and recommendation system for WhatsApp chats. The system is implemented in Python and is divided into three key steps:
Este proyecto proporciona un sistema detallado de análisis y recomendación para los chats de WhatsApp. El sistema está implementado en Python y se divide en tres pasos clave:

1. **Processing and Cleaning WhatsApp Chat Messages**
2. **Recommending Similar Senders Based on Message Similarity**
3. **Explaining Recommendations by Analyzing Common Words Between Senders**
1. **Procesamiento y limpieza de mensajes de chat de WhatsApp**
2. **Recomendar remitentes similares según la similitud del mensaje**
3. **Explicar las recomendaciones analizando palabras comunes entre los remitentes**

Each step is carefully designed to extract meaningful insights from raw chat data, allowing for personalized recommendations and deeper understanding of communication patterns.

Cada paso está cuidadosamente diseñado para extraer información significativa de los datos sin procesar del chat, lo que permite recomendaciones personalizadas y una comprensión más profunda de los patrones de comunicación.
---

## Table of Contents

1. [Step 1: Processing WhatsApp Chat Messages](#step-1-processing-whatsapp-chat-messages)
   - [Overview](#overview)
   - [Code Explanation](#code-explanation)
2. [Step 2: Sender Recommendation Based on Message Similarity](#step-2-sender-recommendation-based-on-message-similarity)
   - [Overview](#overview-1)
   - [Code Explanation](#code-explanation-1)
3. [Step 3: Explaining Recommendations with Common Words](#step-3-explaining-recommendations-with-common-words)
   - [Overview](#overview-2)
   - [Code Explanation](#code-explanation-2)
4. [Usage Instructions](#usage-instructions)
5. [Requirements](#requirements)
6. [Author](#author)

## Tabla de contenido

1. [Paso 1: Procesar mensajes de chat de WhatsApp](#paso-1-procesar-mensajes-de-chat-whatsapp)
   - [Resumen](#resumen)
   - [Explicación del código](#código-explicación)
2. [Paso 2: Recomendación del remitente basada en la similitud del mensaje](#paso-2-recomendación-del-remitente-basada-en-la-similitud-del-mensaje)
   - [Resumen](#resumen-1)
   - [Explicación del código](#código-explicación-1)
3. [Paso 3: Explicar las recomendaciones con palabras comunes](#paso-3-explicar-las-recomendaciones-con-palabras-comunes)
   - [Resumen](#resumen-2)
   - [Explicación del código](#código-explicación-2)
4. [Instrucciones de uso](#instrucciones-de-uso)
5. [Requisitos](#requisitos)
6. [Autor](#autor)

---

## Step 1: Processing WhatsApp Chat Messages

### Overview

**English:**

In the first step, the script processes a raw WhatsApp chat file to group messages by their respective senders. It reads each line of the file, identifies the sender using a regular expression that matches the date and time format, and appends the messages under the correct sender. The processed messages are then saved into a new file named `mensajes_concatenados.txt`.

**Español:**

En el primer paso, el script procesa un archivo de chat de WhatsApp sin formato para agrupar los mensajes según sus remitentes correspondientes. Lee cada línea del archivo, identifica al remitente utilizando una expresión regular que coincide con el formato de fecha y hora, y añade los mensajes bajo el remitente correcto. Los mensajes procesados se guardan en un nuevo archivo llamado `mensajes_concatenados.txt`.

### Code Explanation

**English:**

1. **Input File**: The script starts by specifying the path to the input file, `Grupo Whatsapp.txt`.
2. **Message Dictionary**: A dictionary is created using `defaultdict(list)` to store messages, where each key is a sender's name and the value is a list of messages from that sender.
3. **Regular Expression**: The script uses a regex pattern to detect lines that start with a date and time, indicating the beginning of a new message.
4. **Sender Identification**: The script splits the line to extract the sender's name and message content.
5. **Appending Messages**: If a line does not contain a sender, it is appended to the last identified sender's messages.
6. **Output File**: Finally, the script writes the concatenated messages to `mensajes_concatenados.txt`.

**Español:**

1. **Archivo de Entrada**: El script comienza especificando la ruta al archivo de entrada, `Grupo Whatsapp.txt`.
2. **Diccionario de Mensajes**: Se crea un diccionario usando `defaultdict(list)` para almacenar los mensajes, donde cada clave es el nombre de un remitente y el valor es una lista de mensajes de ese remitente.
3. **Expresión Regular**: El script utiliza un patrón regex para detectar líneas que comienzan con una fecha y hora, lo que indica el comienzo de un nuevo mensaje.
4. **Identificación del Remitente**: El script divide la línea para extraer el nombre del remitente y el contenido del mensaje.
5. **Añadiendo Mensajes**: Si una línea no contiene un remitente, se añade a los mensajes del último remitente identificado.
6. **Archivo de Salida**: Finalmente, el script escribe los mensajes concatenados en `mensajes_concatenados.txt`.

---

## Step 2: Sender Recommendation Based on Message Similarity

### Overview

**English:**

The second step focuses on recommending senders with similar messaging styles based on the content of their messages. This is achieved through the TF-IDF (Term Frequency-Inverse Document Frequency) algorithm, which converts the text into numerical values that represent how important each word is within the corpus. Cosine similarity is then calculated to find how similar different senders are based on their messages.

**Español:**

El segundo paso se centra en recomendar remitentes con estilos de mensajería similares según el contenido de sus mensajes. Esto se logra a través del algoritmo TF-IDF (Frecuencia Inversa de Documentos por Término), que convierte el texto en valores numéricos que representan la importancia de cada palabra dentro del corpus. Luego se calcula la similitud del coseno para encontrar qué tan similares son los diferentes remitentes en función de sus mensajes.

### Code Explanation

**English:**

1. **Reading the Processed File**: The script reads the `mensajes_concatenados.txt` file into a pandas DataFrame.
2. **TF-IDF Vectorization**: The `TfidfVectorizer` from scikit-learn is used to convert the text messages into a TF-IDF matrix, where each row represents a sender's message and each column represents a term (word).
3. **Cosine Similarity Calculation**: The cosine similarity between each pair of senders is calculated using `linear_kernel`, which compares the TF-IDF vectors.
4. **Storing Results**: A dictionary is created where each sender is associated with their most similar senders.
5. **Recommendation Function**: The `recomendar()` function allows users to input a sender's name and receive a list of the most similar senders based on the calculated similarities.

**Español:**

1. **Lectura del Archivo Procesado**: El script lee el archivo `mensajes_concatenados.txt` en un DataFrame de pandas.
2. **Vectorización TF-IDF**: Se utiliza `TfidfVectorizer` de scikit-learn para convertir los mensajes de texto en una matriz TF-IDF, donde cada fila representa el mensaje de un remitente y cada columna representa un término (palabra).
3. **Cálculo de la Similitud del Coseno**: Se calcula la similitud del coseno entre cada par de remitentes utilizando `linear_kernel`, que compara los vectores TF-IDF.
4. **Almacenamiento de Resultados**: Se crea un diccionario donde cada remitente está asociado con sus remitentes más similares.
5. **Función de Recomendación**: La función `recomendar()` permite a los usuarios ingresar el nombre de un remitente y recibir una lista de los remitentes más similares según las similitudes calculadas.

---

## Step 3: Explaining Recommendations with Common Words

### Overview

**English:**

The final step aims to provide a detailed explanation of why a certain sender was recommended by comparing the common words used by two senders. The script identifies the words that contribute most to the similarity between senders and shows how often these words were used by each sender.

**Español:**

El paso final tiene como objetivo proporcionar una explicación detallada de por qué se recomendó a un determinado remitente comparando las palabras comunes utilizadas por dos remitentes. El script identifica las palabras que más contribuyen a la similitud entre remitentes y muestra con qué frecuencia se usaron estas palabras por cada remitente.

### Code Explanation

**English:**

1. **Identifying Common Words**: The script compares the TF-IDF vectors of two senders to identify the words they both use.
2. **Sorting by Importance**: The common words are sorted by their importance, which is calculated as the sum of their TF-IDF scores in both senders' messages.
3. **Displaying Results**: The top 100 common words, along with how many times each sender used them and their TF-IDF scores, are displayed to explain why the recommendation was made.

**Español:**

1. **Identificación de Palabras Comunes**: El script compara los vectores TF-IDF de dos remitentes para identificar las palabras que ambos utilizan.
2. **Ordenación por Importancia**: Las palabras comunes se ordenan según su importancia, que se calcula como la suma de sus puntuaciones TF-IDF en los mensajes de ambos remitentes.
3. **Mostrando Resultados**: Se muestran las 100 palabras comunes principales, junto con la cantidad de veces que cada remitente las usó y sus puntuaciones TF-IDF, para explicar por qué se hizo la recomendación.

---

## Usage Instructions

**English:**

1. **Prepare the Input File**: Place your WhatsApp chat file in the same directory as the script and name it `Grupo Whatsapp.txt`.
2. **Run Step 1**: Execute the script to generate the `mensajes_concatenados.txt` file, which contains the cleaned and grouped messages.
3. **Run Step 2**: Use the `recomendar()` function to generate a list of similar senders based on their messaging style.
4. **Run Step 3**: Use the `explicar_recomendacion()` function to understand the common words that led to the recommendation.

**Español:**

1. **Preparar el Archivo de Entrada**: Coloca tu archivo de chat de WhatsApp en el mismo directorio que el script y nómbralo `Grupo Whatsapp.txt`.
2. **Ejecutar el Paso 1**: Ejecuta el script para generar el archivo `mensajes_concatenados.txt`, que contiene los mensajes agrupados y limpiados.
3. **Ejecutar el Paso 2**: Usa la función `recomendar()` para generar una lista de remitentes similares en función de su estilo de mensajería.
4. **Ejecutar el Paso 3**: Usa la función `explicar_recomendacion()` para entender las palabras comunes que llevaron a la recomendación.

---
IF IT SAYS MULTIMEDIA OMITTED IT MEANS THERE IS SIMILARITY BECAUSE THEY BOTH SEND MANY FILES
SI DICE MULTIMEDIA OMITIDO SIGNIFICA QUE HAY SIMILITUD DEBIDO A QUE AMBOS ENVIAN MUCHOS ARCHIVOS

## Requirements

To run this project, you need the following dependencies:

- Python 3.x
- pandas
- scikit-learn
- nltk

You can install all required packages using the following command:

```bash
pip install pandas scikit-learn nltk
