import os
import ollama
import streamlit as st
from PIL import Image

def generate_image_description(image_path, max_objects):
    """
    Genera una descrizione dell'immagine usando Ollama Llama 3.2 Vision
    con un numero specifico di oggetti richiesti
    """
    try:
        response = ollama.chat(
            model='llama3.2-vision',
            messages=[{
                'role': 'user',
                'content': f'Identifica e nomina i {max_objects} oggetti principali in questa immagine. Restituisci solo i nomi degli oggetti, separati da virgole, senza descrizioni aggiuntive.',
                'images': [image_path]
            }]
        )
        return response['message']['content']
    
    except Exception as e:
        st.error(f"Errore nell'elaborazione dell'immagine: {e}")
        return None

def classify_and_rename_images(input_dir, output_dir, max_objects):
    # Crea la directory di output se non esiste
    os.makedirs(output_dir, exist_ok=True)

    # Itera attraverso i file nella directory di input
    for filename in os.listdir(input_dir):
        # Controlla che sia un'immagine
        if filename.lower().endswith(('png', 'jpg', 'jpeg', 'bmp', 'gif')):
            try:
                # Percorso completo del file
                file_path = os.path.join(input_dir, filename)
                
                # Genera descrizione con Ollama
                description = generate_image_description(file_path, max_objects)

                # Genera nuovo nome file usando la descrizione
                new_filename = f"{description}{os.path.splitext(filename)[1]}"
                new_file_path = os.path.join(output_dir, new_filename)

                # Salva l'immagine con il nuovo nome
                Image.open(file_path).save(new_file_path)
                
                st.write(f"Elaborato {filename} -> {new_filename}")
                st.write(f"Oggetti identificati: {description}")
                
            except Exception as e:
                st.error(f"Errore nell'elaborazione di {filename}: {e}")

# Interfaccia Streamlit
st.title("Rinominatore di Immagini con LLM visuale")

# Input utente
input_dir = st.text_input("Directory di Input", "./input_images")
output_dir = st.text_input("Directory di Output", "./output_images")
max_objects = st.slider("Numero di oggetti da identificare", 1, 5, 3)

# Pulsante di elaborazione
if st.button("Elabora Immagini"):
    if os.path.exists(input_dir):
        st.write("Elaborazione immagini in corso...")
        classify_and_rename_images(input_dir, output_dir, max_objects)
        st.write("Elaborazione completata! Controlla la directory di output.")
    else:
        st.error("La directory di input non esiste.")