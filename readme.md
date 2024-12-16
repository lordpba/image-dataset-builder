# Image Dataset Builder

This project is a Streamlit application that renames images based on the objects identified within them using the Ollama Llama 3.2 Vision model. The application allows users to specify the number of objects to identify and renames the images accordingly.

## Features

- Identify and name objects in images using Ollama Llama 3.2 Vision.
- Rename images based on identified objects.
- User-friendly interface with Streamlit.
- Customizable input and output directories.
- Adjustable number of objects to identify.

## Installation

### Clone the Repository

1. Clone the repository:
    ```bash
    git clone <repository-url>
    cd image-dataset-builder
    ```

### Install Dependencies

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Install Ollama

#### Windows

1. Download the Ollama installer from the [official website](https://ollama.com/download).
2. Run the installer and follow the on-screen instructions.

#### macOS

1. Download the Ollama installer from the [official website](https://ollama.com/download).
2. Open the downloaded `.dmg` file and drag the Ollama app to your Applications folder.

#### Linux

1. Download the Ollama package for your distribution from the [official website](https://ollama.com/download).
2. Follow the instructions provided on the website to install the package.

## Usage

1. Run the Streamlit application:
    ```bash
    streamlit run app1.py
    ```

2. Open your web browser and go to `http://localhost:8501`.

3. Enter the input directory containing the images you want to process.

4. Enter the output directory where the renamed images will be saved.

5. Use the slider to select the number of objects to identify in each image.

6. Click the "Elabora Immagini" button to start processing the images.

## Example

1. Input Directory: `./input_images`
2. Output Directory: `./output_images`
3. Number of objects to identify: `3`

The application will process each image in the input directory, identify the specified number of objects, and save the renamed images in the output directory.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.