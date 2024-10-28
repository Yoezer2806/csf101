def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()

def count_lines(content):
    return len(content.split('\n'))

def count_words(content):
    return len(content.split())

from collections import Counter

def most_common_word(content):
    words = content.lower().split()
    word_counts = Counter(words)
    return word_counts.most_common(1)[0]

def unique_word_count(content):
    words = set(content.lower().split())
    return len(words)

def longest_word(content):
    words = content.split()
    return max(words, key=len)

def count_specific_word(content, word):
    words = content.lower().split()
    return words.count(word.lower())

def average_word_length(content):
    words = content.split()
    total_length = sum(len(word) for word in words)
    return total_length / len(words)

def percentage_longer_than_average(content):
    words = content.split()
    avg_length = average_word_length(content)
    longer_words = [word for word in words if len(word) > avg_length]
    return (len(longer_words) / len(words)) * 100 if words else 0

def analyze_text(filename):
    content = read_file(filename)
    
    num_lines = count_lines(content)
    num_words = count_words(content)
    common_word, common_count = most_common_word(content)
    num_unique_words = unique_word_count(content)
    longest = longest_word(content)
    avg_length = average_word_length(content)
    specific_word_count = count_specific_word(content, "the")  # Example specific word
    percentage_long = percentage_longer_than_average(content)
    
    print(f"File: {filename}")
    print(f"Number of lines: {num_lines}")
    print(f"Number of words: {num_words}")
    print(f"Number of unique words: {num_unique_words}")
    print(f"Most common word: '{common_word}' (appears {common_count} times)")
    print(f"Longest word: '{longest}'")
    print(f"Occurrences of the word 'the': {specific_word_count}")  # Example specific word
    print(f"Average word length: {avg_length:.2f} characters")
    print(f"Percentage of words longer than average: {percentage_long:.2f}%")

# Run the analysis
analyze_text('C:\\Users\\Dell\\OneDrive\\Desktop\\CSF\\Assigment\\SWE\\sample.text')
