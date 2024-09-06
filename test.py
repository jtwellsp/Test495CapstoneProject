import os
os.chdir(r"E:\49500Capstone\49500")  # Change to the directory where your CSV file is
# Print the current working directory
print("Current Working Directory:", os.getcwd())

import csv
import spacy
import warnings

warnings.filterwarnings("ignore", category=FutureWarning)

file_name = r"test_data.csv"
nlp = spacy.load("en_core_web_sm")
nlp.Defaults.stop_words |= {"s"}


# Process the text
text = "blair prepares to name poll date tony blair is likely to name 5 may as election day when parliament returns from its easter break  the bbc s political editor has learned.  andrew marr says mr blair will ask the queen on 4 or 5 april to dissolve parliament at the end of that week. mr blair has so far resisted calls for him to name the day but all parties have stepped up campaigning recently. downing street would not be drawn on the claim  saying election timing was a matter for the prime minister.  a number 10 spokeswoman would only say:  he will announce an election when he wants to announce an election.  the move will signal a frantic week at westminster as the government is likely to try to get key legislation through parliament. the government needs its finance bill  covering the budget plans  to be passed before the commons closes for business at the end of the session on 7 april.  but it will also seek to push through its serious and organised crime bill and id cards bill. mr marr said on wednesday s today programme:  there s almost nobody at a senior level inside the government or in parliament itself who doesn t expect the election to be called on 4 or 5 april.  as soon as the commons is back after the short easter recess  tony blair whips up to the palace  asks the queen to dissolve parliament ... and we re going.  the labour government officially has until june 2006 to hold general election  but in recent years governments have favo"


doc = nlp(text)

# Remove stop words
filtered_tokens = [token.text for token in doc if not token.is_stop and token.text.strip()]

# Print the text excluding stop words
print(filtered_tokens)