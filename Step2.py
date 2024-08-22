import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from pprint import pprint
import nltk
from nltk.corpus import stopwords

# Descarga las stopwords si no las tienes
# Download the stopwords if you don't have them
nltk.download('stopwords')

# Ahora puedes usar stopwords español o ingles
# Now you can use stopwords spanish or english
stop = list(stopwords.words('spanish'))

# Paso 1: Leer el archivo y procesar el contenido
# Step 1: Read the file and process the content
def leer_archivo(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    remitente = []
    mensaje = []
    current_remitente = ''
    current_mensaje = ''

    for line in lines:
        line = line.strip()
        if not line:
            continue
        if ':' in line:
            if current_remitente:
                # Si ya tenemos un remitente actual, lo guardamos
                # If we already have a current sender, we save it
                remitente.append(current_remitente)
                mensaje.append(current_mensaje.strip())
            # Extraemos el remitente y el mensaje
            # We extract the sender and the message
            current_remitente, current_mensaje = line.split(':', 1)
        else:
            # Si la línea no tiene remitente, la añadimos al mensaje actual
            # If the line doesn't have a sender, we add it to the current message
            current_mensaje += ' ' + line

    # Añadimos el último remitente y mensaje si existe
    # We add the last sender and message if it exists
    if current_remitente:
        remitente.append(current_remitente)
        mensaje.append(current_mensaje.strip())

    # Devolvemos un DataFrame con remitente y mensaje
    # We return a DataFrame with sender and message
    return pd.DataFrame({'remitente': remitente, 'mensaje': mensaje})

# Usamos la función para leer el archivo
# We use the function to read the file
df = leer_archivo('mensajes_concatenados.txt')

# Paso 2: Aplicar TF-IDF
# Step 2: Apply TF-IDF
stop = list(stopwords.words('spanish'))
tf = TfidfVectorizer(stop_words=stop)
tfidf_matrix = tf.fit_transform(df['mensaje'])

# Paso 3: Calcular similitudes entre remitentes
# Step 3: Calculate similarities between senders
cosine_similarities = linear_kernel(tfidf_matrix, tfidf_matrix)
results = {}

# Recorremos cada remitente para encontrar sus similares
# We iterate over each sender to find their similar ones
for idx, row in df.iterrows():
    similar_indices = cosine_similarities[idx].argsort()[:-4:-1]
    similar_items = [(df['remitente'][i], round(cosine_similarities[idx][i], 3)) for i in similar_indices if i != idx]
    # Guardamos los remitentes similares en un diccionario
    # We save similar senders in a dictionary
    results[row['remitente']] = similar_items

# Función para recomendar remitentes similares
# Function to recommend similar senders
def recomendar(remitente):
    if remitente in results:
        # Mostramos los remitentes similares
        # We display the similar senders
        pprint(f"La recomendación / The recomendation is: {results[remitente]}")
    else:
        # Mostramos un mensaje si no se encuentra el remitente
        # We display a message if the sender is not found
        print(f"No se encontró el remitente: {remitente}")
        print(f"Sender not found: {remitente}")

# Ejemplo de uso:
# Example of usage:
recomendar('Nombre Remitente')
