import streamlit as st
import pandas as pd
import numpy as np
import spacy
from spacy import displacy
from keras.preprocessing.sequence import pad_sequences
from keras.utils import to_categorical

# Load the trained model
model = spacy.load('en_core_web_sm')

# Define the Streamlit app
def main():
    st.title("Named Entity Recognition with Streamlit")

    # Create a text area for user input
    text_input = st.text_area("Enter text:")

    # When user clicks the button
    if st.button("Extract Named Entities"):
        # Process the text with your NER model
        doc = model(text_input)

        # Display the named entities
        st.write("Named Entities:")
        entities = []
        for ent in doc.ents:
            entities.append([ent.text, ent.label_])
        
        entities_df = pd.DataFrame(entities, columns=['Entity', 'Label'])
        st.dataframe(entities_df)

# Run the Streamlit app
if __name__ == "__main__":
    main()
