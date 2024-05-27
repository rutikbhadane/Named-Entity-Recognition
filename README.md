# Named Entity Recognition (NER) with BiLSTM and LSTM

This repository contains the implementation of a Named Entity Recognition (NER) model using Bi-directional Long Short-Term Memory (BiLSTM) and LSTM layers. The project includes data preprocessing, model training, and deployment through a Streamlit application.

## Project Overview

The goal of this project is to build and deploy a model that can accurately identify named entities in text data. The project is divided into the following sections:

1. **Data Preprocessing:** Handling missing values, encoding categorical variables, and padding sequences.
2. **Model Training:** Implementing and training a BiLSTM-LSTM model to recognize entities.
3. **Model Deployment:** Integrating the trained model into a Streamlit application for real-time entity extraction.

## Repository Structure

- `NER_Model.ipynb`: Jupyter Notebook containing the data preprocessing, model training, and evaluation.
- `main.py`: Streamlit application for deploying the trained NER model.
- `ner_dataset.csv`: Dataset used for training the NER model.

## Requirements

- Python 3.6+
- pandas
- numpy
- itertools
- scikit-learn
- keras
- tensorflow
- spacy
- streamlit

## Setup and Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ner-bilstm-lstm.git
   cd ner-bilstm-lstm

## Usage
Run the Jupyter Notebook:

Open and run NER_Model.ipynb to preprocess the data and train the NER model.
Save the trained model weights.
Deploy the Streamlit app:

Place the trained model weights in the appropriate path.
Run the Streamlit application:
```bash
streamlit run main.py
```
Interact with the app:

Open your web browser and navigate to the URL provided by Streamlit.
Enter text in the input area to extract named entities.
## Results
The trained NER model effectively identifies named entities with high accuracy. The Streamlit application provides an intuitive interface for users to input text and view the extracted entities in real-time.

