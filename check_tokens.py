import re
import os
import csv

pattern = r'([a-zA-Z]{2,})|[\d]+|[¬£]\d+'


input_file = r"test_data_tokens.csv"

def check_string(input_string):
    if not re.match(pattern, input_string):
        print(f"'{input_string}' does not match the pattern")
        
with open(input_file, 'r', newline='', encoding='utf-8') as infile:
        reader = csv.reader(infile)

        for row in reader:
            for cell in row:  # Check every cell in every row
                check_string(cell)
            
print('File done.')
