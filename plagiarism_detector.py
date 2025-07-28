from difflib import SequenceMatcher
import sys

try:
    file1_path = sys.argv[1]
    file2_path = sys.argv[2]
except IndexError:
    print("Error: Please provide two file paths as command line arguments.")
    sys.exit(1)

try:
    with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
        text1 = file1.read()
        text2 = file2.read()
except FileNotFoundError as e:
    print(f"Error: {str(e)}")
    sys.exit(1)

similarity = SequenceMatcher(None, text1, text2).ratio()
print(f"Similarity: {similarity * 100:.2f}%")
