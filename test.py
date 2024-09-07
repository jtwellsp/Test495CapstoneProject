import os

# Print the current working directory
print("Current Working Directory:", os.getcwd())

import csv
import spacy
import warnings
import pandas as pd
import re
from nltk.tokenize import word_tokenize

warnings.filterwarnings("ignore", category=FutureWarning)

input_file = r"BBC_train_full.csv"
output_file = r"BBC_train_full_tokens.csv"

nlp = spacy.load("en_core_web_sm")

def preprocess_text(text):
    # Remove digits using regex
    text = re.sub(r'£\d+(?:\.\d+)?|€\d+(?:\.\d+)?|\$\d+(?:\.\d+)?', '', text)
    text = re.sub(r'\b\d+(\.\d+)?\b', '', text)
    text = text.replace('-', '')
    text = text.replace("'", '')
    text = text.replace(".", '')
    return text

with open(input_file, 'r', newline='', encoding='utf-8') as infile, \
    open(output_file, 'w', newline = '', encoding = 'utf-8') as outfile:
    # Create a CSV reader + writer object
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    # Iterate through each row in the CSV
    for row in reader:
        # Assume the text to tokenize is in the correct column
        #Change to 0 for test data, 1 for BBC(labels are in column 0)
        text = row[1]

        preprocessed_text = preprocess_text(text)
        # Process the text using spaCy
        doc = nlp(preprocessed_text)
        # Remove stop words, punctuation, and words under 2 digits.
        filtered_tokens = [token.text.strip() for token in doc if not token.is_stop and not token.is_punct and not token.text.isdigit()]

        filtered_tokens = [token for token in filtered_tokens if token]
        # output post-filtering to new .csv file
        if filtered_tokens:
            writer.writerow(filtered_tokens)
        
        
print(f"Processed data has been written to {output_file}")
