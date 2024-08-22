import re
from collections import defaultdict

# Ruta del archivo de entrada
# Path to the input file
input_file = 'Grupo Whatsapp.txt'

# Creamos un diccionario para almacenar los mensajes por remitente
# We create a dictionary to store the messages by sender
messages = defaultdict(list)

# Expresión regular para identificar el formato de fecha y hora de los mensajes
# Regular expression to identify the date and time format of the messages
pattern = r'(\d{1,2}/\d{1,2}/\d{4}, \d{1,2}:\d{1,2}\s[ap]\.\sm\.\s- )'

# Variables para guardar el último remitente identificado
# Variables to store the last identified sender
current_sender = None

# Leemos el archivo línea por línea
# We read the file line by line
with open(input_file, 'r', encoding='utf-8') as file:
    for line in file:
        # Verificamos si la línea tiene un formato de fecha y hora
        # We check if the line has a date and time format
        if re.match(pattern, line):
            # Extraemos el remitente del mensaje
            # We extract the sender from the message
            sender_message = line.split(' - ', 1)
            if len(sender_message) > 1:
                parts = sender_message[1].split(':', 1)
                if len(parts) > 1:
                    # Guardamos el remitente actual
                    # We save the current sender
                    current_sender = parts[0].strip()
                    # Guardamos el mensaje
                    # We save the message
                    message = parts[1].strip()
                    # Guardamos el mensaje bajo el remitente correspondiente
                    # We store the message under the corresponding sender
                    messages[current_sender].append(message)
        else:
            # Si la línea no tiene un remitente, se asume que es del último remitente identificado
            # If the line doesn't have a sender, it is assumed to be from the last identified sender
            if current_sender:
                # Agregamos la línea al mensaje del remitente actual
                # We add the line to the current sender's message
                messages[current_sender].append(line.strip())

# Creamos un archivo de salida
# We create an output file
output_file = 'mensajes_concatenados.txt'
with open(output_file, 'w', encoding='utf-8') as file:
    for sender, msgs in messages.items():
        # Escribimos el nombre del remitente seguido de los mensajes concatenados
        # We write the name of the sender followed by the concatenated messages
        file.write(f"{sender}: {' - '.join(msgs)}\n\n")

# Indicamos que el archivo se ha generado exitosamente
# We indicate that the file has been successfully generated
print(f"Archivo '{output_file}' generado exitosamente.")
print(f"File '{output_file}' generated successfully.")