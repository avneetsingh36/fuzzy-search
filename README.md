# Search and Highlight Text Project

## Overview

This Python script searches for a specified phrase or word in a text file and highlights it if found. The script takes user input for the search phrase, and if found, it prints the surrounding context with the phrase highlighted in blue. The script also counts the number of instances the phrase appears in the text and notifies the user if there might be a typo in their search query.

## Requirements

- Python 3.x
- colorama library: Install using pip install colorama

## Usage

Clone the repository or download the script.
Ensure that the text file you want to search is accessible.
Modify the file path in the script to point to your text file. Replace the following line with the correct path to your text file:

```
with open("/Users/rest/of/your/path/md.txt", mode = 'r', encoding="utf-8")
```

Run the script using python script_name.py
Enter the phrase or word you want to search for when prompted.
Type "okay" to continue with the search.
Review the highlighted results and the total number of mentions of the phrase in the text.
Optionally, you can choose to see the entire text with the search phrase highlighted.

## Notes

The script is case-insensitive for the search.
If the search phrase has more than five characters, the script will also search for the phrase with one character added or subtracted, to account for potential typos.

### License

This project is open source and available for use under the terms of the MIT License.
