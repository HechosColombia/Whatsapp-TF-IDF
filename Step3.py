import numpy as np

# Función para mostrar las primeras 100 palabras comunes y su importancia
# Function to show the first 100 common words and their importance
def explicar_recomendacion(remitente1, remitente2, tfidf_matrix, df, tfidf_vectorizer, top_n=100):
    # Obtenemos los índices de los remitentes en el DataFrame
    # We get the indices of the senders in the DataFrame
    index1 = df[df['remitente'] == remitente1].index[0]
    index2 = df[df['remitente'] == remitente2].index[0]

    # Extraer las características del TF-IDF
    # Extract the TF-IDF features
    feature_names = np.array(tfidf_vectorizer.get_feature_names_out())

    # Obtener las puntuaciones TF-IDF para cada remitente
    # Get the TF-IDF scores for each sender
    tfidf_scores_1 = tfidf_matrix[index1].toarray().flatten()
    tfidf_scores_2 = tfidf_matrix[index2].toarray().flatten()

    # Identificar las palabras comunes entre ambos remitentes
    # Identify common words between both senders
    common_indices = np.intersect1d(np.nonzero(tfidf_scores_1)[0], np.nonzero(tfidf_scores_2)[0])
    common_words = feature_names[common_indices]

    # Ordenar palabras comunes por importancia (suma de las puntuaciones TF-IDF)
    # Sort common words by importance (sum of TF-IDF scores)
    importance_scores = tfidf_scores_1[common_indices] + tfidf_scores_2[common_indices]
    sorted_indices = np.argsort(importance_scores)[::-1]  # Orden descendente / Descending order
    top_common_words = common_words[sorted_indices][:top_n]  # Seleccionar top_n palabras / Select top_n words

    # Mostrar las primeras 100 palabras comunes, la cantidad de veces usadas y su importancia
    # Show the first 100 common words, the number of times used, and their importance
    print(f"\n'{remitente1}' es similar a '{remitente2}' debido a las siguientes palabras comunes:\n")
    print(f"\n'{remitente1}' is similar to '{remitente2}' due to the following common words:\n")

    for word in top_common_words:
        # Obtener el índice de la palabra en las características
        # Get the index of the word in the features
        index = np.where(feature_names == word)[0][0]

        # Mostrar cuántas veces cada remitente usó la palabra y su importancia
        # Show how many times each sender used the word and its importance
        print(f"- Palabra: '{word}'")
        print(f"- Word: '{word}'")

        print(f"  - '{remitente1}' la usó {df['mensaje'][index1].split().count(word)} veces con importancia de {tfidf_scores_1[index]:.4f}")
        print(f"  - '{remitente1}' used it {df['mensaje'][index1].split().count(word)} times with an importance of {tfidf_scores_1[index]:.4f}")

        print(f"  - '{remitente2}' la usó {df['mensaje'][index2].split().count(word)} veces con importancia de {tfidf_scores_2[index]:.4f}")
        print(f"  - '{remitente2}' used it {df['mensaje'][index2].split().count(word)} times with an importance of {tfidf_scores_2[index]:.4f}")
        print()

# Nombre del remitente a recomendar
# Name of the sender to recommend
FAFA = 'Nombre Remitente'

# Ejemplo de uso:
# Example of usage:
recomendar(FAFA)

# Explicar la recomendación comparando 'FAFA' con uno de los remitentes recomendados
# Explain the recommendation by comparing 'FAFA' with one of the recommended senders
explicar_recomendacion(FAFA, results[FAFA][0][0], tfidf_matrix, df, tf, top_n=100)
