# Read a .txt file and print its contents
file_path = 'doc.txt'
with open(file_path, 'r') as file:
    contents = file.read()
    # print(contents) 


# Reads a .txt file and prints the top 5 most common words.
from collections import Counter
import re   
file_path = 'doc.txt'
with open(file_path, 'r') as file:
    contents = file.read().lower()
    words = re.findall(r'\b\w+\b', contents)
    word_counts = Counter(words)
    most_common_words = word_counts.most_common(5)
    print(most_common_words)




