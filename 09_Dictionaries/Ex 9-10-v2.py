def create_word_index(input_file, output_file):
    word_dict = {}
    
    # Read the input file line by line
    with open(input_file, 'r') as file:
        line_number = 1
        for line in file:
            # Split the line into words
            words = line.strip().split()
            for word in words:
                # Remove punctuation and convert to lowercase
                # word = ''.join(char for char in word if char.isalnum()).lower()
                # Add line number to the word's entry in the dictionary
                if word:
                    if word not in word_dict:
                        word_dict[word] = []
                    word_dict[word].append(line_number)
            line_number += 1

    # Write the word index to the output file
    with open(output_file, 'w') as file:
        for word in sorted(word_dict):
            line_numbers = ", ".join(map(str, word_dict[word]))
            file.write(f"{word}: {line_numbers}\n")

# Example usage
create_word_index("./09_Dictionaries/Kennedy.txt", "./09_Dictionaries/index.txt")
