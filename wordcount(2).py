import os
import string
import heapq

class WordCount:
    def __init__(self):
        self.word_counts = {}

    def process_text(self, text):
        word = ''
        for char in text:
            if char.isalnum():
                word += char.lower()
            elif word:
                self.word_counts[word] = self.word_counts.get(word, 0) + 1
                word = ''
        if word:  # Process last word
            self.word_counts[word] = self.word_counts.get(word, 0) + 1

    def fuzzy_search(self, word):
        
        return word if word in self.word_counts else None

    def top_words(self, k):
        return heapq.nlargest(k, self.word_counts.items(), key=lambda item: item[1])

def read_large_file(file_path, chunk_size=1024*1024):
    with open(file_path, 'r') as file:
        while True:
            chunk = file.read(chunk_size)
            if not chunk:
                break
            yield chunk

def main():
    word_counter = WordCount()
    file_path = 'large_text_file.txt'
    
    for chunk in read_large_file(file_path):
        word_counter.process_text(chunk)

    k = 10 
    top_words = word_counter.top_words(k)
    print("Top {} words:".format(k))
    for word, count in top_words:
        print("{}: {}".format(word, count))

if __name__ == "__main__":
    main()
