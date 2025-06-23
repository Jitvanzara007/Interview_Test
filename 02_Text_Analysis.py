''' 
clean the paragraph by converting to lowercase and removing punctuation
clear common stop words (like 'the', 'is', 'at' 'in', etc.)

Count how often each word appears
Filter and return the top-3 words that start with th, sorted by frequency '''




from collections import Counter
import re

def remove_words(text):
    # clear stop words.
    stop_words = {'the', 'is', 'at', 'on', 'in', 'and', 'a', 'to', 'of', 'for', 
                  'with', 'that', 'this', 'it', 'as', 'by', 'an', 'be', 'are'}
    
    # Make everything lowercase and remove punctuation
    words = re.findall(r'\b\w+\b', text.lower())
    return Counter(word for word in words if word not in stop_words)



def get_top_words(word_counts, prefix='', n=3):
    filtered = {word: count for word, count in word_counts.items() if word.startswith(prefix)}
    return Counter(filtered).most_common(n)

# Example 
text = "Think that the theory thrives. Thanks to the thinkers."
word_counts = remove_words(text)
top_words = get_top_words(word_counts, prefix='th', n=3)

print("Top 3 words starting with 'th':", top_words)
