import nltk
import string
from heapq import nlargest

# Ensure necessary NLTK data is downloaded
# nltk.download('stopwords')
# nltk.download('punkt')

def summarize_text(text):
    # Determine the number of sentences for the summary
    sentence_count = text.count(". ")
    length = int(round(sentence_count / 10, 0)) if sentence_count > 20 else 1

    # Remove punctuation from the text
    nopuch = ''.join([char for char in text if char not in string.punctuation])

    # Tokenize the text into words and remove stopwords
    stopwords = set(nltk.corpus.stopwords.words('english'))
    words = [word for word in nopuch.split() if word.lower() not in stopwords]

    # Calculate word frequencies
    word_freq = {}
    for word in words:
        if word not in word_freq:
            word_freq[word] = 1
        else:
            word_freq[word] += 1

    max_freq = max(word_freq.values())
    for word in word_freq:
        word_freq[word] /= max_freq

    # Tokenize the text into sentences
    sent_list = nltk.sent_tokenize(text)

    # Score each sentence based on word frequencies
    sent_score = {}
    for sent in sent_list:
        for word in nltk.word_tokenize(sent.lower()):
            if word in word_freq:
                if sent not in sent_score:
                    sent_score[sent] = word_freq[word]
                else:
                    sent_score[sent] += word_freq[word]

    # Select the top sentences to form the summary
    summary_sents = nlargest(length, sent_score, key=sent_score.get)
    summary = ' '.join(summary_sents)

    return summary

# Get input from the user
user_text = input("Enter text to summarize: ")

# Summarize the text
summary = summarize_text(user_text)

# Print the summary
print("Summary:")
print(summary)
