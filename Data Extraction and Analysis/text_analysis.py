import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import string
import os
import re

# Load NLTK data
nltk.download('punkt')
nltk.download('stopwords')

# Load stop words
stop_words_dir = 'StopWords'
stop_words_files = ['StopWords_Auditor.txt', 'StopWords_Currencies.txt', 'StopWords_DatesandNumbers.txt', 'StopWords_Generic.txt', 'StopWords_GenericLong.txt', 'StopWords_Geographic.txt', 'StopWords_Names.txt']
stop_words = set()
for file in stop_words_files:
    with open(os.path.join(stop_words_dir, file), 'r', encoding='latin-1') as f:
        stop_words.update(f.read().split())

# Load positive and negative words
positive_words = set()
negative_words = set()
with open('MasterDictionary/positive-words.txt', 'r', encoding='latin-1') as f:
    positive_words.update(f.read().split())
with open('MasterDictionary/negative-words.txt', 'r', encoding='latin-1') as f:
    negative_words.update(f.read().split())

# Define function to calculate syllables in a word
def count_syllables(word):
    word = word.lower()
    count = 0
    vowels = "aeiou"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("es") or word.endswith("ed"):
        count -= 1
    if count == 0:
        count += 1
    return count

# Define function to calculate text analysis metrics
def analyze_text(text):
    # Tokenize sentences
    sentences = sent_tokenize(text)
    num_sentences = len(sentences)

    # Tokenize words and filter out stop words and punctuation
    words = word_tokenize(text)
    words = [word for word in words if word.isalpha() and word.lower() not in stop_words]

    # Calculate word count
    word_count = len(words)

    # Calculate positive and negative scores
    positive_score = sum(1 for word in words if word.lower() in positive_words)
    negative_score = sum(1 for word in words if word.lower() in negative_words)

    # Calculate polarity score
    polarity_score = (positive_score - negative_score) / ((positive_score + negative_score) + 0.000001)

    # Calculate subjectivity score
    subjectivity_score = (positive_score + negative_score) / (word_count + 0.000001)

    # Calculate average sentence length
    avg_sentence_length = word_count / num_sentences

    # Calculate complex words
    complex_words = [word for word in words if count_syllables(word) > 2]
    complex_word_count = len(complex_words)
    percentage_of_complex_words = (complex_word_count / word_count) * 100

    # Calculate fog index
    fog_index = 0.4 * (avg_sentence_length + percentage_of_complex_words)

    # Calculate average number of words per sentence
    avg_number_of_words_per_sentence = word_count / num_sentences

    # Calculate syllables per word
    syllables_per_word = sum(count_syllables(word) for word in words) / word_count

    # Calculate personal pronouns
    personal_pronouns = len(re.findall(r'\b(I|we|my|ours|us)\b', text, re.I))

    # Calculate average word length
    avg_word_length = sum(len(word) for word in words) / word_count

    return [positive_score, negative_score, polarity_score, subjectivity_score, avg_sentence_length,
            percentage_of_complex_words, fog_index, avg_number_of_words_per_sentence, complex_word_count,
            word_count, syllables_per_word, personal_pronouns, avg_word_length]

# Load the output data structure template
output_template = 'Output Data Structure.xlsx'
output_df = pd.read_excel(output_template)

# Analyze each article
for index, row in output_df.iterrows():
    url_id = row['URL_ID']
    try:
        with open(f'articles/{url_id}.txt', 'r', encoding='utf-8') as file:
            text = file.read()
        analysis_results = analyze_text(text)
        for i, col in enumerate(output_df.columns[2:], start=2):
            output_df.at[index, col] = analysis_results[i-2]
    except Exception as e:
        print(f"Failed to analyze {url_id}: {e}")

# Save the output
output_df.to_excel('Output.xlsx', index=False)
print("Text analysis completed.")
