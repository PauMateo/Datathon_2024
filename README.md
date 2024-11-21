# Datathon 2024 🥭🤖🥭🤖🥭

Welcome to our GitHub repository featuring our solution to the Datathon FME 2024 Mango Challenge. We are a team of three data scientist and one computer scientist.

The Mango Challenge demanded to make an specialization of a tagging model to identify clothing characteristics. We have used the pre-trained model EfficientNet-B2 with a modified last layer and backpropagation . Also they demanded a prototype of an app for their designers to tag de products and we have delivered using the popular PyQt6 framework.
https://www.kaggle.com/t/6658f489d3d8447dba8d0c04196cfd07

# Datathon FME 2024 - Product Attribute Prediction

This repository contains my team's solution to the Mango's challenge: **Product Attribute Prediction Challenge**, which aims to automate the process of extracting design attributes from product images and metadata. By leveraging machine learning, the solution streamlines the creation of comprehensive product sheets, ensuring data quality, consistency, and efficiency.  

---

## Table of Contents  
- [Overview](#overview)  
- [Solution Approach](#solution-approach)  
- [Features](#features)  
- [Tech Stack](#tech-stack)  
- [Installation](#installation)  
- [Usage](#usage)  
- [File Structure](#file-structure)  
- [Acknowledgements](#acknowledgements)  

---

## Overview  
The lifecycle of a fashion product involves multiple stages: from inspiration and design to prototyping and cataloging. Logging attributes like silhouette type, sleeve length, and more is a manual and time-consuming process. This challenge addresses this bottleneck by predicting attributes from images and metadata, automating the process for efficiency and accuracy.

Our solution uses **Transfer Learning** with the **EfficientNetB2** architecture, fine-tuned for this task, combined with a **PyQT-based GUI** to provide an intuitive and functional interface.

---

## Solution Approach  

1. **Model Training**  
   - A pre-trained **EfficientNetB2** convolutional neural network (CNN) was fine-tuned using PyTorch to extract meaningful features from product images.  
   - Custom training loops ensured high performance and adaptability to the challenge's specific requirements.  

2. **Prediction**  
   - Each product in the test set is processed to predict attribute values across 11 possible types.  
   - Items with non-applicable attributes are assigned the value `"INVALID"`.  

3. **Graphical User Interface (GUI)**  
   - Developed using **PyQT**, the GUI allows users to:  
     - Load product images  
     - Input the clothe type  
     - View predicted attribute values in real time
   - The interface ensures usability for both technical and non-technical stakeholders.  

---

## Features  

- **High Accuracy**: Fine-tuning EfficientNetB2 ensures precise attribute prediction.  
- **Intuitive GUI**: A user-friendly PyQT-based interface for visualization and interaction.  
- **Scalability**: Easily adaptable for future datasets and attribute types.  
- **Error Handling**: Automatically handles non-applicable attributes with the `"INVALID"` designation.  

---

## Tech Stack  

- **Deep Learning Framework**: PyTorch  
- **Model Architecture**: EfficientNetB2 (Transfer Learning)  
- **GUI Framework**: PyQT  
- **Data Handling**: Pandas, NumPy  
- **Visualization**: PyQT Widgets  

---

## Installation  

1. Clone this repository:  
   ```bash  
   git clone https://github.com/your_username/product-attribute-prediction.git  
   cd product-attribute-prediction
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
3. Run the aplication
   ```bash
   python main.py

---

## Usage
1. Open the GUI by running the main.py file.
2. Load a product image and optionally provide metadata.
3. View predicted attributes for the product in the GUI.
4. Export predictions if needed for further use.


## File structure
```graphql
mango-attribute-prediction/  
│  
├── custom_widgets/ 
├── icons/
├── style/               # Style files
├── test_assets/         # Support files 
│  
├── MangoLocoPrediction.csv  # Predictions obtained from the test dataset
│  
├── params4b2            # Coefficnets of our trained model
│    
├── Mango_CNN.ipynb      # Defining and training of the CNN  
│  
├── utils/               # Eines auxiliars per preprocessar i avaluar dades  
│   └── dictionary_types.py  # Definició de tipus de diccionari per atributs  
│  
├── app.py               # GUI script
├── requirements.txt
├── README.md
└── LICENSE

    
