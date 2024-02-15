def wordCount(t):
    word_dict = {}
    with open(t, 'r') as file:
        for line_num, line in enumerate(file, start=1):
            words = line.strip().split()
            for word in words:
                if word in word_dict:
                    if line_num not in word_dict[word]:
                        word_dict[word].append(line_num)
                else:
                    word_dict[word] = [line_num]
    return word_dict

# Example:
result = wordCount('text_file.txt')
print(result)
