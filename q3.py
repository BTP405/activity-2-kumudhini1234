def wordCount(t):
# def wordCount(t):

def wordCount(t):
    try:
        word_dict = {}

        with open(t, 'r') as file:
            for line_number, line in enumerate(file, start=1):
                words = line.strip().split()
                for word in words:
                    # If the word is already in the dictionary, append the line number
                    if word in word_dict:
                        word_dict[word].append(line_number)
                    else:
                        # If the word is not in the dictionary, create a new entry
                        word_dict[word] = [line_number]

        return word_dict

    except FileNotFoundError:
        print(f"Error: File '{t}' not found.")
        return None

# Example usage:
file_path = 'text_file.txt'  # Replace with your file path
result = wordCount(file_path)

if result is not None:
    for word, line_numbers in result.items():
        print(f"{word}: {line_numbers}")
