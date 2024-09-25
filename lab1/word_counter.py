import os

def file_reader(input_file):
    if input_file == "":
        raise ValueError("Input file name cannot be empty")
    elif os.path.exists(input_file) == False:
        raise FileNotFoundError(f"File {input_file} not found")
    else:
        with open(input_file, 'r') as file:
            words = file.read().split()
        return words

def word_counter(words):
    word_num = 0
    unique_words = []
    unique_words_num = 0
    for word in words:
        word = word.strip('.,!?()[]{}"').lower()
        word_num += 1
        if word not in unique_words:
            unique_words.append(word)
            unique_words_num += 1
    return word_num, unique_words_num

def main():
    words = file_reader("words.txt")
    word_num, unique_words_num = word_counter(words)
    print(f'The number of words is {word_num}')
    print(f'The number of unique words is {unique_words_num}')

if __name__ == '__main__':
    main()
    