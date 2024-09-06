import os
os.chdir(r"E:\49500Capstone\49500")  # Change to the directory where your CSV file is
# Print the current working directory
print("Current Working Directory:", os.getcwd())

import csv
import spacy
import warnings

warnings.filterwarnings("ignore", category=FutureWarning)

input_file = r"test_data.csv"
output_file = r"test_data_tokens.csv"

nlp = spacy.load("en_core_web_sm")
with open(input_file, 'r', newline='', encoding='utf-8') as infile, \
    open(output_file, 'w', newline = '', encoding = 'utf-8') as outfile :
    # Create a CSV reader object
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    # Iterate through each row in the CSV
    for row in reader:
        # Assume the text to tokenize is in the first column
        text = row[0]

        # Process the text using spaCy
        doc = nlp(text)
        # Remove stop words
        filtered_tokens = [token.text for token in doc if not token.is_stop and not token.is_punct and len(token.text.strip()) > 1 ]


        # Print the text excluding stop words
        writer.writerow(filtered_tokens)
print(f"Processed data has been written to {output_file}")
