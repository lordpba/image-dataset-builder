import os
import ollama
import streamlit as st
from PIL import Image

def generate_image_description(image_path, max_objects):
    """
    Generate an image description using Ollama Llama 3.2 Vision
    with a specified number of objects
    """
    try:
        response = ollama.chat(
            model='llama3.2-vision',
            messages=[{
                'role': 'user',
                'content': f'Identify and name the top {max_objects} objects in this image. Return only the names of the objects, separated by commas, without additional descriptions.',
                'images': [image_path]
            }]
        )
        return response['message']['content']
    
    except Exception as e:
        st.error(f"Error processing the image: {e}")
        return None

def classify_and_rename_images(input_dir, output_dir, max_objects):
    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Iterate through the files in the input directory
    for filename in os.listdir(input_dir):
        # Check if it is an image
        if filename.lower().endswith(('png', 'jpg', 'jpeg', 'bmp', 'gif')):
            try:
                # Full file path
                file_path = os.path.join(input_dir, filename)
                
                # Generate description with Ollama
                description = generate_image_description(file_path, max_objects)

                # Generate new file name using the description
                new_filename = f"{description}{os.path.splitext(filename)[1]}"
                new_file_path = os.path.join(output_dir, new_filename)

                # Save the image with the new name
                Image.open(file_path).save(new_file_path)
                
                st.write(f"Processed {filename} -> {new_filename}")
                st.write(f"Identified objects: {description}")
                
            except Exception as e:
                st.error(f"Error processing {filename}: {e}")

# Streamlit interface
st.title("Image Renamer with Visual LLM")

# User input
input_dir = st.text_input("Input Directory", "./input_images")
output_dir = st.text_input("Output Directory", "./output_images")
max_objects = st.slider("Number of objects to identify", 1, 5, 3)

# Process button
if st.button("Process Images"):
    if os.path.exists(input_dir):
        st.write("Processing images...")
        classify_and_rename_images(input_dir, output_dir, max_objects)
        st.write("Processing completed! Check the output directory.")
    else:
        st.error("The input directory does not exist.")